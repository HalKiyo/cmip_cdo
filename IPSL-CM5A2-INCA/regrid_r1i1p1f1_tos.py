import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from cmip_remap import NCO_DIR, run  # noqa: E402


def main():
    run(
        variable='tos',
        realm='Omon',
        model='IPSL-CM5A2-INCA',
        periods=[(1850, 2014)],
        data_dir=NCO_DIR,
    )


if __name__ == '__main__':
    main()
