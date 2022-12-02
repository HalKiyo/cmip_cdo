import cartopy.crs as ccrs
import xarray as xr
from netCDF4 import Dataset
from cdo import Cdo
import matplotlib.pyplot as plt

def main():
    save_flag = True
    variable = 'mrso'
    realm = 'Lmon'
    variant = 'r1i1p1f1'
    grid = 'gn'
    model = 'ICON-ESM-LR'
    begin_time = 1850
    end_time = 1859

    remap = Remap(save_flag, variable, realm, variant, grid, model)
    remap.regrid(*remap.load(begin_time, end_time))
    for i in range(1860, 2010, 10):
        remap.regrid(*remap.load(i, i+9))
    remap.regrid(*remap.load(2010, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


class Remap():
    def __init__(self, save_flag, variable, realm, variant, grid, model):
        self.save_flag = save_flag
        self.variable = variable
        self.realm = realm
        self.variant = variant
        self.grid = grid
        self.model = model

    def load(self, begin_time, end_time):
        datadir = f"/work/kajiyama/data/cmip6/raw/{self.model}/{self.variable}"
        savedir = f"/work/kajiyama/cdo/cmip6/{self.model}/{self.variable}"
        loadname = f"/{self.variable}_{self.realm}_{self.model}_historical_{self.variant}_{self.grid}_" \
                   f"{begin_time}01-{end_time}12.nc"
        savename = f"/{self.variable}_{begin_time}-{end_time}.nc"
        infile = datadir + loadname
        outfile = savedir + savename
        time_length = (end_time - begin_time + 1) * 12
        return infile, outfile, time_length

    def regrid(self, infile, outfile, time_length):
        cdo = Cdo()
        cdo.remapycon('global_1', input=f"-seltimestep,1/{time_length} -selvar,{self.variable} "+infile, output=outfile)
        print(f'{outfile}: saved')

    def loop(self):
        for i in range(self.start_loop, self.stop_loop+1, self.timestep_loop):
            begin_time, end_time = i, i + self.timestep_loop - 1
            self.regrid(*self.load(begin_time, end_time))

    def plot(self, infile, origin='lower'):
        cdo = Cdo()
        projection = ccrs.PlateCarree(central_longitude=180)
        img_extent = (-180,180,-90,90)
        val = cdo.remapycon('global_1', input=f'-seltimestep,1 '+infile, returnXArray=f"{self.variable}")
        if self.variable == 'tsl':
            data = val[0,0,:,:].plot(subplot_kws=dict(projection=projection,facecolor='gray'),
                           transform=projection)
        else:
            data = val.plot(subplot_kws=dict(projection=projection,facecolor='gray'),
                           transform=projection)
        data.axes.coastlines()
        plt.show()


if __name__ == '__main__':
    main()

