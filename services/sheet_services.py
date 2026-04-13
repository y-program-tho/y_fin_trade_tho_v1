import os
import logging
import time
import gspread
import pandas as pd
import streamlit as st
from dotenv import load_dotenv, dotenv_values 
from google.oauth2.service_account import Credentials

logger = logging.getLogger(__name__)

class SheetService:

    def __init__(self):

        load_dotenv()
        scope = os.getenv('SCOPE')
        cred_file = os.getenv('CRED_FILE')
        sheet_id = os.getenv('SHEET_ID')

        creds = Credentials.from_service_account_file(cred_file, scopes=[scope])

        client = gspread.authorize(creds)

        self.sheet = client.open_by_key(sheet_id)

        logger.info("Starting Sheet Services")

        return

    def read_sheet(self, worksheet_name):

        logger.info(f"Reading worksheet: {worksheet_name}")

        worksheet = self.sheet.worksheet(worksheet_name)
        
        stonks_df = pd.DataFrame(worksheet.get_all_records())

        logger.info(f"Data retrieved. No. of rows: {len(stonks_df)}, No. of columns: {len(stonks_df.columns)}")

        return stonks_df

    def write_to_sheet(self, worksheet_name, df):

        logger.info(f"Writing new data to sheet")
 
        worksheet = self.sheet.worksheet(worksheet_name)

        worksheet.clear()

        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

        logger.info(f"Worksheet has been updated")

        return

    def append_rows_to_sheet(self, worksheet_name, df, retries=3):

        worksheet = self.sheet.worksheet(worksheet_name)

        rows = df.values.tolist()

        for attempt in range(retries):
            
            try:
                worksheet.append_rows(df.values.tolist())

                logger.info(f"Appeneded {len(rows)} rows")

                return
            
            except Exception as e:

                logging.warning(f"Retry {attempt+1}, failed: {e}")

                time.sleep(2)

        raise Exception(f"Failed to append rows after retries")
