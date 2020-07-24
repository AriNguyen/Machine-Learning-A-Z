#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import libraries

import numpy as np  #  contains math tools
import matplotlib.pyplot as plt  # plot nice chart
import pandas as pd  # import dataset and manage dataset

# Import dataset
dataset = pd.read_csv('Data.csv')
#       first colon take all the line
#       :-1 take all the columns except the last one
#       .values take  all the values
#       => create matrix of independent variables
X = dataset.iloc[:, :-1].values  
#       create independent vector
y = dataset.iloc[:, 3].values

# Taking care of Mising data
#       sklearn: library to make machine model
#       preprocessing: contains classes/methods to prepocess data
#       import Imputer class: to take care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
#       fit the imputer objct to matrix of feature X
imputer = imputer.fit(X[:, 1:3])
#       transform: replace missing data with missing value
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding Categorial data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#       fit labelencoder_X to the first colimn Country of our matrix X
#       return the first column encoded
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
#       Dummy variables
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting dataset into Trainings Set and Test set
# X_train: training part of the matrix X
# X_test: testing part 
# y_train: training part of dependent variable that associated to X_train
# y_test: testing part of dependent vector  
# test_size = 0.5: half of data go to train, half go to test
# 0.2: 2 observations in test set, 8 in training set  
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler 
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)












