import streamlit as st
import etl.yfinance_etl_to_gs as yf_to_gs

st.title("y_fin_trade_tho_v1")
stonks_data = yf_to_gs.get_stonk_data_from_gs()
st.dataframe(stonks_data)

# Spacing
st.write(" ")
st.write(" ")
st.write(" ")

ticker = st.selectbox("What stock would you like to view",
                     ('MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN")
                     )
st.write(f"The columns are {[stonks_data.columns]}")
st.subheader(f"{ticker} Stock Chart")
st.line_chart(stonks_data[stonks_data['Ticker'] == ticker], x='Date', y='Close')
