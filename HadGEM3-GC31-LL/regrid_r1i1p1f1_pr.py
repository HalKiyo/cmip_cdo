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
    model = 'HadGEM3-GC31-LL'
    begin_time = 1850
    end_time = 1949

    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(begin_time, end_time))
    remap.regrid(*remap.load(1950, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)

if __name__ == '__main__':
    main()

