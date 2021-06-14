from algorithm import Algorithm
from chart import CandlestickChart
import matplotlib.pyplot as plt
import numpy as np
import datetime as datetime
import pandas_datareader

def moving_average_(np_array, n):
    return np.convolve(np_array, np.ones(n)/n, mode='valid')

class TestAlgorithm(Algorithm):
    def __init__(self):
        self.cash = 100.0
        self.stocks = 0.0
        self.bought = []
        self.sold = []

    def buying_rule(self, chart, time):
        if time > 950: return
        if self.cash == 0.0: return
        if chart.moving_30[time] < chart.moving_50[time]:
            self.stocks = self.cash / chart.candlesticks[time]
            self.cash = 0.0
            self.bought.append(time)

    def selling_rule(self, chart, time):
        if time > 950: return
        if self.stocks == 0.0: return
        if chart.moving_30[time] > chart.moving_50[time]:
            self.cash = chart.candlesticks[time] * self.stocks
            self.stocks = 0.0
            self.sold.append(time)

money_gained = []
if_never_sold = []
for _ in range(1000):
    chart = CandlestickChart(1000)
    lst = TestAlgorithm.run(chart)
    """
    #print(chart.candlesticks)
    fig, axs = plt.subplots(2)
    fig.suptitle('Test')
    axs[0].plot(chart.candlesticks)
    axs[0].plot(chart.moving_average(30))
    axs[0].plot(chart.moving_average(50))
    for x in TestAlgorithm.algorithms[0].bought:
        axs[0].axvline(x=x, color='g')
    for x in TestAlgorithm.algorithms[0].sold:
        axs[0].axvline(x=x, color='r')
    axs[1].plot(lst)"""

    money_gained.append(lst[-1] - 100)
    if_never_sold.append(chart.candlesticks[-1] - 100)
    #print(f'Money gained: {lst[-1] - 100}')
    #print(f'If never sold: {chart.candlesticks[-1] - 100}')

print(f'Money gained: {sum(money_gained)}')
print(f'If never sold: {sum(if_never_sold)}')


#plt.show()


"""
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(chart.candlesticks)
axs[0].plot(TestAlgorithm.algorithms[0].moving_average_30)
axs[0].plot(TestAlgorithm.algorithms[0].moving_average_50)
axs[1].plot(lst)
plt.show()"""

"""
start = datetime.datetime(2016, 6, 10)
end = datetime.datetime(2021, 6, 3)

data = pandas_datareader.DataReader('AAPL', 'yahoo', start, end)
print(data)
data.plot(None, 'Close')
plt.ylim((0,150))
plt.yticks((0, 50, 100, 150))
plt.show()
#plt.plot(data["close"], data["date"])
"""
