import os
import pandas as pd
import yfinance as yf
import streamlit as st
import gspread
from dotenv import load_dotenv, dotenv_values
from google.oauth2.service_account import Credentials

def gs_config():
    load_dotenv()
    scope = os.getenv('SCOPE')
    cred_file = os.getenv('CRED_FILE')
    sheet_id = os.getenv('SHEET_ID')
    creds = Credentials.from_service_account_file(cred_file, scopes=[scope])
    client = gspread.authorize(creds)
    gs_workbook = client.open_by_key(sheet_id)
    return gs_workbook

# gs_workbook.worksheet.sheet1.get_all_values()

def yf_stocks_data_to_gs(stonk_list=['MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN"], period='1mo'):
    # Dowload data from yfinance for top 5 stocks
    stonk_data = yf.download(stonk_list, period=period)

    # Transform stock data dataframe from wide to long 
    stonk_df_step_one = stonk_data.stack()
    stonk_df_step_two = stonk_df_step_one.rename_axis(None, axis=1)
    stonk_df_final = stonk_df_step_two.reset_index()
    stonk_df_final['Date'] = stonk_df_final['Date'].astype(str)

    # Load data into google sheets
    stonk_gs_wb = gs_config()
    stonk_gs_wb.sheet1.update([stonk_df_final.columns.values.tolist()] + stonk_df_final.values.tolist())
    return f"Data for {period} has been loaded to Google Sheets successfully. Size of data:{stonk_df_final.shape}"

@st.cache_data(ttl=1800)
def get_stonk_data_from_gs():
    stonk_gs_wb = gs_config()
    stonks_df = pd.DataFrame(stonk_gs_wb.sheet1.get_all_values())
    stonks_df.columns = stonks_df.iloc[0]
    stonks_df = stonks_df[1:]
    stonks_df = stonks_df.reset_index(drop=True)
    stonks_df = stonks_df.rename_axis(None, axis=1)
    stonks_df['Date'] = pd.to_datetime(stonks_df['Date'])
    return stonks_df