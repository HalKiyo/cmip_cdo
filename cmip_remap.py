"""Shared helper for regridding CMIP6 historical monthly data with CDO.

Every model directory holds thin wrapper scripts (regrid_r1i1p1f1_<var>.py)
that only declare their settings and call run() from this module.
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
from cdo import Cdo

# Input and output roots on the analysis machine
RAW_DIR = "/work/kajiyama/data/cmip6/raw"
NCO_DIR = "/work/kajiyama/nco/cmip6"
SAVE_DIR = "/work/kajiyama/cdo/cmip6"

# Default CDO remapping operator and target grid
DEFAULT_METHOD = 'remapbil'
DEFAULT_TARGET = 'r360x180'


def chunks(start, stop, step):
    """Return (begin, end) year pairs, one for each i in range(start, stop, step)."""
    return [(i, i + step - 1) for i in range(start, stop, step)]


class Remap():
    def __init__(self, variable, realm, model, variant='r1i1p1f1', grid='gn',
                 save_flag=True, method=DEFAULT_METHOD, target=DEFAULT_TARGET,
                 data_dir=RAW_DIR, plot_mode='full'):
        self.variable = variable
        self.realm = realm
        self.model = model
        self.variant = variant
        self.grid = grid
        self.save_flag = save_flag
        self.method = method
        self.target = target
        self.data_dir = data_dir
        # 'full' plots the field as is, 'first' plots [0, 0, :, :]
        # and 'mean' plots the mean over axis 1 (soil depth for tsl)
        self.plot_mode = plot_mode

    def load(self, begin_time, end_time):
        datadir = f"{self.data_dir}/{self.model}/{self.variable}"
        savedir = f"{SAVE_DIR}/{self.model}/{self.variable}"
        loadname = f"/{self.variable}_{self.realm}_{self.model}_historical_{self.variant}_{self.grid}_" \
                   f"{begin_time}01-{end_time}12.nc"
        savename = f"/{self.variable}_{begin_time}-{end_time}.nc"
        infile = datadir + loadname
        outfile = savedir + savename
        time_length = (end_time - begin_time + 1) * 12
        return infile, outfile, time_length

    def regrid(self, infile, outfile, time_length):
        if self.save_flag is True:
            cdo = Cdo()
            remap = getattr(cdo, self.method)
            remap(self.target, input=f"-seltimestep,1/{time_length} -selvar,{self.variable} "+infile, output=outfile)
            print(f'{outfile}: saved')
        else:
            print("outfile is NOT saved yet")

    def plot(self, infile):
        cdo = Cdo()
        projection = ccrs.PlateCarree(central_longitude=180)
        remap = getattr(cdo, self.method)
        val = remap(self.target, input='-seltimestep,1 '+infile, returnXArray=f"{self.variable}")
        if self.plot_mode == 'first':
            val = val[0,0,:,:]
        elif self.plot_mode == 'mean':
            val = np.mean(val, axis=1)
        data = val.plot(subplot_kws=dict(projection=projection,facecolor='gray'),
                        transform=projection)
        data.axes.coastlines()
        plt.show()


def run(variable, realm, model, periods, plot_period=None, **kwargs):
    """Regrid every (begin, end) period in order, then plot the first time step of plot_period.

    plot_period defaults to the first entry of periods. Other keyword
    arguments are passed to Remap.
    """
    remap = Remap(variable, realm, model, **kwargs)
    for begin_time, end_time in periods:
        remap.regrid(*remap.load(begin_time, end_time))
    if plot_period is None:
        plot_period = periods[0]
    inp, _, _ = remap.load(*plot_period)
    remap.plot(inp)
