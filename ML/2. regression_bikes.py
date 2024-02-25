import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import copy
import seaborn as sns # seaborn is a wrapper over matplotlib
import tensorflow as tf
from sklearn.linear_model import LinearRegression

# SUPERVISED LEARNING

dataset_cols = ["bike_count", "hour", "temp", "humidity", "wind", "visibility", "dew_pt_temp", "radiation", "rain", "snow", "functional"]
df = pd.read_csv("SeoulBikeData.csv", encoding='latin1').drop(["Date", "Holiday", "Seasons"], axis=1)

#print(df.head())

df.columns = dataset_cols
#print(df.head())

df['functional'] = (df['functional'] == 'Yes').astype(int)
df = df[df['hour'] == 12]
df = df.drop(['hour'], axis = 1)

print(df.head())

# for label in df.columns[1: ]:
#     plt.scatter(df[label], df['bike_count'])
#     plt.title(label)
#     plt.ylabel('Bike Count at Noon')
#     plt.xlabel(label)
#     plt.show()

df = df.drop(['wind', 'visibility', 'functional'], axis = 1)

# TRAIN/VALID/TEST DATASET

train, valid, test = np.split(df.sample(frac = 1), [int(0.6 * len(df)), int(0.8 * len(df))])

def get_xy(dataframe, y_label, x_labels = None):  # x_labels is optional and defaults to none
    dataframe = copy.deepcopy(dataframe)  # make a copy ensuring not affecting the original dataframe
    
    if x_labels is None:  # use all the columns of the df except for thr target avriable features
        X = dataframe([c for c in dataframe.columns if c!= y_label]).values # create a matrix by selecting all columns, then convert them to a numpy array using .values
    else:
        if len(x_labels) == 1:  # if there's only one feature, select it and reshape it 
            X = dataframe[x_labels[0]].values.reshape(-1, 1)  # make this 2D
        else:  # if multiple features, select those to be 2D with a single column, to prepare for horizontal stacking 
            X = dataframe[x_labels].values # remove the unnecessary reshape

    y = dataframe[y_label].values.reshape(-1, 1)
    data = np.hstack((X, y)) # contains both features and the target variable

    return data, X, y


_, X_train_temp, y_train_temp = get_xy(train, "bike_count", x_labels=["temp"])
_, X_val_temp, y_val_temp = get_xy(valid, "bike_count", x_labels=["temp"])
_, X_test_temp, y_test_temp = get_xy(test, "bike_count", x_labels=["temp"])
#print(X_train_temp)

temp_reg = LinearRegression()
temp_reg.fit(X_train_temp, y_train_temp)

#print(temp_reg.coef_, temp_reg.intercept_)
#print(temp_reg.score(X_test_temp, y_test_temp)) # 0.34 -- better than 0; the higher the number, the higher the chance the 2 var would be correlated

plt.scatter(X_train_temp, y_train_temp, label="Data", color="blue")
x = tf.linspace(-20, 40, 100)
x_values = np.array(x) # convert tensorflow to numpy array
plt.plot(x_values, temp_reg.predict(x_values.reshape(-1, 1)), label="Fit", color="red", linewidth=3)
plt.legend()
plt.title("Bikes vs Temp")
plt.ylabel("Number of bikes")
plt.xlabel("Temp")
#plt.show()

### MULTIPLE LINEAR REGRESSION

_, X_train_all, y_train_all = get_xy(train, "bike_count", x_labels=df.columns[1:]) # remove the bikecount
_, X_val_all, y_val_all = get_xy(valid, "bike_count", x_labels=df.columns[1:])
_, X_test_all, y_test_all = get_xy(test, "bike_count", x_labels=df.columns[1:])

all_reg = LinearRegression()
all_reg.fit(X_train_all, y_train_all)

print(all_reg.score(X_test_all, y_test_all)) # this is improved 