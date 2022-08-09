# PP_binance_technical_challenge

## Introduction
Binance technical challenge for the interview process.

## Challenge
### Assignment
- Use public market data from the SPOT API at https://api.binance.com
- Binance API spot documentation is at https://github.com/binance-exchange/binance-official-api-docs/
- All answers should be provided as source code written in either Go, Python, Java, Rust, and/or Bash.
 
### Questions
  1. Print the top 5 symbols with quote asset BTC and the highest volume over the last 24 hours in descending order.
  2. Print the top 5 symbols with quote asset USDT and the highest number of trades over the last 24 hours in descending order.
  3. Using the symbols from Q1, what is the total notional value of the top 200 bids and asks currently on each order book?
  4. What is the price spread for each of the symbols from Q2?
  5. Every 10 seconds print the result of Q4 and the absolute delta from the previous value for each symbol.
  6. Make the output of Q5 accessible by querying http://localhost:8080/metrics using the Prometheus Metrics format.

## Installation

* Install requirements.txt
  * `pip install -r requirements.txt`
* Run with Python 3.10.2
  * `python main.py`


## Notes
This script prints the results onto the screen and loops forever when started.