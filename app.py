import yfinance as yf
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

from PIL import Image
from urllib.request import urlopen

st.write("""
# Simple Cryptocurrency Price App
Shown are the Cryptocurrency closing price and volume of Bitcoin!
""")

Bitcoin = 'BTC-INR'
Ethereum = 'ETH-INR'

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)

BTC_History = BTC_Data.history(period="max")
ETH_History = ETH_Data.history(period="max")
#print(BTC_History)

BTC = yf.download(Bitcoin, start="2021-12-30", end="2021-12-30")
ETH = yf.download(Ethereum, start="2021-12-30", end="2021-12-30")

#Bitcoin
st.write("Bitcoin (₹)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/1.png'))
#Display Image
st.image(imageBTC)
#Display Dataframe
st.table(BTC)
#Display Linechart
#st.line_chart(BTC_History.Close, height=500)
#Display Barchart
#st.bar_chart(BTC_History.Close)
fig = px.line(BTC_History, x=BTC_History.index, y='Close', width=850, height=600)
st.plotly_chart(fig)
# fig = go.Figure([go.Scatter(x=BTC_History['Date'], y=BTC_History['Close'])])
# fig.show()

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
# tickerSymbol = 'GOOGL'
# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)
# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-5')
# # Open	High	Low	Close	Volume	Dividends	Stock Splits

# st.line_chart(tickerDf.Close)
# st.bar_chart(tickerDf.Volume)


