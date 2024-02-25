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

# plt.scatter(X_train_temp, y_train_temp, label="Data", color="blue")
# x = tf.linspace(-20, 40, 100)
# x_values = np.array(x) # convert tensorflow to numpy array
# plt.plot(x_values, temp_reg.predict(x_values.reshape(-1, 1)), label="Fit", color="red", linewidth=3)
# plt.legend()
# plt.title("Bikes vs Temp")
# plt.ylabel("Number of bikes")
# plt.xlabel("Temp")
# plt.show()

### MULTIPLE LINEAR REGRESSION

_, X_train_all, y_train_all = get_xy(train, "bike_count", x_labels=df.columns[1:]) # remove the bikecount
_, X_val_all, y_val_all = get_xy(valid, "bike_count", x_labels=df.columns[1:])
_, X_test_all, y_test_all = get_xy(test, "bike_count", x_labels=df.columns[1:])

all_reg = LinearRegression()
all_reg.fit(X_train_all, y_train_all)

#print(all_reg.score(X_test_all, y_test_all)) # this is improved 

# Regression with Neural Net

def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('MSE')
    plt.legend()
    plt.grid(True)
    plt.show()

temp_normalizer = tf.keras.layers.Normalization(input_shape = (1, ), axis = None)
temp_normalizer.adapt(X_train_temp.reshape(-1))

temp_nn_model = tf.keras.Sequential([
    temp_normalizer, 
    tf.keras.layers.Dense(1) # one single dense layer with 1 single unit 
])

temp_nn_model.compile(optimizer = tf.keras.optimizers.legacy.Adam(learning_rate = 0.1), loss = 'mean_squared_error')
history = temp_nn_model.fit(
    X_train_temp.reshape(-1), y_train_temp,
    verbose = 0,
    epochs = 1000,
    validation_data = (X_val_temp, y_val_temp)
)

#plot_loss(history) # values are converging 

# here using backpropagation to train a neural node
# plt.scatter(X_train_temp, y_train_temp, label="Data", color="blue")
# x = tf.linspace(-20, 40, 100)
# plt.plot(x, temp_reg.predict(np.array(x).reshape(-1, 1)), label="Fit", color="red", linewidth=3)
# plt.legend()
# plt.title("Bikes vs Temp")
# plt.ylabel("Number of bikes")
# plt.xlabel("Temp")
# plt.show()

# ### NEURAL NET

temp_normalizer = tf.keras.layers.Normalization(input_shape=(1,), axis=None)
temp_normalizer.adapt(X_train_temp.reshape(-1))

nn_model = tf.keras.Sequential([
    temp_normalizer,
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='relu'),  # final output - one answer/cell, relu = 1 because we cannot have less than 0 bikes
])

nn_model.compile(optimizer = tf.keras.optimizers.legacy.Adam(learning_rate = 0.001), loss = 'mean_squared_error')

history = nn_model.fit(
    X_train_temp, y_train_temp,
    validation_data = (X_val_temp, y_val_temp),
    verbose = 0, epochs = 100
)

#plot_loss(history)

# plt.scatter(X_train_temp, y_train_temp, label="Data", color="blue")
# x = tf.linspace(-20, 40, 100)
# plt.plot(x, nn_model.predict(np.array(x).reshape(-1, 1)), label="Fit", color="red", linewidth=3)
# plt.legend()
# plt.title("Bikes vs Temp")
# plt.ylabel("Number of bikes")
# plt.xlabel("Temp")
# plt.show()

all_normalizer = tf.keras.layers.Normalization(input_shape=(6,), axis=-1)
all_normalizer.adapt(X_train_all)

nn_model = tf.keras.Sequential([
    all_normalizer,
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

nn_model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.001), loss='mean_squared_error')

history = nn_model.fit(
    X_train_all, y_train_all,
    validation_data = (X_val_all, y_val_all),
    verbose = 0, epochs = 100
)

#plot_loss(history) # curves decreasing 

# print(all_reg.score(X_test_all, y_test_all))
# print(all_reg.predict(X_test_all))

# calculate the MSE for both linear reg and nn
y_pred_lr = all_reg.predict(X_test_all)
y_pred_nn = nn_model.predict(X_test_all)

def MSE(y_pred, y_real):
      return (np.square(y_pred - y_real)).mean()

# print(MSE(y_pred_lr, y_test_all))
# print(MSE(y_pred_nn, y_test_all)) # nn results have a larger mse the lr 

# plot the real results vs the predictions

ax = plt.axes(aspect = 'equal')
plt.scatter(y_test_all, y_pred_lr, label = 'Lin Reg Preds')
plt.scatter(y_test_all, y_pred_nn, label = 'NN Preds')
plt.xlabel('True Values')
plt.ylabel("Predictions")
lims = [0, 1800]
plt.xlim(lims)
plt.ylim(lims)
plt.legend()
_ = plt.plot(lims, lims, c = 'red')
plt.show()

# notice that for the nn, for the larger values, it seems more spread out 
# and we tend to underestimate in the area below the diag

 