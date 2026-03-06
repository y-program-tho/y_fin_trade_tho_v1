# y_fin_trade_tho_v1

Table Of Contents:
- [Description](#description)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Project Usage](#usage)

## Description
y_fin_trade_tho_v1 is lightweight Python Application that allows users to select a stock ticker and view various pieces of information such as Open Price, Close Price, Volume etc with a chart visualisations with technical indicators applicable to the selected stock.

The intention is that this will be deployed as a web application using Streamlit, allowing users to interact with the data and visualizations in a user-friendly interface without needing to write code or prepare a development enviroment.

The current architecture layout is as follows:
```
y_fin_trading_tho_v1
    │
    ├─ main.py
    │
    └─ etl/
    │    │  
    │    └ yfinance_etl_to_gs.py
    │
    └─ fin_visualisation/ 
         │ 
         ├ tech_indicators.py
         └ charts.py
```

## Data Sources
Finacial data is sourced from yfinace library which provides access to Yahoo Finance data.

## Installation
To install the required dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
``` 

Once the dependencies are installed, you can run the application using the following command:

```bash
streamlit run main.py
``` 