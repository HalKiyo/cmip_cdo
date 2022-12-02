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
    model = 'TaiESM1'
    begin_time = 1850
    end_time = 1850

    remap = Remap(save_flag, variable, realm, variant, grid, model)
    remap.regrid(*remap.load(begin_time, end_time))
    for i in range(1851, 2015):
        remap.regrid(*remap.load(i, i))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


if __name__ == '__main__':
    main()
