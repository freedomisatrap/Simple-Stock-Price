import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Simple Stock Price App

 Shown are the stock **closing price** and **volume** of Tesla
""")
tickerSymbol ='TSLA'
#define the ticked symbol
tickerData = yf.Ticker(tickerSymbol)
#get the histirical prices for this ticker
tickerDf= tickerData.history(period='id',start='2017-5-31',end='2021-4-21')
#Open High Low Close Volume Dividends Stock Splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume) 
