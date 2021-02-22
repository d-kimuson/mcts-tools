import codecs
import json
from typing import List, Dict, Union

from config.paths import RECORD_DIR, DIST_DIR, SHOT_PATTERNS_PATH
from analyze_match_data.gateways import load_json
from analyze_match_data.usecase.core import MatchInfo
from analyze_match_data.usecase.entities import ScorePattern


def write_result(result: Dict[str, Dict[str, Union[int, str]]], count: int) -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    with open(str(SHOT_PATTERNS_PATH), 'w+') as f:
        f.write(json.dumps(result, indent=2))

    print('{} file has complited'.format(count))


def extract_patterns(length: int = -1) -> None:
    paths = [str(path) for path in RECORD_DIR.glob('*_League.json')]
    score_patterns: List[ScorePattern] = []
    fail_patterns: List[ScorePattern] = []

    count = 0

    for path in paths[:length]:
        count += 1
        # Read Record File
        f = codecs.open(path, 'r', 'utf-8-sig')
        json_data = json.loads(f.read())
        f.close()

        # Load Match Info
        actions, judge_actions, frames = load_json(json_data)
        match_info = MatchInfo(actions, judge_actions, frames)

        # Extrach & Join
        _score_patterns, _fail_patterns = match_info.get_patterns()
        score_patterns += [
            pattern for pattern in _score_patterns if pattern.is_valid
        ]
        fail_patterns += [
            pattern for pattern in _fail_patterns if pattern.is_valid
        ]

        score_keys = [pattern.pattern_str for pattern in score_patterns]
        fail_keys = [pattern.pattern_str for pattern in fail_patterns]

        result: Dict[str, Dict[str, Union[int, str]]] = {}

        for pattern in score_keys + fail_keys:
            score_count = score_keys.count(pattern)
            fail_count = fail_keys.count(pattern)

            result_item: Dict[str, Union[int, str]] = {
                'score_count': score_count,
                'fail_count': fail_count,
                'rate': '{:.1f}%'.format(100 * score_count / (score_count + fail_count))
            }

            if pattern not in result.keys():
                result[pattern] = result_item

        if count % 20 == 0:
            write_result(result, count)

    write_result(result, count)
    print('completed all files')
