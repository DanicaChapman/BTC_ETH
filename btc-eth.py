import streamlit as st
import yfinance as yf
import datetime
from datetime import date, timedelta


today = datetime.date.today()
last_week = today - datetime.timedelta(days=5)

st.title("Bitcoin and Ethereum Daily Prices")
st.header("Dashboard")

#ticker variables
bitcoin = "BTC-USD"
ethereum = "ETH-USD"

#yfinance data
btc_data = yf.Ticker(bitcoin)
eth_data = yf.Ticker(ethereum)

#history
btc_his = btc_data.history(period="max")
eth_his = eth_data.history(period="max")

#dataframe data
BTC = yf.download(bitcoin, start=last_week, end=date.today().strftime("%Y-%m-%d"))
ETH = yf.download(ethereum, start=last_week, end=date.today().strftime("%Y-%m-%d"))

st.write("Bitcoin")
st.bar_chart(btc_his.Close)
st.table(BTC)


st.write("Ethereum")
st.bar_chart(eth_his.Close)
st.table(ETH)