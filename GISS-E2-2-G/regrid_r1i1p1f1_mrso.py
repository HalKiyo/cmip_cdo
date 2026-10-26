import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='mrso',
        realm='Lmon',
        model='GISS-E2-2-G',
        periods=[(1850, 1875)] + chunks(1876, 1976, 25) + [(1976, 1990), (1991, 2014)],
    )


if __name__ == '__main__':
    main()
