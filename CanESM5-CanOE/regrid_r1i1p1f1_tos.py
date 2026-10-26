import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='CanESM5-CanOE',
        variant='r1i1p2f1',
        periods=[(1850, 2014)],
    )


if __name__ == '__main__':
    main()
