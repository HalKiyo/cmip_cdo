import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import run  # noqa: E402


def main():
    run(
        variable='tsl',
        realm='Lmon',
        model='MIROC-ES2H',
        variant='r1i1p4f2',
        periods=[(1850, 2014)],
        plot_mode='first',
    )


if __name__ == '__main__':
    main()
