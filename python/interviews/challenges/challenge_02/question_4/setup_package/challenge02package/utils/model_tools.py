import numpy as np


def get_prediction(model: dict, input_data: np.array) -> np.array:
    """
    Prediction function to for the application, since the other prediction
    :param model:
    :param input_data:
    :return:
    """
    slope = model['slope']
    intercept = model['intercept']
    y_pred = input_data * np.array(slope) + np.array(intercept)
    results_dict = {}
    if isinstance(input_data, list):
        for _idx, _i in enumerate(input_data):
            results_dict[f'{_i}'] = y_pred[_idx]
    else:
        results_dict[f'{input_data}'] = y_pred

    return results_dict
