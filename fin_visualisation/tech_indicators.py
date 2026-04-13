from services.sheet_services import SheetService
from fin_visualisation.tech_indicators import TechnicalIndicator


class TechnicalIndicator:

    def calc_sma(df, window=20):
        tickers = list(set(df['ticker'].to_list()))

        sma_df = df[df['ticker']==tickers[0]]
        sma_df[f"SMA_of_{window}"] = sma_df["close"].rolling(window=window).mean()

        for ticker in tickers[1:]:
            sma_df = df[df['ticker']==ticker]
            sma_df[f"SMA_of_{window}"] = sma_df["close"].rolling(window=window).mean()
            df = pd.concat([df, sma_df])

        df = df.reset_index(drop=True)

        return df
    
    def calc_ema(df, window=20):
        tickers = list(set(df['ticker'].to_list()))

        ema_df = df[df['ticker']==tickers[0]]
        ema_df[f"EMA_of_{window}"] = ema_df["close"].ewm(span=window, adjust=False).mean()

        for ticker in tickers[1:]:
            ema_df = df[df['ticker']==ticker]
            ema_df[f"EMA_of_{window}"] = ema_df["close"].ewm(span=window, adjust=False).mean()
            df = pd.concat([df, ema_df])

        df = df.reset_index(drop=True)
        
        return df

    def calc_all_indicators(df):

        df = TechnicalIndicator.calc_sma(df)
        df = TechnicalIndicator.calc_ema(df)
        
        return df