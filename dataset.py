# -*- coding: utf-8 -*-
"""dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c5miGQgINaxLm1W7DqlRKcIiwclnlA3Y
"""

pip install keras

pip install tensorflow

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
import random

import pickle
pickle_in=open("/content/drive/MyDrive/X_train.pickle","rb")
X_train=pickle.load(pickle_in)

pickle_in=open("/content/drive/MyDrive/y_train.pickle","rb")
y_train=pickle.load(pickle_in)

X_train.shape

y_train.shape





num_of_samples=[]
cols=5
num_classes=10
fig,axs=plt.subplots(nrows=num_classes,ncols=cols,figsize=(5,8))
fig.tight_layout()

for i in range(cols):
  for j in range(num_classes):
    x_selected=X_train[y_train==j]
    axs[j][i].imshow(x_selected[random.randint(0,len(x_selected-1)),:,:],cmap=plt.get_cmap("gray"))
    axs[j][i].axis("off")
    if i==2:
      axs[j][i].set_title(str(j))
      num_of_samples.append(len(x_selected))

def leNet_model():
  model=Sequential()
  model.add(Conv2D(30,(5,5),input_shape=(28,28,1), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2,2)))
  
  model.add(Conv2D(15,(3,3),activation='relu'))
  model.add(MaxPooling2D(pool_size=(2,2)))
  
  model.add(Flatten())
  
  model.add(Dense(500,activation='relu'))
  model.add(Dense(num_classes,activation='softmax'))
  model.compile(Adam(lr=0.01),loss='categorical_crossentropy',metrics=['accuracy'])
  return model

model=leNet_model()
print(model.summary())

model.fit(X_train,y_train,validation_split=0.1,epochs=10,batch_size=400,verbose=1,shuffle=1)

