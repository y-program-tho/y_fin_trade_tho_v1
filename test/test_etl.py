import numpy as np
import pandas as pd
from unittest.mock import patch
import etl.yfinance_to_gs_etl as etl

def test_etl_clean_market_data_for_dupes():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-01"],
        "close":[100, 100]
    })

    cleaned = etl.clean_stock_data(df)

    assert len(cleaned) == 1

def test_etl_clean_market_data_for_na():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-02"],
        "close":[np.nan, np.nan]
    })

    filled_na = etl.clean_stock_data(df)

    assert len(df) == len(filled_na[filled_na['close']=='-'])

def test_etl_clean_market_data_for_na():

    df = pd.DataFrame({
        "Date":["2024-01-01", "2024-01-02"],
        "Close":[150, 350]
    })

    lowercase_columns = etl.clean_stock_data(df)

    is_lowered = [col.islower() for col in lowered_cols]
    is_lowered = [col for col in is_lowered if True]

    assert len(lowercase_columns.columns) == lem(is_lowered)

def test_etl_transform_yf_multi_stock_pivot_data():

    df = pd.DataFrame({
        ("AAPL", "Close"):[100, 101],
        ("MSFT", "Close"):[200, 201]
    })

    df.index = pd.date_range("2024-01-01", periods=2)

    result = etl.transform_yf_multi_stock_pivot_data(df)

    assert isinstance(df, pd.DataFrame)

def test_etl_transform_yf_multi_stock_pivot_data_col_struct():

    df = pd.DataFrame({
        ("AAPL", "Close"):[100],
        ("MSFT", "Close"):[200]
    })
    
    result = etl.transform_yf_multi_stock_pivot_data(df)

    assert result.shape[1] >= 2


def test_etl_transform_yf_multi_stock_pivot_data_integrity():

    df = pd.DataFrame({
        ("AAPL", "Close"):[100],
        ("MSFT", "Close"):[200]
    })

    result = etl.transform_yf_multi_stock_pivot_data(df)

    values = result.iloc[:, -1].tolist()
 
    assert 100 in values
    assert 200 in values

def test_etl_transform_yf_multi_stock_pivot_data_empty():

    df = pd.DataFrame()

    result = etl.transform_yf_multi_stock_pivot_data(df)
 
    assert result.empty

def test_etl_transform_yf_multi_stock_pivot_data_single_stock():

    df = pd.DataFrame({
        ("AAPL", "Close"):[100, 101]
    })

    df.index = pd.date_range("2024-01-01", periods=2)

    result = etl.transform_yf_multi_stock_pivot_data(df)

    assert len(result) == 2


@patch("builtins.print")
def test_etl_valiadte_isnull():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-01"],
        "close":[np.nan, 100]
    })

    etl.validate_stock_data(df)

    assert mock_print.assert_called_with("Missing close prices")

@patch("builtins.print")
def test_etl_valiadte_is_negative():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-01"],
        "close":[100, -75]
    })

    etl.validate_stock_data(df)

    assert mock_print.assert_called_with("Negative price detected")

@patch("builtins.print")
def test_etl_detect_dupes():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-01"],
        "close":[100, 100]
    })

    etl.detect_dupes_or_outliers(df)

    assert mock_print.assert_called_with("Duplicates detected")

@patch("builtins.print")
def test_etl_detect_bad_data():

    df = pd.DataFrame({
        "date":["2024-01-01", "2024-01-03"],
        "close":[100, 50000]
    })

    etl.detect_dupes_or_outliers(df)

    assert mock_print.assert_called_with("Possible bad data detected")