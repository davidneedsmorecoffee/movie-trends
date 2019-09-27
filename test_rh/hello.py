print("Hello World!")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy import stats
from scipy.stats import linregress

test1 = [1,5,10,15,20]
test2 = [25,50,75,100]

plt.scatter(test1,test2,edgecolors="black",facecolors="blue")
plt.grid (b=True,which="major",axis="both",linestyle="-",color="lightgrey")
plt.title("City Latitude vs. Max Temperature (09/24/2019)")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")
plt.show()