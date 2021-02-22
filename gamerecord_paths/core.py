from itertools import chain
from pathlib import Path
from datetime import datetime
from pytz import utc


def parse_date(filename: str) -> datetime:
    # TODO: should handle exception
    parsed_str = filename.split("UTC_")[1].split("_file")[0].replace("_", "-")
    year, month, day, hour, minute, second = [
        int(_) for _ in parsed_str.split("-")
    ]
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second, tzinfo=utc)


def is_valid(filename: str) -> bool:
    _min = datetime(2017, 9, 17, tzinfo=utc)
    _max = datetime(2017, 11, 13, tzinfo=utc)

    date = parse_date(filename)
    return _min <= date <= _max


def get_paths_dict(base_path: Path) -> dict:
    paths = {}
    user_paths = [x for x in base_path.iterdir() if x.is_dir()]

    for user_path in user_paths:
        match_path = user_path / 'ACGSRecordings'
        paths[user_path.name] = [
            str(path) for path in match_path.iterdir() if path.is_file() and is_valid(path.name)
        ]

    return paths


def get_paths_list(base_path: Path) -> list:
    return [{"path": path} for path in list(chain(*[path for path in get_paths_dict(base_path).values()]))]
