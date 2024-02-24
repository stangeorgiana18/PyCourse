import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

# SUPERVISED LEARNING 

cols = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fM4Long', 'fM3Trans', 'fAlpha', 'fDist', 'class']
df = pd.read_csv("magic04.data", names = cols)
print(df.head) # attached the labels to the columns 

#print(df['class'].unique())

# convert 0 for g, 1 for h
df['class'] = (df['class'] == 'g').astype(int)

#print(df.head())

for label in cols[ :-1]:
    plt.hist(df[df['class'] == 1][label], color = 'blue', label = 'gamma', alpha = 0.7, density = True) # all the diff values that belong to class 1 for a specific label
    plt.hist(df[df['class'] == 0][label], color = 'red', label = 'hadron', alpha = 0.7, density = True) # density = True normalizes the distributions; distribute over how many samples there are
    plt.title(label)
    plt.ylabel('Probability')
    plt.xlabel(label)
    plt.legend()
    #plt.show()


#### TRAIN, VALIDATION, TEST DATASETS

# frac = 1 --> shuffle 
# 60-80% - training
# 80-100% - validation 
# remaining portion - test 
df.reset_index(drop = True, inplace = True) # reset the index of the DataFrame before splitting bcs of previous keyerror
train, valid, test = np.split(df.sample(frac = 1), [int(0.6 * len(df)), int(0.8 * len(df))])


def scale_dataset(dataframe, oversample = False):
    x = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    # scale the values - to be relative to the mean and the standard deviation of that column
    scaler = StandardScaler()
    X = scaler.fit_transform(x)
    
    # oversample our training data set - increase the number of these values so they match better
    # increase the size of our dataset of the smaller class so they match
    if oversample:
        ros = RandomOverSampler()
        X, y = ros.fit_resample(X, y)

    # X - 2 dim; y - 1 dim --> reshape y into a 2D item
    # np.reshape(y, (len(y), 1)) the same as below
    data = np.hstack((X, np.reshape(y, (-1, 1)))) # horizontally stacke the arrays together; side by side, not on top of each other
    
    return data, X, y

#print(len(train[train['class'] == 1]))  # gamma ~7000
#print(len(train[train['class'] == 0]))  # hadron ~4000

train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
test, X_test, y_test = scale_dataset(test, oversample=False)

#print(len(y_train))
#print(sum(y_train == 1)) # 7416
#print(sum(y_train == 0)) # 7416

########
#### KNN
########

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn_model = KNeighborsClassifier(n_neighbors = 3)
knn_model.fit(X_train, y_train)

y_pred = knn_model.predict(X_test)

print(classification_report(y_test, y_pred))

###############
### NAIVE BAYES 
###############

from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model = nb_model.fit(X_train, y_train)

y_pred = nb_model.predict(X_test)

print(classification_report(y_test, y_pred)) # lower scores than in the knn model

#######################
### LOGISTIC REGRESSION
#######################

from sklearn.linear_model import LogisticRegression

lg_model = LogisticRegression() # we can use different penalties 
lg_model = lg_model.fit(X_train, y_train)

y_pred = lg_model.predict(X_test)

print(classification_report(y_test, y_pred)) # performed better than NB but not better than knn

#######
### SVM
#######

from sklearn.svm import SVC # support vector classifier

svm_model = SVC()
svm_model = svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

print(classification_report(y_test, y_pred)) # the best accuracy so far 

####################
#### NEURAL NETWORKS
####################

import tensorflow as tf

def train_model(X_train, y_train, num_nodes, dropout_prob, learning_r, batch_size, epochs):
    nn_model = tf.keras.Sequential([
        tf.keras.layers.Dense(num_nodes, activation='relu', input_shape = (9, )),
        tf.keras.layers.Dropout(dropout_prob), # randomly choose at this rate certain nodes and don't train them -- prevents overfitting
        tf.keras.layers.Dense(num_nodes, activation='relu'),
        tf.keras.layers.Dropout(dropout_prob), # probability of turning off a node during the training 
        tf.keras.layers.Dense(1, activation='sigmoid') # the output layers - projectiv our predictions to be 0/1
    ])

    nn_model.compile(optimizer = tf.keras.optimizers.legacy.Adam(learning_r), loss = 'binary_crossentropy', metrics = ['accuracy'])

    history = nn_model.fit(
        X_train, y_train, epochs = epochs, batch_size = batch_size, validation_split = 0.2, verbose = 0   # verbose = 0 --> don't print anything

    )

    return nn_model, history 


# plot the loss and accuracy over all the different epochs (training cycles)
def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Binary crossentropy')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_accuracy(history):
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()

#print(X_train.shape)

#plot_loss(history)
#plot_accuracy(history)

epochs = 100

least_val_loss = float('inf') # record if the model has a validation loss
least_loss_model = None # keep track of the model

for num_nodes in [16, 32, 64]:
    for dropout_prob in [0, 0.2]:
        for learning_r in [0.01, 0.005, 0.001]:
            for batch_size in [32, 64, 128]:  # number of samples to work through before updating the model's internal parameters (weights and biases)
                print(f"{num_nodes} nodes, dropout {dropout_prob}, lr {learning_r}, batch size {batch_size}")
                model, history = train_model(X_train, y_train, num_nodes, dropout_prob, learning_r, batch_size, epochs)
                
                #plot_loss(history)
                #plot_accuracy(history)

                validation_loss = model.evaluate(X_valid, y_valid)[0]
                
                if validation_loss < least_val_loss:
                    least_val_loss = validation_loss
                    least_loss_model = model

# PREDICT
                    
y_pred = least_loss_model.predict(X_test) # values close to 0 and 1, so cast them:
y_pred = (y_pred > 0.5).astype(int).reshape(-1, )
print(y_pred)
print(classification_report(y_test, y_pred)) # performed similar to the svm model

