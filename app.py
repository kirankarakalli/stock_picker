import streamlit as st
from stock_picker.crew import StockPicker
import yfinance as yf

st.title("CrewAI Stock Picker")

tickers = st.text_input(
    "Enter stock tickers",
    value="AAPL, MSFT, TSLA"
)

ticker_list = [t.strip().upper() for t in tickers.split(",") if t.strip()]

st.subheader("Stock Price Charts")

period = st.selectbox(
    "Select period",
    ["1mo", "6mo", "1y", "5y"],
    index=2
)

for ticker in ticker_list:
    st.write(f"### {ticker}")

    stock = yf.Ticker(ticker)
    history = stock.history(period=period)

    if history.empty:
        st.warning(f"No price data found for {ticker}")
    else:
        st.line_chart(history["Close"])

if st.button("Run Stock Picker"):
    inputs = {
        "topic": tickers
    }

    with st.spinner("Running CrewAI agents..."):
        result = StockPicker().crew().kickoff(inputs=inputs)

    st.subheader("Final Report")
    st.markdown(str(result))