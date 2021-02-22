from typing import Optional, List, Tuple, Union

from analyze_match_data.gateways.types import ActionType, GoalReason
from analyze_match_data.gateways.frame import Frame
from analyze_match_data.gateways.core import TennisAction, JudgeTennisAction, Position
from .entities import ScorePattern, Player


class MatchInfo:
    def __init__(
        self,
        actions: List[TennisAction],
        judge_actions: List[JudgeTennisAction],
        frames: List[Frame]
    ) -> None:
        self.actions = actions
        self.judge_actions = judge_actions
        self.frames = frames
        self._frames_length = len(frames)

    def get_patterns(self) -> Tuple[List[ScorePattern], List[ScorePattern]]:
        score_patterns: List[ScorePattern] = []
        fail_patterns: List[ScorePattern] = []

        top_player = Player()
        bottom_player = Player()
        prev_action: Optional[
            Union[TennisAction, JudgeTennisAction]
        ] = None
        prev_prev_action: Optional[
            Union[TennisAction, JudgeTennisAction]
        ] = None

        all_actions = sorted(
            [_ for _ in self.actions if _.action_type == ActionType.SetHitPoint] +
            self.judge_actions,
            key=lambda action: action.frame_number
        )

        for action in all_actions:
            if action.action_type == ActionType.NewServe and prev_action is not None and prev_prev_action is not None:
                # extract score pattern
                maybe_target_position = self.get_target_position(
                    prev_action.frame_number,
                    action.goal_frame
                )

                if maybe_target_position is None:
                    prev_action = None
                    prev_prev_action = None
                    top_player.set_position(None)
                    bottom_player.set_position(None)
                    continue

                is_bottom_score = maybe_target_position.y > 0

                top_player_pos = prev_action.pos_history['top'] \
                    if prev_action.pos_history is not None is not None and prev_action.is_bottom_player == is_bottom_score\
                    else prev_prev_action.pos_history['top'] if prev_prev_action.pos_history is not None else None
                bottom_player_pos = prev_action.pos_history['bottom'] \
                    if prev_action.pos_history is not None and prev_action.is_bottom_player == is_bottom_score \
                    else prev_prev_action.pos_history['bottom'] if prev_prev_action.pos_history is not None else None

                if maybe_target_position is not None and \
                        top_player_pos is not None and \
                        bottom_player_pos is not None:
                    pattern = ScorePattern(
                        top_player_pos,
                        bottom_player_pos,
                        maybe_target_position,
                        action.goal_reason,
                        action.shot_type,
                    )
                    score_patterns.append(pattern)

                # reset because new server occured
                prev_action = None
                prev_prev_action = None
                top_player.set_position(None)
                bottom_player.set_position(None)

            if action.action_type == ActionType.SetHitPoint:
                if prev_action is not None:
                    # Extract not score pattern

                    if prev_action.is_bottom_player != action.is_bottom_player:
                        maybe_target_position = self.get_target_position(
                            prev_action.frame_number,
                            action.frame_number
                        )

                        if maybe_target_position is not None and \
                                top_player.position is not None and \
                                bottom_player.position is not None:
                            pattern = ScorePattern(
                                top_player.position,
                                bottom_player.position,
                                maybe_target_position,
                                GoalReason._None,
                                action.shot_type,
                            )
                            fail_patterns.append(pattern)

                # Update bottom player's position
                frame = self.get_frame(action.frame_number)
                if action.is_bottom_player:
                    bottom_player.set_position(
                        frame.ball_frame.position if frame is not None else None
                    )
                else:
                    top_player.set_position(
                        frame.ball_frame.position if frame is not None else None
                    )

                action.set_pos_history({
                    'top': top_player.position,
                    'bottom': bottom_player.position,
                })

                prev_prev_action = prev_action
                prev_action = action

        return (score_patterns, fail_patterns)

    def get_target_position(self, prev_frame_number: int, goal_frame_number: int) -> Optional[Position]:
        for frame_number in range(prev_frame_number, goal_frame_number):
            prev_frame = self.get_frame(frame_number)
            next_frame = self.get_frame(frame_number + 1)

            if prev_frame is not None and next_frame is not None and prev_frame.judge_frame.ball_ground_touch_count == 0 and next_frame.judge_frame.ball_ground_touch_count == 1:
                return prev_frame.ball_frame.position

        return None

    def get_frame(self, frame_number: int) -> Optional[Frame]:
        if frame_number < self._frames_length:
            return self.frames[frame_number]
        else:
            return None
