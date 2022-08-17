import datetime

import dateutil
from lightgbm import LGBMRegressor
import lightgbm as lgb
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def plot_predictions(input_data: pd.DataFrame, category: str, y_test=pd.DataFrame, mae=None):
    input_series = input_data.loc[:, 'target']
    # plot reality vs prediction for the last week of the dataset
    fig = plt.figure(figsize=(16, 8))
    labels = ['Prediction']

    if not y_test.empty:
        plt.plot(y_test, color='red')
        labels.append('Real')
        title = f'{category} - Real vs Prediction - MAE {mae}'
    else:
        title = f'{category} - Prediction'

    plt.title(title, fontsize=20)
    plt.plot(input_series, color='green')
    plt.xlabel('Timestamp')
    plt.ylabel('Sales')
    plt.legend(labels=labels)
    plt.grid()
    plt.show()


class ChallengeModelling():
    def __init__(self, category='Tap'):
        self.mae_path = f'./artifacts/{category}_error_mae.txt'
        self.model_path = f'./artifacts/{category}_model.txt'
        self.category = category
        self.results_path = f'./data/results/{self.category}_prediction_result.csv'

    def train_time_series_with_folds(self, df, horizon=12, plot_features=False, plot_prediction=False):
        # create 1 week lag variable by shifting the target value for 1 week

        # drop NaNs after feature engineering
        df.dropna(how='any', axis=0, inplace=True)

        X = df.drop(self.category, axis=1)
        y = df[self.category]

        # take last week of the dataset for validation
        X_train, X_test = X.iloc[:-horizon, :], X.iloc[-horizon:, :]
        y_train, y_test = y.iloc[:-horizon], y.iloc[-horizon:]
        # X_train, X_test = X.iloc[:, :], X.iloc[:, :]
        # y_train, y_test = y.iloc[:], y.iloc[:]

        # create, train and do inference of the model
        model = LGBMRegressor(random_state=42)
        model.fit(X_train, y_train)

        if plot_features:
            # create a dataframe with the variable importances of the model
            df_importances = pd.DataFrame({
                'feature': model.feature_name_,
                'importance': model.feature_importances_
            }).sort_values(by='importance', ascending=False)

            # plot variable importances of the model
            plt.title(f'{self.category} - Variable Importances', fontsize=16)
            sns.barplot(x=df_importances.importance, y=df_importances.feature, orient='h')

        model.booster_.save_model(self.model_path)
        predictions = self.do_prediction(X_test)
        # predictions = model.predict(X_test)
        mae = np.round(mean_absolute_error(y_test, predictions['target']), 3)
        with open(self.mae_path, 'w') as _f:
            _f.write(str(mae))
        if plot_prediction:
            plot_predictions(input_data=predictions, category=self.category, y_test=y_test, mae=mae)
        if plot_features:
            plt.show()

    def do_prediction(self, input_data: pd.DataFrame, plot_prediction=False):
        model = lgb.Booster(model_file=self.model_path)
        predictions = model.predict(input_data)
        predictions = pd.DataFrame(predictions, index=input_data.index)
        predictions = predictions.rename({0: 'target'}, axis=1)
        predictions.to_csv(self.results_path)
        if plot_prediction:
            plot_predictions(input_data=predictions, category=self.category)
        return predictions

    def generate_data(self, start_date_str: str, input_raw: pd.DataFrame):

        start_date_dt = datetime.datetime.strptime(start_date_str, '%Y%m')
        dates_ls = []
        for _i in range(0, 12):
            new_date = start_date_dt + dateutil.relativedelta.relativedelta(months=_i)
            dates_ls.append(new_date)
        dates_dict = {'yearmonth': dates_ls}
        new_data = pd.DataFrame(dates_dict)
        combined_data = pd.concat([input_raw, new_data])

        return combined_data
