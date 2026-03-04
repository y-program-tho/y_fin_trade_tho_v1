import pandas as pd
import yfinance as yf

# Dowload data from yfinance for top 5 stocks
stonk_data = yf.download(['MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN"], period='1mo')

# Transform stock data to reduce number of columns
stonk_df = stonk_data.reset_index()
stonk_df_step_one = stonk_data.stack()
stonk_df_step_two = stonk_df_step_one.reset_index()
stonk_df_step_three = stonk_df_step_two.rename_axis(None, axis=1)
stonk_df_step_four = stonk_df_step_three.set_index("Date")

