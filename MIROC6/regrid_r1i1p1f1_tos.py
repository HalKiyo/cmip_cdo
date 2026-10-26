import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='MIROC6',
        periods=[(1850, 1949), (1950, 2014)],
    )


if __name__ == '__main__':
    main()
