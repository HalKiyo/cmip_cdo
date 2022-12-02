import cartopy.crs as ccrs
import xarray as xr
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'snc'
    realm = 'LImon'
    model = 'EC-Earth3'
    begin_time = 1850
    end_time = 1850


    remap = Remap(save_flag, variable, realm, model)
    for i in range(1850, 2015):
        remap.regrid(*remap.load(i, i))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


if __name__ == '__main__':
    main()

