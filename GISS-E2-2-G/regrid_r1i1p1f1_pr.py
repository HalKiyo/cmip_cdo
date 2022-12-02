import cartopy.crs as ccrs
import xarray as xr
from netCDF4 import Dataset
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'pr'
    realm = 'Amon'
    model = 'GISS-E2-2-G'
    begin_time = 1850
    end_time = 1875

    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(begin_time, end_time))
    for i in range(1876, 1976, 25):
        remap.regrid(*remap.load(i, i+24))
    remap.regrid(*remap.load(1976, 1990))
    remap.regrid(*remap.load(1991, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)

if __name__ == '__main__':
    main()

