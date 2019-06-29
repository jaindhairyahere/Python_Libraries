import matplotlib.pyplot as plt
import scipy.linalg as alg
import numpy as np

import sys
import sklearn.linear_model as linear_model
from sklearn.datasets import load_boston
import time
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
#Reading data into matrices X	, y

a = load_boston()
print(a.data.shape)
print(a.target.shape)
X = pd.DataFrame(a.data)
print(X)
y = pd.Series(a.target)
print(y)

plt.ion()
fig = plt.figure()
fig.suptitle("No axes declared till now")

fig , ax_list = plt.subplots(2,2)

# for i in range(len(ax_list)):
# 	plt.gca(ax_list[i])
# 	x = np.array([j for j in range(5) ])
# 	y = np.array([(j+2)**i for j in range(5) ])
# 	plt.plot(x,y)
plt.show()
time.sleep(5)
plt.close()
