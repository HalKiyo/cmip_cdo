import cartopy.crs as ccrs
from cdo import Cdo
import matplotlib.pyplot as plt

def main():
    variable = 'tos'
    realm = 'Omon'
    model = 'AWI-ESM-1-1-LR'
    start_loop = 1851
    stop_loop = 2010
    timestep_loop = 10

    remap = Remap(variable, realm, model, start_loop, stop_loop, timestep_loop)
    remap.regrid(*remap.load(1850, 1850))
    remap.loop()
    remap.regrid(*remap.load(2011, 2014))
    inp, _, _ = remap.load(2011,2014)
    remap.plot(inp)

class Remap():
    def __init__(self, variable, realm, model, start_loop, stop_loop, timestep_loop):
        self.variable = variable
        self.realm = realm
        self.model = model
        self.start_loop = start_loop
        self.stop_loop = stop_loop
        self.timestep_loop = timestep_loop

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
        cdo.remapycon('global_1', input=f"-seltimestep,1/{time_length} -selvar,{self.variable} "+infile, output=outfile)
        print(f'{outfile}: saved')

    def loop(self):
        for i in range(self.start_loop, self.stop_loop+1, self.timestep_loop):
            begin_time, end_time = i, i + self.timestep_loop - 1
            self.regrid(*self.load(begin_time, end_time))

    def plot(self, infile, origin='lower'):
        cdo = Cdo()
        projection = ccrs.PlateCarree(central_longitude=180)
        img_extent = (-180,180,-90,90)
        val = cdo.remapycon('global_1', input=f'-seltimestep,1 '+infile, returnXArray=f"{self.variable}")
        data = val.plot(subplot_kws=dict(projection=projection,facecolor='gray'),
                       transform=projection)
        data.axes.coastlines()
        plt.show()


if __name__ == '__main__':
    main()

