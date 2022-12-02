import cartopy.crs as ccrs
import xarray as xr
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'pr'
    realm = 'Amon'
    model = 'CESM2-FV2'
    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(1850, 1899))
    remap.regrid(*remap.load(1900, 1949))
    remap.regrid(*remap.load(1950, 1999))
    remap.regrid(*remap.load(2000, 2014))
    inp, _, _ = remap.load(1850, 1899)
    remap.plot(inp)


if __name__ == '__main__':
    main()

