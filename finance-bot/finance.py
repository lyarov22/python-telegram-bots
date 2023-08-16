import yfinance as yf

msft = yf.Ticker("MSFT")
tsla = yf.Ticker("TSLA")

hist = tsla.history(period="1wk")

#напиши код который удаляет числа которые идут через :

print(hist['Close'][-7:])