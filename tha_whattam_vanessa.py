## Neural Networking for healthcare

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn import metrics

#Neural Network
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

#Multiple Regression
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf

# Read in the financial data
cali_data = pd.read_table("data/calihospital_financial.txt")
# See how long it is
len(cali_data)

# For your model, create new columns in your data for lag effects of 2-periods, 3-periods, and 5-periods. (3 pts.)
# Make a copy of our response variable
d1 = cali_data.GROP_TOT

# Lag effect of 2-periods
# Add two values
lag2col = pd.Series([0, 0])
# Add back to the d1 dataframe
lag2col = pd.concat([lag2col, d1], ignore_index=True)
lag2col = lag2col.iloc[0:39,]

# Add to the original cali_data 
newcols1 = pd.DataFrame({'lag2': lag2col})
cali_data2 = pd.concat([cali_data, newcols1], axis=1)
cali_data2.head

# Lag effect of 3-periods
lag3col = pd.Series([0,0,0])
lag3col = pd.concat([lag3col, d1], ignore_index=True)
lag3col = lag3col.iloc[0:39,]

newcols2 = pd.DataFrame({'lag3': lag3col})
cali_data3 = pd.concat([cali_data2, newcols2], axis=1)

# Lag effect of 5-periods
lag5col = pd.Series([0,0,0,0,0])
lag5col = pd.concat([lag5col, d1], ignore_index=True)
lag5col = lag5col.iloc[0:39,]

newcols5 = pd.DataFrame({'lag5': lag5col})
cali_data4 = pd.concat([cali_data3, newcols5], axis=1)


# Choose the columns we need
cali_data5 = cali_data4[['QRT','GRIP_TOT','GROP_TOT',
                         'NET_TOT','TOT_OP_EXP', 'NONOP_REV', 
                         'lag2', 'lag3', 'lag5']]
cali_data5.head()

# Add a time variable
timelen = len(cali_data5.index) + 1
timecols = pd.DataFrame({'time': list(range(1,timelen))})
cali_data5 = pd.concat([cali_data5, timecols], axis=1)

# Finalized data with 3 lag effects
cali_data6 = cali_data5[['GROP_TOT','time','lag2', 'lag3', 'lag5']]

# * Create training and testing data. (2 pts.)

# Split 70% of the data into train and 30% into test
splitnum = np.round((len(cali_data6.index) * 0.7), 0).astype(int)
splitnum

# Assign records 0-27 as train, and 28-39 as test
cali_train = cali_data6.iloc[0:27,]
cali_test = cali_data6.iloc[28:39,]

# * For your model, create three ANN models and compare the error scores. (3 pts.)

# Create the first model
grop_ann1 = MLPRegressor(activation='relu', solver='sgd')
grop_ann1.fit(cali_train[['time','lag2','lag5']], cali_train.GROP_TOT)

grop_ann1_pred = grop_ann1.predict(cali_test[['time','lag2','lag5']])


# Create the second model
grop_ann2 = MLPRegressor(activation='logistic', solver='sgd')
grop_ann2.fit(cali_train[['time','lag2','lag5']], cali_train.GROP_TOT)

grop_ann2_pred = grop_ann2.predict(cali_test[['time','lag2','lag5']])


# Create the third model
grop_ann3 = MLPRegressor(activation='relu', solver='sgd')
grop_ann3.fit(cali_train[['time','lag2','lag3', 'lag5']], cali_train.GROP_TOT)

grop_ann3_pred = grop_ann3.predict(cali_test[['time','lag2','lag3', 'lag5']])

# Error scores
# Model 1 metrics
metrics.mean_absolute_error(cali_test.GROP_TOT, grop_ann1_pred)
metrics.mean_squared_error(cali_test.GROP_TOT, grop_ann1_pred)

# Model 2 metrics
metrics.mean_absolute_error(cali_test.GROP_TOT, grop_ann2_pred)
metrics.mean_squared_error(cali_test.GROP_TOT, grop_ann2_pred)

# Model 3 metrics
metrics.mean_absolute_error(cali_test.GROP_TOT, grop_ann3_pred)
metrics.mean_squared_error(cali_test.GROP_TOT, grop_ann3_pred)

# * Which ones perform better and why? (2 pts.)
