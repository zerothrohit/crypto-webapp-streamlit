import yfinance as yf
import streamlit as st
from streamlit.script_runner import RerunException
import plotly.express as px
#import plotly.graph_objects as go

from PIL import Image
from urllib.request import urlopen

from datetime import date

today = date.today()

# YY-mm-dd
d = today.strftime("%Y-%m-%d")
#print("d1 =", d1)

st.write("""
# Simple Cryptocurrency Price App💰
_Shown are the Cryptocurrency closing price and graph_
""")


#sidebar
st.sidebar.header('Select a cryptocurrency👆')
currency = st.sidebar.selectbox('Cryptocurrency:', ('Bitcoin (BTC)', 'Ethereum (ETH)', 'Ripple (XRP)', 'Tether (USDT)', 'Polygon (MATIC)', 'DogeCoin (DOGE)', 'Shiba Inu (SHIB)', 'Solana (SOL)', 'Cardano (ADA)', 'Polkadot (DOT)', 'Litecoin (LTC)'))
currencytype = st.sidebar.selectbox('Currency:', ('INR (₹)', 'USD ($)'))
if st.sidebar.button('Refresh Data'):
    raise RerunException(st._RerunData(None))

if currencytype == 'INR (₹)':
    ct = "INR"
    cs = "₹"

if currencytype == 'USD ($)':
    ct = "USD"
    cs = "$"

Bitcoin = 'BTC' + '-' + ct
#print(Bitcoin)
Ethereum = 'ETH' + '-' + ct
Ripple = 'XRP' + '-' + ct
Tether = 'USDT' + '-' + ct
Polygon = 'MATIC' + '-' + ct
Dogecoin = 'DOGE' + '-' + ct
ShibaInu = 'SHIB' + '-' + ct
Solana = 'SOL' + '-' + ct
Cardano = 'ADA' + '-' + ct
Polkadot = 'DOT' + '-' + ct
Litecoin = 'LTC' + '-' + ct

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
USDT_Data = yf.Ticker(Tether)
MATIC_Data = yf.Ticker(Polygon)
DOGE_Data = yf.Ticker(Dogecoin)
SHIB_Data = yf.Ticker(ShibaInu)
SOL_Data = yf.Ticker(Solana)
ADA_Data = yf.Ticker(Cardano)
DOT_Data = yf.Ticker(Polkadot)
LTC_Data = yf.Ticker(Litecoin)

BTC_History = BTC_Data.history(period="max")
ETH_History = ETH_Data.history(period="max")
XRP_History = XRP_Data.history(period="max")
USDT_History = USDT_Data.history(period="max")
MATIC_History = MATIC_Data.history(period="max")
DOGE_History = DOGE_Data.history(period="max")
SHIB_History = SHIB_Data.history(period="max")
SOL_History = SOL_Data.history(period="max")
ADA_History = ADA_Data.history(period="max")
DOT_History = DOT_Data.history(period="max")
LTC_History = LTC_Data.history(period="max")
#print(BTC_History)

BTC = yf.download(Bitcoin, start=d, end=d)
ETH = yf.download(Ethereum, start=d, end=d)
XRP = yf.download(Ripple, start=d, end=d)
USDT = yf.download(Tether, start=d, end=d)
MATIC = yf.download(Polygon, start=d, end=d)
DOGE = yf.download(Dogecoin, start=d, end=d)
SHIB = yf.download(ShibaInu, start=d, end=d)
SOL = yf.download(Solana, start=d, end=d)
ADA = yf.download(Cardano, start=d, end=d)
DOT = yf.download(Polkadot, start=d, end=d)
LTC = yf.download(Litecoin, start=d, end=d)

#Bitcoin(BTC)
if currency == 'Bitcoin (BTC)':
    st.write("**Bitcoin **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/1.png'))
    #Display Image
    st.image(image)
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

#Ethereum(ETH)
if currency == 'Ethereum (ETH)':
    st.write("**Ethereum **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/1027.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(ETH)
    #Display Linechart
    fig = px.line(ETH_History, x=ETH_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Ripple(XRP)
if currency == 'Ripple (XRP)':
    st.write("**Ripple **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/52.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(XRP)
    #Display Linechart
    fig = px.line(XRP_History, x=XRP_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Tether(USDT)
if currency == 'Tether (USDT)':
    st.write("**Tether **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/825.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(USDT)
    #Display Linechart
    fig = px.line(USDT_History, x=USDT_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Polygon(MATIC)
if currency == 'Polygon (MATIC)':
    st.write("**Polygon **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://www.coinopsy.com/media/img/logos/matic_network.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(MATIC)
    #Display Linechart
    fig = px.line(MATIC_History, x=MATIC_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Dogecoin(DOGE)
if currency == 'Dogecoin (DOGE)':
    st.write("**Dogecoin **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/74.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(DOGE)
    #Display Linechart
    fig = px.line(DOGE_History, x=DOGE_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Shiba Inu(SHIBA)
if currency == 'Shiba Inu (SHIB)':
    st.write("**Shiba Inu **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/5994.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(SHIB)
    #Display Linechart
    fig = px.line(SHIB_History, x=SHIB_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Solana(SOL)
if currency == 'Solana (SOL)':
    st.write("**Solana **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://digitalcoinprice.com/assets/images/coins/200x200/solana.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(SOL)
    #Display Linechart
    fig = px.line(SOL_History, x=SOL_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

#Cardano(ADA)
if currency == 'Cardano (ADA)':
    st.write("**Cardano **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/2010.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(ADA)
    #Display Linechart
    fig = px.line(ADA_History, x=ADA_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)


#Polkadot(DOT)
if currency == 'Polkadot (DOT)':
    st.write("**Polkadot **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/6636.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(DOT)
    #Display Linechart
    fig = px.line(DOT_History, x=DOT_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)


#Litecoin(LTC)
if currency == 'Litecoin (LTC)':
    st.write("**Litecoin **" + "(**" + cs + "**)")
    image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/200x200/2.png'))
    #Display Image
    st.image(image)
    #Display Dataframe
    st.table(LTC)
    #Display Linechart
    fig = px.line(LTC_History, x=LTC_History.index, y='Close', width=850, height=600)
    st.plotly_chart(fig)

st.sidebar.subheader(
    """Created by [Rohit Wahwal](https://github.com/zerothrohit)😊 """)
