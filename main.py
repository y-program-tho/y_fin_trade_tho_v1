import streamlit as st
from services.sheet_services import SheetService


st.title("y_fin_trade_tho_v1")
sheet_service = SheetService()
stonks_data = sheet_service.read_sheet("stock_price") 
st.dataframe(stonks_data)

# Spacing
st.write(" ")
st.write(" ")
st.write(" ")

ticker = st.selectbox("What stock would you like to view",
                     ('MSFT', 'AAPL', 'GOOG', "NVDA", "AMZN")
                     )
st.subheader(f"{ticker} Stock Chart")
st.line_chart(stonks_data[stonks_data['Ticker'] == ticker], x='Date', y='Close')
