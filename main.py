import streamlit as st
import etl.yfinance_etl_to_gs as yf_to_gs

st.title("y_fin_trade_tho_v1")
stonks_data = yf_to_gs.proto_stonks_data()
st.dataframe(stonks_data)

# Spacing
st.write(" ")
st.write(" ")
st.write(" ")

ticker = st.selectbox("What stock would you like to view",
                     ('MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN")
                     )
st.subheader(f"{ticker} Stock Chart")
st.line_chart(stonks_data[stonks_data['Ticker'] == ticker]['Close'], y='Close')
