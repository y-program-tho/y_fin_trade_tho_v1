import streamlit as st

def plot_stock_price(df):
    return st.line_chart(df[["Close", "SMA_20", "EMA_20"]])