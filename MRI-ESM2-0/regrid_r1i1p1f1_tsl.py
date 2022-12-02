import numpy as np
import cartopy.crs as ccrs
import xarray as xr
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'tsl'
    realm = 'Lmon'
    variant = 'r1i1p1f1'
    grid = 'gn'
    model = 'MRI-ESM2-0'
    begin_time = 1850
    end_time = 1899

    remap = Remap(save_flag, variable, realm, variant, grid, model)
    remap.regrid(*remap.load(begin_time, end_time))
    remap.regrid(*remap.load(1900, 1949))
    remap.regrid(*remap.load(1950, 1999))
    remap.regrid(*remap.load(2000, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


if __name__ == '__main__':
    main()

