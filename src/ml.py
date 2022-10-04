import yfinance as yf
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_sample_images
import matplotlib.pyplot as plt

microsoft = yf.Ticker("MSFT")

history = microsoft.history(period='max', interval='1d')

PREVIOUS_OBSERVATIONS = 10

close = history["Close"].to_numpy()
sliding_window = np.lib.stride_tricks.sliding_window_view(close, window_shape = PREVIOUS_OBSERVATIONS)

x = sliding_window[:-1]
y = close[PREVIOUS_OBSERVATIONS:]

train_x = x[:-365]
train_y = y[:-365]
test_x = x[-365:]
test_y = y[-365:]

reg = MLPRegressor(hidden_layer_sizes = (128, 64, 32), verbose = True)

reg.fit(train_x, train_y)

prediction = reg.predict(test_x)
print(train_x)
print(test_x)
print(prediction)

plt.figure(figsize = (10,8))
plt.plot(list(range(len(test_x))), prediction)
plt.plot(list(range(len(close)-PREVIOUS_OBSERVATIONS)), y)

plt.figure(figsize = (10,8))
plt.plot(list(range(len(test_x))), test_y, color="red")
plt.plot(list(range(len(test_x))), prediction, color="blue")
plt.show()
