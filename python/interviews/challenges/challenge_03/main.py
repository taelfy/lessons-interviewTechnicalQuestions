import pandas as pd

import utils.challenge_tools as ct
import utils.challenge_model as cm

if __name__ == '__main__':
    model_cat = 'Tap'

    if model_cat == 'Tap':
        drop_col = 'Pack'
    else:
        drop_col = 'Tap'

    # DATA ENGINEERING
    tools = ct.CommonTools(category=model_cat)
    raw_pd = tools.read_data(plot_data=False)

    got_feature_pd = tools.feature_engineering(got_raw_pd=raw_pd)
    # plot the analysis data
    ct.analysis(input_data=got_feature_pd,
                category=model_cat,
                # plot_raw=True,
                # plot_month_mean=True,
                # plot_month_box=True,
                # plot_seasonality=True,
                # plot_auroregressive=True,
                # plot_auroregressive_partial=True
                )

    # MODELLING
    modelling = cm.ChallengeModelling(category=model_cat)
    got_feature_pd = got_feature_pd.drop(drop_col, axis=1)
    modelling.train_time_series_with_folds(
        got_feature_pd,
        horizon=12,
        # plot_features=True,
        # plot_prediction=True
    )

    start_date_str = '202201'
    new_data = modelling.generate_data(start_date_str=start_date_str, input_raw=raw_pd)
    got_new_pd = tools.feature_engineering(got_raw_pd=new_data, new_flag=True)
    got_new_pd = got_new_pd.loc['2022-01-01':, :].drop(['Tap', 'Pack'], axis=1)
    predictions = modelling.do_prediction(got_new_pd,
                                          # plot_prediction=True
                                          )

    # REPORTING
    tap_result = f'./data/results/Tap_prediction_result.csv'
    pack_result = f'./data/results/Pack_prediction_result.csv'
    report_pd = tools.do_reporting(input_data=raw_pd, tap_result=tap_result, pack_result=pack_result)

    # SPECIAL PLOTTING
    tools.special_plot(
        input_data=report_pd,
        plot_data=True
    )
