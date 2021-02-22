from typing import List

from .core import Position
from .types import JsonDict, MatchType


class JudgeFrame:
    def __init__(
        self,
        match_type: MatchType,
        tie_break_phase: int,
        ball_ground_touch_count: int,
        serve_side: int,
        last_hit_side: int,
        is_serving: bool,
        is_second_serve_now: bool,
    ) -> None:
        self.match_type = match_type
        self.tie_break_phase = tie_break_phase
        self.ball_ground_touch_count = ball_ground_touch_count
        self.serve_side = serve_side
        self.last_hit_side = last_hit_side
        self.is_serving = is_serving
        self.is_second_serve_now = is_second_serve_now

    @classmethod
    def from_json_dict(cls, _json: JsonDict) -> 'JudgeFrame':
        return cls(
            MatchType(_json["MatchType"]),
            _json["TieBreakPhase"],
            _json["BallGroundTouchCount"],
            _json["ServeSide"],
            _json["LastHitSide"],
            _json["IsServing"],
            _json["IsSecondServeNow"],
        )


class BallFrame:
    def __init__(
            self,
            position: Position,
            is_ball_out_of_bounds: bool
    ) -> None:
        self.position = position
        self.is_ball_out_of_bounds: bool = is_ball_out_of_bounds

    @classmethod
    def from_json_dict(cls, _json: JsonDict) -> 'BallFrame':
        return cls(
            Position.from_json_dict(_json["Position"]),
            _json["IsBallOutOfBounds"],
        )


class Frame:
    def __init__(
        self,
        _time: float,
        judge_frame: JudgeFrame,
        ball_frame: BallFrame
    ) -> None:
        self.time: float = _time
        self.judge_frame = judge_frame
        self.ball_frame = ball_frame

    @classmethod
    def from_json_dict(cls, _json: JsonDict) -> 'Frame':
        return cls(
            _json["Time"],
            JudgeFrame.from_json_dict(_json["JudgeF"]),
            BallFrame.from_json_dict(_json["BallF"])
        )
