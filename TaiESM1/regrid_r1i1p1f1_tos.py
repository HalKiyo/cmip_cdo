import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import chunks, run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='TaiESM1',
        periods=chunks(1850, 2015, 1),
    )


if __name__ == '__main__':
    main()
