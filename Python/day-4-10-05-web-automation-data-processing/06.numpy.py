import numpy as np

prices = np.array([29.99,24.99,19.99,39.99,34.99])

print("Max price: ",np.max(prices))
print("Min price: ",np.min(prices))
print("Average price: ",np.mean(prices))
print("price>30: ",prices[prices>30])