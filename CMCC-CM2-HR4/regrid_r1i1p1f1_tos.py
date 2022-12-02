import cartopy.crs as ccrs
from cdo import Cdo
import matplotlib.pyplot as plt
from regrid_r1i1p1f1_mrso import Remap

def main():
    save_flag = True
    variable = 'tos'
    realm = 'Omon'
    model = 'CMCC-CM2-HR4'

    remap = Remap(save_flag, variable, realm, model)
    remap.regrid(*remap.load(1850, 1874))
    remap.regrid(*remap.load(1875, 1899))
    remap.regrid(*remap.load(1900, 1924))
    remap.regrid(*remap.load(1925, 1949))
    remap.regrid(*remap.load(1950, 1974))
    remap.regrid(*remap.load(1975, 1999))
    remap.regrid(*remap.load(2000, 2014))
    inp, _, _ = remap.load(1850, 1874)
    remap.plot(inp)


if __name__ == '__main__':
    main()

