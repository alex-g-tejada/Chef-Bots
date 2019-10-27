#************************************************************************************
# Armando Gallegos
# Senior design Topping Identifcation ML
# Filename: fastest_R_CNN
#
# Objective:
#*************************************************************************************

# all double ## comments are self inserted test hooks in order to see progress 
# and debug if need by.

# importing libaries 
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import patches

train = pd.read_csv('lettuce.csv')

train.head()

print (train)

image = plt.imread('lettuce/1.jpg')
plt.imshow(image)
