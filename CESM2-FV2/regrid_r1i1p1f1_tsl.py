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
    model = 'CESM2-FV2'
    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(1850, 1899))
    remap.regrid(*remap.load(1900, 1949))
    remap.regrid(*remap.load(1950, 1999))
    remap.regrid(*remap.load(2000, 2014))
    inp, _, _ = remap.load(1850, 1899)
    plot(inp)

def plot(infile, origin='lower'):
    cdo = Cdo()
    projection = ccrs.PlateCarree(central_longitude=180)
    img_extent = (-180,180,-90,90)
    val = cdo.remapbil('r360x180', input=f'-seltimestep,1 '+infile, returnXArray='tsl')
    data = val[0,0,:,:].plot(subplot_kws=dict(projection=projection,facecolor='gray'),
                   transform=projection)
    data.axes.coastlines()
    plt.show()


if __name__ == '__main__':
    main()

