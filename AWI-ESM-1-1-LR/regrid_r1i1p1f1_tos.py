import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='AWI-ESM-1-1-LR',
        periods=[(1850, 1850)] + chunks(1851, 2011, 10) + [(2011, 2014)],
        plot_period=(2011, 2014),
        method='remapycon',
        target='global_1',
    )


if __name__ == '__main__':
    main()
