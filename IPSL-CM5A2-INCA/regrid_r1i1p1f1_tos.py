import cartopy.crs as ccrs
import xarray as xr
from netCDF4 import Dataset
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'tos'
    realm = 'Omon'
    variant = 'r1i1p1f1'
    grid = 'gn'
    model = 'IPSL-CM5A2-INCA'
    begin_time = 1850
    end_time = 2014

    remap = Remap(save_flag, variable, realm, variant, grid, model)
    remap.regrid(*load(begin_time, end_time))
    inp, _, _ = load(begin_time, end_time)
    remap.plot(inp)

def load(begin_time, end_time):
    save_flag = True
    variable = 'tos'
    realm = 'Omon'
    variant = 'r1i1p1f1'
    grid = 'gn'
    model = 'IPSL-CM5A2-INCA'

    datadir = f"/work/kajiyama/nco/cmip6/{model}/{variable}"
    savedir = f"/work/kajiyama/cdo/cmip6/{model}/{variable}"
    loadname = f"/{variable}_{realm}_{model}_historical_{variant}_{grid}_" \
               f"{begin_time}01-{end_time}12.nc"
    savename = f"/{variable}_{begin_time}-{end_time}.nc"
    infile = datadir + loadname
    outfile = savedir + savename
    time_length = (end_time - begin_time + 1) * 12
    return infile, outfile, time_length

if __name__ == '__main__':
    main()

