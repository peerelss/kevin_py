import yfinance as yf

# 指定股票代码和时间范围
ticker = "AAPL"  # 替换成您感兴趣的股票代码
start_date = "2022-01-01"  # 替换成您感兴趣的起始日期
end_date = "2022-06-30"  # 替换成您感兴趣的结束日期

# 获取历史股票价格数据
stock_data = yf.download(ticker, start=start_date, end=end_date)

print(stock_data)