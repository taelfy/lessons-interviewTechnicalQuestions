import decimal
import http.client
import json
import pandas as pd
from decimal import Decimal


def get_request(uri, req_method='GET'):
    url_api = 'api.binance.com'
    conn = http.client.HTTPSConnection(url_api)
    conn.request(req_method, uri)
    resp = conn.getresponse()
    status = resp.status
    if status != 200:
        raise Exception(f"Error getting request. Status: {status}")
    text = resp.read().decode()
    resp_j = json.loads(text)
    return resp_j


def get_spread(x)-> decimal.Decimal:
    spread = Decimal(x['askPrice']) - Decimal(x['bidPrice'])
    return Decimal(spread)


def print_top_5_field(symbol: str, field: str, symbol_pd: pd.DataFrame):
    if symbol == 'BTC':
        print('Question 1: Print the top 5 symbols with quote asset BTC and the highest volume over the last 24 hours in descending order.')
    elif symbol == 'USDT':
        print('Question 2: Print the top 5 symbols with quote asset USDT and the highest number of trades over the last 24 hours in descending order.')
    else:
        raise Exception(f"Error: Symbol not part of technical challenge. Symbol: {symbol}")

    for _row in symbol_pd.iterrows():
        symbol = _row[1]['symbol']
        field_val = _row[1][field]
        print(f'Symbol: {symbol}, {field}: {field_val}')


def get_ticker_fields(symbol: str, field: str, print_fields=False, limit=None) -> pd.DataFrame:
    uri = '/api/v3/exchangeInfo'
    symbols_all_j = get_request(uri)
    symbols_ls = [_i['symbol'] for _i in symbols_all_j['symbols'] if _i['quoteAsset'] == symbol]

    uri = '/api/v3/ticker/24hr'
    symbols_info_j = get_request(uri)
    symbol_info_ls = [_i for _i in symbols_info_j if _i['symbol'] in symbols_ls]
    symbol_pd = pd.DataFrame(symbol_info_ls)
    symbol_pd[field] = symbol_pd[field].astype(float)
    symbol_pd = symbol_pd.sort_values(field, ascending=False)
    symbol_pd_top_5 = symbol_pd.iloc[:limit, :]
    if print_fields:
        print_top_5_field(symbol, field, symbol_pd_top_5)
    return symbol_pd_top_5


def print_notional_values(symbol_pd: pd.DataFrame()):
    print("Question 3: Using the symbols from Q1, what is the total notional value of the top 200 bids and asks currently on each order book?")
    for _row in symbol_pd.iterrows():
        uri = f'/api/v3/depth?symbol={_row[1]["symbol"]}&limit=200'
        symbol_depth = get_request(uri)
        for _i in ['bids', 'asks']:
            sym_depth_pd = pd.DataFrame(data=symbol_depth[_i], columns=[f"{_i}_price", f"{_i}_qty"], dtype=float)
            sym_depth_pd[f'{_i}_notional_value'] = sym_depth_pd[f'{_i}_price'] * sym_depth_pd[f'{_i}_qty']
            bids_notional_val = sym_depth_pd[f'{_i}_notional_value'].sum()
            print(f'Symbol: {_row[1]["symbol"]}, {_i} total notional value: {bids_notional_val}')


def update_prom_gauge(prom_gauge, abs_delta):
    print("Question 6: Make the output of Q5 accessible by querying http://localhost:8080/metrics using the Prometheus Metrics format.")
    for _row in abs_delta.iterrows():
        format_val = "{:.{prec}f}".format(_row[1]["spread_delta"], prec=abs(Decimal(_row[1]["spread_delta"]).as_tuple().exponent))
        prom_gauge.labels(_row[0]).set(format_val)


class BinanceClass:
    def __init__(self, url: str):
        self.url = url
        self.saved_delta_pd = pd.DataFrame({})

    def print_price_spread(self, symbol_pd: pd.DataFrame()):
        print("Question 4: What is the price spread for each of the symbols from Q2?")
        symbol_pd['spread'] = symbol_pd.apply(lambda x: get_spread(x), axis=1)
        self.saved_delta_pd = symbol_pd
        for _row in symbol_pd.iterrows():
            print(f'Symbol: {_row[1]["symbol"]}, Price Spread: {"{:.{prec}f}".format(_row[1]["spread"], prec=abs(Decimal(_row[1]["spread"]).as_tuple().exponent))}')

    def print_abs_delta(self) -> pd.DataFrame:
        print("Question 5: Every 10 seconds print the result of Q4 and the absolute delta from the previous value for each symbol.")
        got_fields = get_ticker_fields('USDT', 'count', limit=None)
        self.saved_delta_pd = self.saved_delta_pd.set_index('symbol')
        got_fields['spread'] = got_fields.apply(lambda x: get_spread(x), axis=1)
        got_fields_idx = got_fields.set_index('symbol')
        got_fields_idx['spread_delta'] = abs(self.saved_delta_pd['spread'] - got_fields_idx['spread'])
        got_fields_idx = got_fields_idx.dropna(subset='spread_delta')
        for _row in got_fields_idx.iterrows():
            format_val = "{:.{prec}f}".format(_row[1]["spread_delta"], prec=abs(Decimal(_row[1]["spread_delta"]).as_tuple().exponent))
            print(f'Symbol: {_row[0]}, Abs Price Spread Diff: {format_val}')
        # save this for the next iteration
        self.saved_delta_pd = got_fields.iloc[:5, :]
        return got_fields_idx
