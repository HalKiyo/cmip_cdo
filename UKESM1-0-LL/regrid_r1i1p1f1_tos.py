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
    variant = 'r1i1p1f2'
    grid = 'gn'
    model = 'UKESM1-0-LL'
    begin_time = 1850
    end_time = 1949

    remap = Remap(save_flag, variable, realm, variant, grid, model)
    remap.regrid(*remap.load(begin_time, end_time))
    remap.regrid(*remap.load(1950, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


if __name__ == '__main__':
    main()

