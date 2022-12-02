import cartopy.crs as ccrs
import xarray as xr
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'snc'
    realm = 'LImon'
    variant = 'r1i1p1f1'
    grid = 'gn'
    model = 'MRI-ESM2-0'
    begin_time = 1850
    end_time = 2014

    remap = Remap(save_flag, variable, realm, variant, grid, model)
    remap.regrid(*remap.load(begin_time, end_time))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


if __name__ == '__main__':
    main()

