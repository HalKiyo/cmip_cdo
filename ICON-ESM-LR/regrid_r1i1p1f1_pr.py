import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='pr',
        realm='Amon',
        model='ICON-ESM-LR',
        periods=chunks(1850, 2010, 10) + [(2010, 2014)],
        method='remapycon',
        target='global_1',
    )


if __name__ == '__main__':
    main()
