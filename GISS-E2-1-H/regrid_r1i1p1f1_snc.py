import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import run  # noqa: E402


def main():
    run(
        variable='snc',
        realm='LImon',
        model='GISS-E2-1-H',
        periods=[(1850, 1900), (1901, 1950), (1951, 2000), (2001, 2014)],
    )


if __name__ == '__main__':
    main()
