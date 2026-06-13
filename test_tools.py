import yfinance as yf

stock = yf.Ticker("AAPL")
news = stock.news

print(news[0])