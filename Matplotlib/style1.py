import matplotlib.pyplot as plt
import scipy.linalg as alg
import numpy as np

import matplotlib as mpl
import sys
import sklearn.linear_model as linear_model
from sklearn.datasets import load_boston
import time
import pandas as pd

def myPlotter(ax,xdata,ydata,param_dict):
	'''

	:param ax: Axes
		The axes to Draw to

	:param xdata: The X data

	:param ydata: The Y data

	:param param_dict: Parameter Dictionary
		Dictionary of **kwargs to pass to ax.plot()
	:return:
		out : list of artists added
	'''

	out = ax.plot(xdata,ydata,**param_dict)
	ax.legend()
	return out

housing_dataset = load_boston()

fig, ax_list= plt.subplots(1,1)
myPlotter(ax_list,np.array([housing_dataset.data[i][5] for i in range(506)]),housing_dataset.target,{'marker':'x', 'label':'Housing Data'})
plt.show()
