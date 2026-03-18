import os
import pandas as pd
import streamlit as st
import gspread
from dotenv import load_dotenv, dotenv_values 
from google.oauth2.service_account import Credentials


class SheetService:
    def __init__(self):

        load_dotenv()
        scope = os.getenv('SCOPE')
        cred_file = os.getenv('CRED_FILE')
        sheet_id = os.getenv('SHEET_ID')

        creds = Credentials.from_service_account_file(cred_file, scopes=[scope])

        client = gspread.authorize(creds)
        self.sheet = client.open_by_key(sheet_id)


    @st.cache_data(ttl=1800)
    def read_sheet(self, worksheet_name):
        worksheet = self.sheet.worksheet(worksheet_name)
        stonks_df = pd.DataFrame(worksheet.get_all_records())
        stonks_df.columns = stonks_df.iloc[0]
        stonks_df = stonks_df[1:]
        stonks_df = stonks_df.reset_index(drop=True)
        stonks_df = stonks_df.rename_axis(None, axis=1)
        stonks_df['Date'] = pd.to_datetime(stonks_df['Date'])
        return stonks_df


    def write_to_sheet(self, worksheet_name, df):

        worksheet = self.sheet.worksheet(worksheet_name)

        worksheet.clear()

        worksheet.update(
            [
                df.columns.values.tolist() +
                df.values.tolist()
            ]
        )

    def append_rows_to_sheet(self, worksheet_name, df):

        worksheet = self.sheet.worksheet(worksheet_name)

        worksheet.append_rows(df.values.tolist())

