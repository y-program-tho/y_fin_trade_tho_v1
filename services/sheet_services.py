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


    def read_sheet(self, worksheet_name):

        worksheet = self.sheet.worksheet(worksheet_name)
        stonks_df = pd.DataFrame(worksheet.get_all_records())

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

