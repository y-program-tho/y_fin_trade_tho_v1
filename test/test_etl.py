import numpy as np
import pandas as pd
import etl.yfinance_to_gs_etl

def test_clean_market_data_for_dupes():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-01"],
        "close":[100, 100]
    })

    cleaned = clean_stock_data(df)

    assert len(cleaned) == 1

def test_clean_market_data_for_na():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-02"],
        "close":[np.nan, np.nan]
    })

    filled_na = clean_stock_data(df)

    assert len(df) == len(filled_na[filled_na['close']=='-'])