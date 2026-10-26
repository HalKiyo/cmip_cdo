import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='pr',
        realm='Amon',
        model='GISS-E2-2-H',
        periods=[(1850, 1875)] + chunks(1876, 2001, 25) + [(2001, 2014)],
    )


if __name__ == '__main__':
    main()
