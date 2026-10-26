import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='CMCC-CM2-HR4',
        periods=chunks(1850, 2000, 25) + [(2000, 2014)],
    )


if __name__ == '__main__':
    main()
