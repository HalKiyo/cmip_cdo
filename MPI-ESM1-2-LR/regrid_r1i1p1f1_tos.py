import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='MPI-ESM1-2-LR',
        periods=chunks(1850, 2010, 20) + [(2010, 2014)],
    )


if __name__ == '__main__':
    main()
