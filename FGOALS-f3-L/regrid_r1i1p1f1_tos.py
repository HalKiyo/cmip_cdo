import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='FGOALS-f3-L',
        periods=[(1850, 2014)],
    )


if __name__ == '__main__':
    main()
