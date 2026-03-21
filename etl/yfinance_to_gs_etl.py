import pandas as pd
import yfinance as yf
from services.sheet_services import SheetService

def extract_stock_data_yfinance():

    stonks_df = yf.download(['MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN"], period='1mo')

    return stonks_df


def clean_stock_data(df):

    df.columns = df.columns.str.lower()

    df = df.fillna()
    
    df = df.drop_duplicates()
    
    return df 

def run_yf_to_gs_etl_multi_stock():
    # Dowload data from yfinance for top 5 stocks
    stonks_data = extract_stock_data_yfinance()

    # Transform stock data dataframe from wide to long 
    stonk_df_step_one = stonk_data.stack()
    stonk_df_step_two = stonk_df_step_one.rename_axis(None, axis=1)
    stonk_df_final = stonk_df_step_two.reset_index()
    stonk_df_final['Date'] = stonk_df_final['Date'].astype(str)

    # Load data into google sheets
    sheet_service = SheetService()
    sheet_service.write_to_sheet("stock_price", stonk_df_final)
    return f"Data for {period} has been loaded to Google Sheets successfully. Size of data:{stonk_df_final.shape}"
