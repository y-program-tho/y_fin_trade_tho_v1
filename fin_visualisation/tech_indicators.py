from services.sheet_services import SheetService
from fin_visualisation.tech_indicators import TechnicalIndicator


class TechnicalIndicator:

    def calc_sma(df, window=20):
        df[f"SMA_of_{window}"] = df["Close"].rolling(winodw=window).mean()
        return df
    
    def calc_ema(df, window=20):
        df[f"EMA_of_{window}"] = df["Close"].ewm(span=window, adjust=False).mean()
        return df

    def calc_all_indicators(df):

        df = TechnicalIndicator.calc_sma(df)
        df = TechnicalIndicator.calc_ema(df)
        
        return df