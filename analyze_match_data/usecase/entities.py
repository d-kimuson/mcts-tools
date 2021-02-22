from typing import Optional

from analyze_match_data.gateways.types import JsonDict, GoalReason, ShotType
from analyze_match_data.gateways.core import Position


class Player:
    def __init__(self) -> None:
        self.position: Optional[Position] = None

    def set_position(self, position: Optional[Position]) -> None:
        self.position = position


class ScorePattern:
    def __init__(
        self,
        winner_position: Position,
        loser_position: Position,
        target_position: Position,
        goal_reason: GoalReason,
        shot_type: ShotType
    ) -> None:
        # as top player
        if winner_position.y > 0.0:
            self.winner_position = winner_position.generate_reversed()
            self.loser_position = loser_position.generate_reversed()
            self.target_position = target_position.generate_reversed()
        else:
            self.winner_position = winner_position.generate_reversed()
            self.loser_position = loser_position.generate_reversed()
            self.target_position = target_position.generate_reversed()

        self.goal_reason = goal_reason
        self.shot_type = shot_type

    @property
    def is_valid(self) -> bool:
        return self.winner_position is not None and \
            self.loser_position is not None and \
            self.winner_position.y * self.loser_position.y < 0 and \
            self.loser_position.y * self.target_position.y > 0

    @property
    def as_dict(self) -> JsonDict:
        return {
            "winner_position": self.winner_position.as_dict,
            "loser_position": self.loser_position.as_dict,
            "target_position": self.target_position.as_dict,
            "pattern": self.pattern_str,
            "goal_reason": str(self.goal_reason),
            "shot_type": str(self.shot_type),
        }

    @property
    def pattern_str(self) -> str:
        return f"{self.winner_position.as_int},{self.loser_position.as_int},{self.target_position.as_int},{str(self.shot_type)}"
