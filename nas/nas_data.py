import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 加载纳斯达克指数数据
data = pd.read_csv('nasdaq100.csv')
dates = data['Date']
prices = data['Close']

# 使用移动平均线进行平滑处理
window_size = 5  # 你可以根据需要调整窗口大小
smoothed_prices = prices.rolling(window=window_size).mean()

# 初始化存储局部最大值和最小值的列表
local_maxima = []
local_minima = []

# 滑动窗口计算局部最大值和最小值
for i in range(window_size, len(smoothed_prices) - window_size):
    window = smoothed_prices[i - window_size:i + window_size + 1]
    if prices[i] == window.max():
        local_maxima.append((dates[i], prices[i]))
    elif prices[i] == window.min():
        local_minima.append((dates[i], prices[i]))

# 转换为DataFrame以便于绘图和分析
local_maxima_df = pd.DataFrame(local_maxima, columns=['Date', 'Price'])
local_minima_df = pd.DataFrame(local_minima, columns=['Date', 'Price'])

# 绘制结果
plt.figure(figsize=(14, 7))
plt.plot(dates, prices, label='Nasdaq Index', color='blue')
plt.plot(dates, smoothed_prices, label='Smoothed Nasdaq Index', color='orange')
plt.scatter(local_maxima_df['Date'], local_maxima_df['Price'], color='red', label='Local Maxima', marker='^')
plt.scatter(local_minima_df['Date'], local_minima_df['Price'], color='green', label='Local Minima', marker='v')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Nasdaq Index with Local Maxima and Minima')
plt.legend()
plt.show()
