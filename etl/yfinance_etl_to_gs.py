import pandas as pd
import yfinance as yf

def proto_stonks_data():
    # Dowload data from yfinance for top 5 stocks
    stonk_data = yf.download(['MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN"], period='1mo')

    # Transform stock data dataframe from wide to long 
    stonk_df_step_one = stonk_data.stack()
    stonk_df_step_two = stonk_df_step_one.rename_axis(None, axis=1)
    stonk_df_step_three = stonk_df_step_two.reset_index()
    stonk_df_final = stonk_df_step_three.set_index("Date")
    return stonk_df_final

