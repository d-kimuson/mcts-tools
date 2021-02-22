from math import sqrt
from typing import Dict, Optional, Union

from .types import ShotType, ActionType, JsonDict, GoalReason

# same as implementation of mcts ai
XCoatSepNum = 6
YCoatSepNum = 4
XUnitLength = 8.0 / XCoatSepNum
YUnitLength = 24.0 / (YCoatSepNum * 2)
AgentPosMin = XCoatSepNum * YCoatSepNum
AgentPosMax = XCoatSepNum * YCoatSepNum * 2 - 1
OpponentPosMin = 0
OpponentPosMax = XCoatSepNum * YCoatSepNum - 1
maxPosNum = XCoatSepNum * YCoatSepNum * 2


class Position:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_json_dict(cls, _json: JsonDict) -> 'Position':
        return cls(
            _json["x"],
            _json["z"],
            _json["y"]
        )

    def distance(self, target: 'Position') -> float:
        x_diff = self.x - target.x
        y_diff = self.y - target.y

        return sqrt(x_diff ** 2 + y_diff ** 2)

    def generate_reversed(self) -> 'Position':
        return Position(
            -1 * self.x,
            -1 * self.y,
            self.z
        )

    @property
    def as_int(self) -> int:
        x = self.x + 4.0
        y = self.y + 12.0

        x_num = (x // XUnitLength if x <
                 8.0 else XCoatSepNum - 1) if x > 0.0 else 0
        y_num = (y // YUnitLength if y <
                 24.0 else YCoatSepNum * 2 - 1) if y > 0.0 else 0

        return int(x_num + XCoatSepNum * y_num)

    @property
    def as_dict(self) -> Dict[str, float]:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def __str__(self) -> str:
        return "Position<{:.2f}, {:.2f}, {:.2f}>".format(self.x, self.y, self.z)

    __repr__ = __str__


class TennisAction:
    def __init__(
        self,
        action_type: ActionType,
        position: Position,
        frame_number: int,
        is_bottom_player: bool,
        shot_type: ShotType
    ) -> None:
        self.action_type = action_type
        self.position = position
        self.frame_number = frame_number
        self.is_bottom_player = is_bottom_player
        self.shot_type = shot_type

        self.pos_history: Optional[Dict[str, Union[Position, None]]] = None

    @classmethod
    def from_json_dict(cls, _json: JsonDict) -> 'TennisAction':
        return cls(
            ActionType(_json["ActionType"]),
            Position.from_json_dict(_json["Position"]),
            _json["FrameNumber"],
            _json["IsBottomPlayer"],
            ShotType(_json["ShotType"]),
        )

    def set_pos_history(self, pos_history: Dict[str, Union[Position, None]]) -> None:
        self.pos_history = pos_history

    def __str__(self) -> str:
        return "TennisAction<frame: {}, action_type: {}, bottom?: {}>".format(self.frame_number, self.action_type, self.is_bottom_player)

    __repr__ = __str__


class JudgeTennisAction:
    def __init__(
        self,
        action_type: ActionType,
        position: Position,
        frame_number: int,
        is_bottom_player: bool,
        shot_type: ShotType,
        goal_reason: GoalReason,
        goal_frame: int,
    ) -> None:
        self.action_type = action_type
        self.position = position
        self.frame_number = frame_number
        self.is_bottom_player = is_bottom_player
        self.shot_type = shot_type
        self.goal_reason = goal_reason
        self.goal_frame = goal_frame

        self.pos_history: Optional[Dict[str, Union[Position, None]]] = None

    @classmethod
    def from_json_dict(cls, _json: JsonDict) -> 'JudgeTennisAction':
        return cls(
            ActionType(_json["ActionType"]),
            Position.from_json_dict(_json["Position"]),
            _json["FrameNumber"],
            _json["IsBottomPlayer"],
            ShotType(_json["ShotType"]),
            GoalReason(_json["GoalReason"]),
            _json["GoalFrame"],
        )

    def set_pos_history(self, pos_history: Dict[str, Union[Position, None]]) -> None:
        self.pos_history = pos_history

    def __str__(self) -> str:
        return "JudgeTennisAction<frame: {}, action_type: {}, bottom?: {}>".format(self.frame_number, self.action_type, self.is_bottom_player)

    __repr__ = __str__
