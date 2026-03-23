import pandas as pd
import yfinance as yf
from services.sheet_services import SheetService

def clean_stock_data(df):

    logger.info(f"")

    df.columns = df.columns.str.lower()

    df = df.fillna()
    
    df = df.drop_duplicates()
    
    return df 

def transform_yf_multi_stock_data(df):

    logger.info(f"")

    df = df.stack()
    df = df.rename_axis(None, axis=1)
    df = df.reset_index()
    df['Date'] = df['Date'].astype(str)

    return df  

def validate_stock_data(df):

    logger.info(f"")

    if df['Close'].isnull().any():
        raise ValueError("Missing close prices")

    if (df['Close'] < 0).any():
        raise ValueError("Negative price detected")

    return True

def detect_dupes_or_outliers(df):

    logger.info(f"")

    if len(df.duplicated()) > 0:
        print("Duplicates detected")

    if df["Close"].max()>1000:
        print("Possible bad data detected")

    return

def run_yf_to_gs_etl_multi_stock():

    logger.info("Starting ETL Pipeline")

    # Dowload data from yfinance for top 5 stocks
    stonks_df = yf.download(['MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN"], period='1mo')

    stonks_df = clean_stock_data(stonks_df)

    # Transform stock data dataframe from wide to long 
    stonks_df = transform_yf_multi_stock_data(stonks_df)

    # Load data into google sheets
    sheet_service = SheetService()
    sheet_service.write_to_sheet("stock_price", stonk_df_final)
    return f"Data for {period} has been loaded to Google Sheets successfully. Size of data:{stonk_df_final.shape}"

