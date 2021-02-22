from icecream import ic
import json
import sys

from config.paths import DIST_DIR, MATCH_DATA_DIR
from gamerecord_paths.core import get_paths_dict, get_paths_list


def export_path_list():
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(DIST_DIR / 'paths_list.json'), 'w+') as f:
        jsonized_paths = json.dumps(
            get_paths_list(MATCH_DATA_DIR),
            indent=2
        )
        f.write(jsonized_paths)


if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        raise RuntimeError(
            'use like: python main.py [method: export_path_list, etc]'
        )

    method = sys.argv[1]
    if method == 'export_path_list':
        export_path_list()
    else:
        raise RuntimeError(
            'use like: python main.py [method: export_path_list, etc]'
        )
