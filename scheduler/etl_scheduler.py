import schedule
import time
from etl.yfinance_to_gs_etl import run_yf_to_gs_etl_multi_stock

schedule.every().day().at("12:00").do(run_yf_to_gs_etl_multi_stock)

while True:

    schecule.run_pending()

    time.sleep(60)