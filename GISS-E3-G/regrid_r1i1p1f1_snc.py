import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='snc',
        realm='LImon',
        model='GISS-E3-G',
        grid='gr',
        periods=chunks(1850, 2000, 50) + [(2000, 2014)],
    )


if __name__ == '__main__':
    main()
