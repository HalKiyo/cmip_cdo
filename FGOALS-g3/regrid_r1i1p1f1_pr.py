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
    model = 'FGOALS-g3'
    begin_time = 1850
    end_time = 1859

    remap = Remap(save_flag, variable, realm, model)
    for i in range(1850, 2010, 10):
        remap.regrid(*remap.load(i, i+9))
    remap.regrid(*remap.load(2010, 2016))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)

if __name__ == '__main__':
    main()

