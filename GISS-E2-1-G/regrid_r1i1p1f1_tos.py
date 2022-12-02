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
    model = 'GISS-E2-1-G'
    begin_time = 1850
    end_time = 1900

    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(1850, 1900))
    for i in range(1901, 2001, 50):
        remap.regrid(*remap.load(i, i+49))
    remap.regrid(*remap.load(2001, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


if __name__ == '__main__':
    main()

