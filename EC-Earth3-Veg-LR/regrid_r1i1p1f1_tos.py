import cartopy.crs as ccrs
import xarray as xr
from netCDF4 import Dataset
from cdo import Cdo
import matplotlib.pyplot as plt

def main():
    save_flag = True
    variable = 'tos'
    realm = 'Omon'
    model = 'EC-Earth3-Veg-LR'
    begin_time = 1850
    end_time = 1850

    remap = Remap(save_flag, variable, realm, model)
    for i in range(1850,2015):
        remap.regrid(*remap.load(i, i))
    inp, _, _ = remap.load(begin_time, end_time)
    remap.plot(inp)


class Remap():
    def __init__(self, save_flag, variable, realm, model):
        self.save_flag = save_flag
        self.variable = variable
        self.realm = realm
        self.model = model

    def load(self, begin_time, end_time):
        datadir = f"/work/kajiyama/data/cmip6/raw/{self.model}/{self.variable}"
        savedir = f"/work/kajiyama/cdo/cmip6/{self.model}/{self.variable}"
        loadname = f"/{self.variable}_{self.realm}_{self.model}_historical_r1i1p1f1_gn_" \
                   f"{begin_time}01-{end_time}12.nc"
        savename = f"/{self.variable}_{begin_time}-{end_time}.nc"
        infile = datadir + loadname
        outfile = savedir + savename
        time_length = (end_time - begin_time + 1) * 12
        return infile, outfile, time_length

    def regrid(self, infile, outfile, time_length):
        cdo = Cdo()
        if self.save_flag == True:
            cdo.remapbil('r360x180', input=f"-seltimestep,1/{time_length} -selvar,{self.variable} "+infile, output=outfile)
            print(f'{outfile}: saved')
        else:
            print("outfile is NOT saved yet")

    def plot(self, infile, origin='lower'):
        cdo = Cdo()
        projection = ccrs.PlateCarree(central_longitude=180)
        img_extent = (-180,180,-90,90)
        val = cdo.remapbil('r360x180', input=f'-seltimestep,1 '+infile, returnXArray=f"{self.variable}")
        data = val.plot(subplot_kws=dict(projection=projection,facecolor='gray'),
                       transform=projection)
        data.axes.coastlines()
        plt.show()


if __name__ == '__main__':
    main()

