from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras import optimizers
from keras.datasets import mnist

import numpy as np


(x_train, y_train), (x_test, y_test) = mnist.load_data()

real_y_train = np.empty(shape = [0, 10])
real_y_test = np.empty(shape = [0, 10])


for i in y_train:
    trans = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    trans[i] = 1
    trans= np.array([trans])
    real_y_train = np.vstack((real_y_train, trans))



for i in y_test:
    trans = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    trans[i] = 1
    trans = np.array([trans])
    real_y_test = np.vstack((real_y_test, trans))


np.random.seed(7)


model = Sequential()
model.add(Dense(100, input_shape = (28, 28), activation = 'sigmoid'))
model.add(Dense(100, activation = 'sigmoid'))
model.add(Flatten())
model.add(Dense(10, activation = 'softmax'))

adam = optimizers.adam(lr = 0.01)
model.compile(loss = 'binary_crossentropy', optimizer = adam, metrics = ['accuracy'])

model.fit(x_train, real_y_train, epochs = 3)

score = model.evaluate(x_test, real_y_test)
print("This is the final output!!!")
print("\n%s:%.2f%%" % (model.metrics_names[1], score[1]*100))
