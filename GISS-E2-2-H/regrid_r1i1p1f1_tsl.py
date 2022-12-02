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
    model = 'GISS-E2-2-H'
    begin_time = 1850
    end_time = 1875

    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(begin_time, end_time))
    for i in range(1876, 2001, 25):
        remap.regrid(*remap.load(i, i+24))
    remap.regrid(*remap.load(2001, 2014))
    inp, _, _ = remap.load(begin_time, end_time)
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

