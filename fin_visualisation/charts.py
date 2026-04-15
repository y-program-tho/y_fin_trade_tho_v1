import streamlit as st

def plot_stock_price(df):
    return st.line_chart(df[["Close"]])