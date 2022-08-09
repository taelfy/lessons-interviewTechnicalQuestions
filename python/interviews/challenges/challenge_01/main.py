import time
from prometheus_client import start_http_server, Gauge
from utils.BinanceChallenge import BinanceClass, get_ticker_fields, print_notional_values, update_prom_gauge

if __name__ == '__main__':
    start_http_server(8080)
    prom_gauge = Gauge('spread_abs_delta_value', 'Delta between new and old price spread ', ['symbol'])

    url = 'https://api.binance.com/api'
    bc = BinanceClass(url)
    # Q1
    btc_top_5 = get_ticker_fields('BTC', 'quoteVolume', True, limit=5)
    # Q2
    usdt_top_5 = get_ticker_fields('USDT', 'count', True, limit=5)
    # Q3
    print_notional_values(btc_top_5)
    # Q4
    bc.print_price_spread(usdt_top_5)

    while True:
        # Q5
        got_abs_delta = bc.print_abs_delta()
        # Q6
        update_prom_gauge(prom_gauge, got_abs_delta)
        time.sleep(10)
