# y_fin_trade_tho_v1

Table Of Contents:
- [Description](#description)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Project Usage](#usage)
- [System Design](#system-design)

## Description
y_fin_trade_tho_v1 is lightweight Python Application that allows users to select a stock ticker and view various pieces of information such as Open Price, Close Price, Volume etc with a chart visualisations with technical indicators applicable to the selected stock.

The intention is that this will be deployed as a web application using Streamlit, allowing users to interact with the data and visualizations in a user-friendly interface without needing to write code or prepare a development enviroment.

The current architecture layout is as follows:
```
y_fin_trading_tho_v1
    │
    ├─ main.py
    |
    ├─ config/
    │   │  
    │   └ logging_config.py
    │   
    ├─ etl/
    │   │  
    │   └ yfinance_etl_to_gs.py
    |   
    ├─ fin_visualisation/ 
    |   │ 
    |   ├ charts.py 
    |   └ tech_indicators.py
    |
    ├─ scheduler/ 
    |   │  
    |   └ etl_scheduler.py
    |   
    └─ service/
        │  
        └ sheet_services.py    
```

## Data Sources
Finacial data is sourced from yfinace library which provides access to Yahoo Finance data.

## Data Schema
For the data schema it is based on the transformed data from yfinance ("processed_stock_data" table), then there exists data that hold the technical indicators that are calculated from the stock data ("technical_indicator" table). Here are the schemas for each table:

“processed_stock_data” table  

| Column | Type | Example | Description |
| --------- | -------- | ---------- | ----------------------------------------------------- |
| timestamp | datetime | 2025-01-01 | Price of stock start of day |
| ticker | string | AAPL | A 3-4 letter company abbreviation |
| open | float | 180.22 | Price of stock at the start of a given timeframe |
| high | float | 183.50 | Price of stock at it highest within a given timeframe |
| low | float | 178.90 | Price of stock at its lowest within a given timeframe |
| close | float | 181.45 | Price of stock at the end of a given timeframe |
| volume | integer | 30000000 | No. of trades executed within a given time period |
  
  
“tech_indicators” table  

| Column | Type | Example | Description |
| --------- | -------- | ---------- | ------------------------------------------------------------------------- |
| timestamp | datetime | 2025-01-01 | Price of stock start of day |
| ticker | string | AAPL | A 3-4 letter company abbreviation |
| SMA_20 | float | 180.22 | A simple moving average that has a 20 value window per calculation  |
| SMA_50 | float | 183.50 | A simple moving average that has a 50 value window per calculation  |
| EMA_20 | float | 180.22 | An exponential moving average that has a 20 value window per calculation  |
| EMA_50 | float | 183.50 | An exponential moving average that has a 50 value window per calculation  |
  


## Usage
The platform will be deployed onto Streamlit, allowing users to interact with the data and visualizations in a user-friendly interface without needing to write code or prepare a development enviroment.

The platform will also be dockerised so that it can be easily deployed to a cloud service provider such as AWS, GCP or Azure.

## System Design
The system is designed to create a modular platform that will allow ETL pipelines to extract financial trading data and load it into a google sheet for storage, then ustilise the data in visulaisations and technical indicators to emulate a trading enviroment for users to interact and learn to trade in a risk free enviroment.

'''
Exchange
   │
   └── Company
           ├── StockPrice
           └── Indicator

User
 │
 ├── Portfolio
 │       ├── Position ──> Company
 │       └── Trade ──> Company
 │
 ├── Watchlist
 │       └── WatchlistItem ──> Company
 │
 └── Strategy
         └── Backtest
'''