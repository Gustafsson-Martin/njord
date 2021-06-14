import random
import numpy as np


class CandlestickChart():
    def __init__(self, n):
        self.stock = "AAPL"
        self.candlesticks = np.array(list(random_candlestick_generator(100, n)))
        self.moving_30 = self.moving_average(30)
        self.moving_50 = self.moving_average(50)

    def moving_average(self, n):
        return np.convolve(self.candlesticks, np.ones(n)/n, mode='valid')



def random_candlestick_generator(current_price, candles):
    i = 0
    while (i < candles):
        current_price = current_price * (1 + random.uniform(-0.00099, 0.001))
        yield current_price
        i += 1
