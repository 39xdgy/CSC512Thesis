from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np

np.random.seed(7)

model = Sequential()
model.add(Dense(4, input_dim = 3, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

adam = optimizers.adam(lr = 0.01)
model.compile(loss = 'mse', optimizer = adam, metrics = ['accuracy'])

x = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1], [1, 0, 1]])
y = np.array([0, 1, 1, 1, 1, 1, 1])





model.fit(x, y, epochs = 1000)

test_out = model.predict(np.array([[1, 1, 1]]))
print(test_out)

