import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='snc',
        realm='LImon',
        model='HadGEM3-GC31-MM',
        variant='r1i1p1f3',
        periods=chunks(1850, 1970, 20) + [(1970, 1987), (1988, 1989), (1990, 2009), (2010, 2014)],
    )


if __name__ == '__main__':
    main()
