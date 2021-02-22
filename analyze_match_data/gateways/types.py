from enum import Enum
from typing import Dict, Any

JsonDict = Dict[str, Any]


class ActionType(Enum):
    SetMovePoint = 0
    SetHitPoint = 1
    SetServeHitPoint = 2
    DoNothing = 3
    ActionNotFound = 4
    ForceTransitionToEnd = 5
    NewServe = 6
    _None = 7
    ActivatePowerShot = 8
    AssistantHint = 9
    Touch = 10
    ServeToss = 11


class ShotType(Enum):
    _None = 0
    TopSpin = 1
    Slice = 2
    Serve = 3
    Lob = 4
    Drop = 5
    Smash = 6
    Volley = 7
    Difficult = 8
    Undefined = 9
    QuickVolley = 10
    DifficultStretchVolley = 11

    def __int__(self) -> int:
        return self.value

    def __float__(self) -> float:
        return float(self.value)


def str_to_shot_type(_str: str) -> ShotType:
    if '_None' in _str:
        return ShotType(0)
    if 'ShotType.TopSpin' == _str:
        return ShotType(1)
    if 'ShotType.Slice' == _str:
        return ShotType(2)
    if 'ShotType.Serve' == _str:
        return ShotType(3)
    if 'ShotType.Lob' == _str:
        return ShotType(4)
    if 'ShotType.Drop' == _str:
        return ShotType(5)
    if 'ShotType.Smash' == _str:
        return ShotType(6)
    if 'ShotType.Volley' == _str:
        return ShotType(7)
    if 'ShotType.Difficult' == _str:
        return ShotType(8)
    if 'ShotType.Undefined' == _str:
        return ShotType(9)
    if 'ShotType.QuickVolley' == _str:
        return ShotType(10)
    if 'ShotType.DifficultStretchVolley' == _str:
        return ShotType(11)

    raise RuntimeError('Unsupported Shot Type')


class GoalReason(Enum):
    Common = 0
    BounceOutOfCourt = 1
    NetShot = 2
    SecondBounceOnCourt = 3
    BounceOutOfServeArea = 4
    BounceOnOwnCourtSide = 5
    _None = 6
    MissingShootPoint = 7
    SecondBounceOutOfCourt = 8
    BallOutOfGameArea = 9


def str_to_goal_reason(_str: str) -> GoalReason:
    if 'GoalReason.Common' == _str:
        return GoalReason(0)
    if 'GoalReason.BounceOutOfCourt' == _str:
        return GoalReason(1)
    if 'GoalReason.NetShot' == _str:
        return GoalReason(2)
    if 'GoalReason.SecondBounceOnCourt' == _str:
        return GoalReason(3)
    if 'GoalReason.BounceOutOfServeArea' == _str:
        return GoalReason(4)
    if 'GoalReason.BounceOnOwnCourtSide' == _str:
        return GoalReason(5)
    if 'GoalReason._None' == _str:
        return GoalReason(6)
    if 'GoalReason.MissingShootPoint' == _str:
        return GoalReason(7)
    if 'GoalReason.SecondBounceOutOfCourt' == _str:
        return GoalReason(8)
    if 'GoalReason.BallOutOfGameArea' == _str:
        return GoalReason(9)

    raise RuntimeError('GoalReason')


class MatchType(Enum):
    League = 0
    Training = 1
    Free = 2
    Server = 3
    Replay = 4
    Friendly = 5
    Tutorial = 6
    Developer = 7
    _None = 8
    Quick = 9
