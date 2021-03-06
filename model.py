# Dependencies
from neuralpy.models import Sequential
from neuralpy.layers import Dense
from neuralpy.regularizers import Dropout
from neuralpy.activation_functions import ReLU
from neuralpy.loss_functions import CrossEntropyLoss
from neuralpy.optimizer import Adam

import pandas as pd
import numpy as np

# Model
model = Sequential()

model.add(Dense(n_nodes=64, n_inputs=784))
model.add(ReLU())

model.add(Dropout())

model.add(Dense(n_nodes=10))

model.build()

model.compile(optimizer=Adam(learning_rate=0.001, betas=(0.9, 0.999), eps=1e-08,
                             weight_decay=0.0, amsgrad=False), loss_function=CrossEntropyLoss(), metrics=["accuracy"])

print(model.summary())

# Reading data
train_data = pd.read_csv("./data/mnist_train.csv")
test_data = pd.read_csv("./data/mnist_test.csv")

train_data = train_data.sample(frac=1)
train_data = train_data.values

test_data = test_data.sample(frac=1)
test_data = test_data.values

X = train_data[:, 1:] / 255.
y = train_data[:, 0]

X_test = test_data[:, 1:]
y_test = test_data[:, 0]

del train_data

n = len(X)

X_train = X[:int(n*0.8)]
y_train = y[:int(n*0.8)]

X_validation = X[int(n*0.8):]
y_validation = y[int(n*0.8):]

del X, y

model.fit(train_data=(X_train, y_train), validation_data=(
    X_validation, y_validation), epochs=5, batch_size=32)

ev = model.evaluate(X=X_test, y=y_test, batch_size=32)

print(ev)
