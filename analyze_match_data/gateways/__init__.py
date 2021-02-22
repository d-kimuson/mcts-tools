from typing import Tuple, List

from .types import JsonDict
from .core import TennisAction, JudgeTennisAction
from .frame import Frame


def load_json(_json: JsonDict) -> Tuple[List[TennisAction], List[JudgeTennisAction], List[Frame]]:
    return (
        [
            TennisAction.from_json_dict(action_json) for action_json in _json["TennisActions"]
        ],
        [
            JudgeTennisAction.from_json_dict(action_json) for action_json in _json["JudgeTennisActions"]
        ],
        [
            Frame.from_json_dict(frame_json) for frame_json in _json["Frames"]
        ]
    )
