# import json
# import codecs
# from typing import Dict, List, Any
# from statistics import mean, median
# from math import exp

# from analyze_match_data.gateways.types import JsonDict, str_to_shot_type, str_to_goal_reason, GoalReason


# def transform_to_df(_json: JsonDict, is_score: bool, length: int = 0) -> pd.DataFrame:
#     shot_types = []
#     perpendicular_line_distances = []
#     distance_target_points = []
#     distance_2_bound_points = []

#     for pattern in _json[:length]:
#         # for pattern in _json:
#         shot_types.append(str_to_shot_type(pattern["shot_type"]))
#         perpendicular_line_distances.append(
#             pattern["perpendicular_line_distance"])
#         distance_target_points.append(pattern["distance_target_point"])
#         distance_2_bound_points.append(pattern["distance_2_bound_point"])

#     return pd.DataFrame({
#         # 'shot_type': shot_types,
#         'perpendicular_line_distances': perpendicular_line_distances,
#         'distance_target_points': distance_target_points,
#         'distance_2_bound_points': distance_2_bound_points,
#         'is_score': is_score  # 目的変数
#     })


# def transform_to_dict(_json: JsonDict) -> List[Dict[str, Any]]:
#     return [{
#         'shot_type': str_to_shot_type(pattern['shot_type']),
#         'goal_reason': str_to_goal_reason(pattern['goal_reason']),
#         'perpendicular_line_distance': pattern['perpendicular_line_distance'],
#         'distance_target_point': pattern['distance_target_point'],
#         'distance_2_bound_point': pattern['distance_2_bound_point']
#     } for pattern in _json]


# def logistic(score_path: str, fail_path: str):
#     score_json_dict, fail_json_dict = load_data(score_path, fail_path)
#     length = min(len(score_json_dict), len(fail_json_dict))

#     score_df = transform_to_df(score_json_dict, True, length)
#     fail_df = transform_to_df(fail_json_dict, False, length)

#     df = pd.concat([score_df, fail_df])
#     X = df.drop("is_score", axis=1)
#     Y = df["is_score"]

#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.4)

#     model = LogisticRegression()
#     model.fit(X_train, Y_train)

#     print(f"正答率: {model.score(X_test, Y_test) * 100:.1f} %")
#     print(model.coef_)
#     print(model.get_params())

#     print('SCORE: ', model.score(score_df.drop(
#         "is_score", axis=1), score_df["is_score"]))
#     print('FAIL : ', model.score(fail_df.drop(
#         "is_score", axis=1), fail_df["is_score"]))

#     print(model.sparsify())


# def load_data(score_path: str, fail_path: str):
#     with open(score_path, 'r') as f:
#         score_json_dict = json.loads(f.read())

#     with open(fail_path, 'r') as f:
#         fail_json_dict = json.loads(f.read())
#     print("Finish load data")

#     return score_json_dict, fail_json_dict


# def lenear(score_path: str, fail_path: str):
#     score_json_dict, fail_json_dict = load_data(score_path, fail_path)

#     score_df = transform_to_df(score_json_dict, 1)
#     fail_df = transform_to_df(fail_json_dict, 0)

#     df = pd.concat([score_df, fail_df])
#     X = df.drop("is_score", axis=1)
#     Y = df["is_score"]

#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.4)

#     model = LinearRegression()
#     model.fit(X_train, Y_train)

#     print(f"正答率: {model.score(X_test, Y_test) * 100:.1f} %")
#     print(model.coef_)

#     print(model.predict(X_train))


# def ana():
#     score_json_dict, fail_json_dict = load_data(score_path, fail_path)
#     length = min(len(score_json_dict), len(fail_json_dict))
#     patterns = transform_to_dict(score_json_dict)

#     filterd = [pattern for pattern in patterns if pattern['goal_reason']
#                == GoalReason.SecondBounceOnCourt]

#     print(
#         mean([_['distance_target_point'] for _ in filterd]),
#         median([_['distance_target_point'] for _ in filterd])
#     )

#     print(
#         mean([_['perpendicular_line_distance'] for _ in filterd]),
#         median([_['perpendicular_line_distance'] for _ in filterd])
#     )

#     filterd = [pattern for pattern in patterns if pattern['goal_reason']
#                == GoalReason.SecondBounceOutOfCourt]

#     print(
#         mean([_['distance_target_point'] for _ in filterd]),
#         median([_['distance_target_point'] for _ in filterd])
#     )

#     print(
#         mean([_['perpendicular_line_distance'] for _ in filterd]),
#         median([_['perpendicular_line_distance'] for _ in filterd])
#     )


# def predict_score(score_path, fail_path):
#     score_json_dict, fail_json_dict = load_data(score_path, fail_path)

#     count = len(score_json_dict)
#     success_count = len([data for data in score_json_dict if predict([-0.02453905, -0.2333926,  0.0380362],
#                                                                      [data['perpendicular_line_distance'], data['distance_target_point'], data['distance_2_bound_point']])])

#     print(success_count / count)


# def predict(params, data):
#     p = 1 / (1 + exp(-1 * (
#         1.0 + params[0] * data[0] + params[1] + data[1] + params[2] + data[2]
#     )))
#     print(p)
#     return p > 0.5
