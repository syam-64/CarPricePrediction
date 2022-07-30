# -*- coding: utf-8 -*-
"""Car Price Prediction Using Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sCFTE-jcyFhktOX-hfzQFhV6JnAhfM60

Importing the necessary libraries
"""

import pandas as pd # for data frames such as structured tabular forms
import numpy as np #for mathematical calculation
import matplotlib.pyplot as plt #for data visualization such as ploting
import seaborn as sns #for making statistical graphics
import warnings #for ignoring the warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split # used to split data into training data and test data
from sklearn.linear_model import LinearRegression #importing LinearRegression
from sklearn import metrics #used for calculation the accuracy and error percentage

"""Data Collection and Processing"""

# loading the data from csv file to pandas dataframe
car_dataset = pd.read_csv('/content/CAR DETAILS FROM CAR DEKHO.csv')

# inspecting the first 20 rows of the dataframe
car_dataset.head()

# checking the number of rows and columns
car_dataset.shape

# getting some information about the dataset
car_dataset.info()

# checking the number of missing values
car_dataset.isnull().sum()

car_dataset['Age'] = 2022 - car_dataset['year']
car_dataset.drop('year',axis=1,inplace = True)

# checking the distribution of categorical data
print(car_dataset.fuel.value_counts()) # checking the number of fuel types
print(car_dataset.seller_type.value_counts()) # checking seller type
print(car_dataset.transmission.value_counts()) # chekicng transmission type
print(car_dataset.Age.value_counts()) # chekicng Age

cat_col = ['fuel','seller_type','transmission','owner']
i=0
while i < 4:
    fig = plt.figure(figsize=[15,5])
 
    plt.subplot(1,2,1)
    sns.countplot(x=cat_col[i], data=car_dataset,palette='spring')
    i += 1
    
    plt.subplot(1,2,2)
    sns.countplot(x=cat_col[i], data=car_dataset,palette='spring')
    i += 1
    
    plt.show()

"""Encoding the Categorical Data"""

# encoding "fuel" Column
car_dataset.replace({'fuel':{'Petrol':0,'Diesel':1,'CNG':2,'LPG':3,'Electric':4}},inplace=True)

# encoding "seller_type" Column
car_dataset.replace({'seller_type':{'Dealer':0,'Individual':1,'Trustmark Dealer':2}},inplace=True)

# encoding "transmission" Column
car_dataset.replace({'transmission':{'Manual':0,'Automatic':1}},inplace=True)

# encoding "owner" Column
car_dataset.replace({'transmission':{'Manual':0,'Automatic':1}},inplace=True)

# encoding "door number" Column
car_dataset.replace({'doornumber':{'two':0,'four':1}},inplace=True)

car_dataset.drop('owner',axis=1,inplace = True)

np.random.seed(0)
df_train, df_test = train_test_split(car_dataset, train_size = 0.7, test_size = 0.3, random_state = 100)
car_dataset

car_dataset.head()

sig_num_col = ['wheelbase','carlength','carwidth','curbweight','enginesize','boreratio','horsepower','citympg','highwaympg',]

scaler = preprocessing.StandardScaler()
car_dataset.head()

import warnings
warnings.filterwarnings("ignore")

car_dataset[sig_num_col] = scaler.fit_transform(car_dataset[sig_num_col])
car_dataset

"""Splitting the data and Target"""

X = car_dataset.drop(['name','selling_price'],axis=1)
Y = car_dataset['selling_price']

print(X)

print(Y)

"""Splitting Training and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.9, test_size = 0.1, random_state = 2)

"""Model Training"""

# loading the linear regression model
lin_reg_model = LinearRegression()

lin_reg_model.fit(X_train,Y_train)

# prediction on Training data
training_data_prediction = lin_reg_model.predict(X_train)

# R squared Error
error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error in training : ", error_score)

"""Visualize the actual prices and Predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

# prediction on Training data
test_data_prediction = lin_reg_model.predict(X_test)

# R squared Error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error in test: ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

"""Model Evaluation"""