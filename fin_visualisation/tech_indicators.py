from services.sheet_services import SheetService
from fin_visualisation.tech_indicators import TechnicalIndicator


class TechnicalIndicator:

    def calc_sma(df, window=20):
        df[f"SMA_of_{window}"] = df["close"].rolling(winodw=window).mean()
        return df
    
    def calc_ema(df, window=20):
        df[f"EMA_of_{window}"] = df["close"].ewm(span=window, adjust=False).mean()
        return df

    def calc_all_indicators(df):

        df = TechnicalIndicator.calc_sma(df)
        df = TechnicalIndicator.calc_ema(df)
        
        return df
    
def load_n_calc():
    
    sheet_service = SheetService()

    df = sheet_service.read_sheet("stock_price")

    df = TechnicalIndicator.calc_all_indicators(df)

    return df
