from icecream import ic
import json
import sys
from statistics import mean, median

from config import MATCH_NUMBER
from config.paths import DIST_DIR, MATCH_DATA_DIR, SHOT_PATTERNS_PATH
from gamerecord_paths.core import get_paths_list
from analyze_match_data import extract_patterns


def export_path_list() -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(DIST_DIR / 'path_list.json'), 'w+') as f:
        jsonized_paths = json.dumps(
            get_paths_list(MATCH_DATA_DIR),
            indent=2
        )
        f.write(jsonized_paths)


def convert_for_csharp() -> None:
    with open(str(SHOT_PATTERNS_PATH), 'r') as f:
        json_data = json.loads(f.read())

    formatted = []

    for key in json_data.keys():
        winner_pos, loser_pos, target_pos, shot_type = key.split(',')
        data = json_data[key]
        count = data['score_count'] + data['fail_count']
        rate = data['score_count'] / count

        formatted.append({
            "WinnerPosition": int(winner_pos),
            "LoserPosition": int(loser_pos),
            "TargetPosition": int(target_pos),
            "ShotType": 1 if shot_type == 'ShotType._Lob' else 0,
            "Count": count,
            "Rate": rate
        })

    rates = [data["Rate"] for data in formatted]

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(DIST_DIR / 'dist_for_csharp.json'), 'w+') as f:
        f.write(json.dumps({
            'Mean': mean(rates),
            'Median': median(rates),
            'Min': min(rates),
            'Max': max(rates),
            'Patterns': formatted,
        }, indent=2))


if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        raise RuntimeError(
            'use like: python main.py [method: export_path_list, etc]'
        )

    method = sys.argv[1]
    if method == 'path_list':
        export_path_list()
    elif method == 'extract':
        extract_patterns(MATCH_NUMBER)
    elif method == 'csharp':
        convert_for_csharp()
    elif method == 'build':  # extract & convert for c#
        extract_patterns(MATCH_NUMBER)
        convert_for_csharp()
    else:
        raise RuntimeError(
            'use like: python main.py [method: export_path_list, etc]'
        )
