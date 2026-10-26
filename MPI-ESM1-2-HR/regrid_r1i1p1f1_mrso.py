import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='mrso',
        realm='Lmon',
        model='MPI-ESM1-2-HR',
        periods=chunks(1850, 2015, 5),
    )


if __name__ == '__main__':
    main()
