import matplotlib.pyplot as plt
import pandas as pd
import requests
import numpy as np
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

pd.options.mode.chained_assignment = None  # default='warn'


def decompose_item_demand(df, share_type='Tap', samples=(96, 'all'), period=48):
    if samples == 'all':
        # decomposing all time series timestamps
        res = seasonal_decompose(df[share_type].values, period=period)
    else:
        # decomposing a sample of the time series
        res = seasonal_decompose(df[share_type].values[-samples:], period=period)

    observed = res.observed
    trend = res.trend
    seasonal = res.seasonal
    residual = res.resid

    # plot the complete time series
    fig, axs = plt.subplots(4, figsize=(16, 8))
    axs[0].set_title('OBSERVED', fontsize=16)
    axs[0].plot(observed)
    axs[0].grid()

    # plot the trend of the time series
    axs[1].set_title('TREND', fontsize=16)
    axs[1].plot(trend)
    axs[1].grid()

    # plot the seasonality of the time series. Period=24 daily seasonality | Period=24*7 weekly seasonality.
    axs[2].set_title('SEASONALITY', fontsize=16)
    axs[2].plot(seasonal)
    axs[2].grid()

    # plot the noise of the time series
    axs[3].set_title('NOISE', fontsize=16)
    axs[3].plot(residual)
    axs[3].scatter(y=residual, x=range(len(residual)), alpha=0.5)
    axs[3].grid()

    plt.show()


# seasons
def season_calc(df):
    if df['month'] in [12, 1, 2]:
        return 1  # 'summer'
    elif df['month'] in [3, 4, 5]:
        return 2  # 'autumn'
    elif df['month'] in [6, 7, 8]:
        return 3  # 'winter'
    elif df['month'] in [9, 10, 11]:
        return 4  # 'spring'


def analysis(input_data: pd.DataFrame,
             category: str,
             plot_raw=False,
             plot_month_mean=False,
             plot_month_box=False,
             plot_seasonality=False,
             plot_auroregressive=False,
             plot_auroregressive_partial=False
             ):
    # plt.style.use("dark_background")\
    plt.style.use('ggplot')
    # raw plot
    if plot_raw:
        input_data[['Tap', 'Pack']].plot()
        plt.title('Tap and Pack Sales')

    if plot_month_mean:
        feat_month_tap = input_data[['month', 'Tap']].groupby('month').mean()
        feat_month_pack = input_data[['month', 'Pack']].groupby('month').mean()
        feat_month_tap.plot()
        feat_month_pack.plot()

    ## boxplot
    if plot_month_box:
        # https://stackoverflow.com/questions/64713964/converting-repeating-rows-to-columns-in-pandas-dataframe
        # box_pd = input_data.pivot(index=None, columns='month', values='Tap').apply(lambda x: pd.Series(x.dropna().to_numpy()))
        input_data[['Tap', 'Pack', 'month']].boxplot(by='month')
        plt.title('Tap and Pack Boxplot')

    # seasonality
    if plot_seasonality:
        decompose_item_demand(df=input_data, share_type='Tap', samples=96, period=48)
        input_data[['Tap', 'Pack', 'season']].boxplot(by='season')
        plt.title('Tap and Pack Seasonality')

    # auroregressive
    if plot_auroregressive:
        plot_acf(input_data['Pack'].values)  # , lags=24)
        plt.title(f'{category} - Autocorrelation')

    if plot_auroregressive_partial:
        plot_pacf(input_data['Pack'].values)  # , lags=12)
        plt.title(f'{category} -  Partial Autocorrelation')

    if plot_raw or plot_month_mean or plot_month_box or plot_seasonality or plot_auroregressive or plot_auroregressive_partial:
        plt.xlabel('Timestamp')
        plt.ylabel('Sales')
        plt.show()
    # quick analysis of data
    print(input_data.info())
    print(input_data.describe())
    print(input_data.describe().T)


class CommonTools():
    def __init__(self, category='Tap'):
        self.category = category

    def read_data(self, plot_data=False):
        raw_pd = pd.read_excel('./data/raw/AA_casestudy_NSW_volume.xlsx', sheet_name='in', header=2)
        raw_pd = raw_pd[raw_pd['yearmonth'] != 'Grand Total']
        raw_pd['yearmonth'] = pd.to_datetime(raw_pd['yearmonth'], format='%Y%m')
        raw_pd = raw_pd.sort_values('yearmonth')

        if plot_data:
            raw_pd.set_index('yearmonth').plot()
            plt.show()

        return raw_pd

    def get_holidays(self):
        resource_ids = [
            '33673aca-0857-42e5-b8f0-9981b4755686',
            'c4163dc4-4f5a-4cae-b787-43ef0fcf8d8b',
            'bda4d4f2-7fde-4bfc-8a23-a6eefc8cef80',
            '253d63c0-af1f-4f4c-b8d5-eb9d9b1d46ab',
            'a24ecaf2-044a-4e66-989c-eacc81ded62f',
            '13ca6df3-f6c9-42a1-bb20-6e2c12fe9d94',
            '56a5ee91-8e94-416e-81f7-3fe626958f7e',
            '768053da-b12b-4196-8fef-9262829998f3',
        ]
        url = 'https://data.gov.au/data/api/3/action/datastore_search?resource_id=768053da-b12b-4196-8fef-9262829998f3'
        # fileobj = urllib.urlopen(url)
        req = requests.get(url)

    def feature_engineering(self, got_raw_pd: pd.DataFrame, new_flag=False):
        if not new_flag:
            # TODO: intead of removing covid period, filter outliers with means
            got_raw_pd = got_raw_pd[
                (got_raw_pd['yearmonth'] < '2020-01-01')
            ]
        got_raw_pd['month'] = got_raw_pd.loc[:, 'yearmonth'].dt.month.copy()
        got_raw_pd.loc[:, 'month'] = got_raw_pd.loc[:, 'month'].astype(int).copy()
        got_raw_pd['season'] = got_raw_pd.apply(season_calc, axis=1)
        # TODO: add holidays feature
        # self.get_holidays()
        # TODO: add linear regression line for trend weighting

        got_raw_pd['prev_month'] = got_raw_pd[self.category].shift(12)
        got_raw_pd = got_raw_pd.set_index('yearmonth')

        return got_raw_pd

    def do_reporting(self, input_data: pd.DataFrame, tap_result: str, pack_result: str):
        category = 'Tap'
        tap_pd = pd.read_csv(tap_result)
        tap_pd = tap_pd.rename({'target': category}, axis=1)
        with open(f'./artifacts/{category}_error_mae.txt', 'r') as _f:
            mae = _f.read()
        tap_pd[f'{category}_upper_limit'] = tap_pd[category] + float(mae)
        tap_pd[f'{category}_lower_limit'] = tap_pd[category] - float(mae)
        tap_pd['yearmonth'] = pd.to_datetime(tap_pd['yearmonth'], format='%Y-%m-%d')
        tap_pd = tap_pd.set_index('yearmonth')

        category = 'Pack'
        pack_pd = pd.read_csv(pack_result)
        pack_pd = pack_pd.rename({'target': category}, axis=1)
        with open(f'./artifacts/{category}_error_mae.txt', 'r') as _f:
            mae = _f.read()
        pack_pd[f'{category}_upper_limit'] = pack_pd[category] + float(mae)
        pack_pd[f'{category}_lower_limit'] = pack_pd[category] - float(mae)
        pack_pd['yearmonth'] = pd.to_datetime(pack_pd['yearmonth'], format='%Y-%m-%d')
        pack_pd = pack_pd.set_index('yearmonth')

        combine_result = tap_pd.join(pack_pd, how='left')
        combine_result['yearmonth'] = combine_result.index
        report_pd = pd.concat([input_data, combine_result], ignore_index=True)
        report_pd = report_pd.set_index('yearmonth')
        return report_pd

    def special_plot(self, input_data: pd.DataFrame, plot_data=False):
        input_data = input_data.loc['2018-01-01':, :]

        # plt.style.use("dark_background")
        plt.style.use('ggplot')
        fig, ax = plt.subplots()
        clrs = sns.color_palette("husl", 5)
        x = np.array(input_data.index)[:]  # np.array(input_data.loc[:,'yearmonth'].values[-12:], dtype=np.float64)
        y0 = np.array(input_data.loc[:, self.category].values, dtype=np.float64)
        y1 = np.array(input_data.loc[:, f'{self.category}_lower_limit'].values, dtype=np.float64)
        y2 = np.array(input_data.loc[:, f'{self.category}_upper_limit'].values, dtype=np.float64)

        plt.fill_between(x, y1, y2, alpha=.5, linewidth=0)
        if plot_data:
            ax.plot(x, y0, linewidth=2)
            plt.title(f'{self.category} Forecasting')
            plt.ylabel('Sales')
            plt.ylabel('Timestamp')
            # plt.legend()
            plt.show()
