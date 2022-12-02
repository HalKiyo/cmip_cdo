import cartopy.crs as ccrs
import xarray as xr
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'snc'
    realm = 'LImon'
    model = 'CanESM5-CanOE'
    begin_time = 1850
    end_time = 2014

    remap = Remap(save_flag, variable, realm, model)

    inp, out, length = remap.load(begin_time, end_time)
    remap.regrid(inp, out, length)
    remap.plot(inp)


if __name__ == '__main__':
    main()

