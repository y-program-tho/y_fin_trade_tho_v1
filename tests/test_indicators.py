import numpy as np
import pandas as pd
from unittest.mock import patch
import fin_visualisation.tech_indicators as ti

def test_sma():

    df = pd.DataFrame({
        "close":[10, 20, 20, 15, 30]
    })

    result = ti.calc_sma(df, window=3)

    assert "SMA_3" in result.columns

def test_ema():

    df = pd.DataFrame({
        "close":[10, 20, 20, 15, 30]
    })

    result = ti.calc_ema(df, window=3)

    assert "EMA_3" in result.columns