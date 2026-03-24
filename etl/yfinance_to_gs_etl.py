import logging
import pandas as pd
import yfinance as yf
from services.sheet_services import SheetService

logger = logging.getLogger(__name__)

def clean_stock_data(df):

    logger.info(f"Cleaning data from yfinance")
    
    df.columns = df.columns.str.lower()
    
    df = df.fillna()
    
    df = df.drop_duplicates()
    
    df['date'] = df['date'].astype(str)
    
    return df 

def transform_yf_multi_stock_data(df):

    logger.info(f"Changing the structure of table")

    df = df.stack()
    
    df = df.rename_axis(None, axis=1)
    
    df = df.reset_index()
    
    return df  

def validate_stock_data(df):

    logger.info(f"")

    if df['close'].isnull().any():
        raise ValueError("Missing close prices")

    if (df['close'] < 0).any():
        raise ValueError("Negative price detected")

    return True

def detect_dupes_or_outliers(df):

    logger.info(f"")

    if len(df.duplicated()) > 0:
        print("Duplicates detected")

    if df["close"].max()>1000:
        print("Possible bad data detected")

    return

def run_yf_to_gs_etl_multi_stock():

    logger.info("Starting ETL Pipeline")

    # Dowload data from yfinance for top 5 stocks
    stonks_df = yf.download(['MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN"], period='1mo')

    sheet_service = SheetService()
    sheet_service.write_to_sheet("raw_stock_data", stonks_df)

    # Transform stock data dataframe from wide to long 
    stonks_df = transform_yf_multi_stock_data(stonks_df)

    stonks_df = clean_stock_data(stonks_df)

    sheet_service.write_to_sheet("processed_stock_data", stonk_df_final)
    return f"Data for {period} has been loaded to Google Sheets successfully. Size of data:{stonk_df_final.shape}"