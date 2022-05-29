from tkinter import X
import pandas as pd
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('data/auto-mpg.csv', sep=";")
print(data)

data = data.sample(frac=1)

y_variable = data['mpg']

x_variables = data.loc[:, data.columns != 'mpg']


x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=test_size, random_state=seed)
regressor = LinearRegression()
regressor = regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

file_to_write = open('data/models/SKlearnMethode_lr.pickle', "wb")
pickle.dump(regressor, file_to_write)



