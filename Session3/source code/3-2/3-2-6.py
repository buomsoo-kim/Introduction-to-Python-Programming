import numpy as np 

data = np.loadtxt('stock-data.csv', delimiter = ',')
data.shape

x_data = data[:,:-1]
y_data = data[:, -1]

print(x_data.shape)
print(x_data)

print(y_data.shape)
print(y_data)