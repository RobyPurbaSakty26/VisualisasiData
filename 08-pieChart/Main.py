from multiprocessing.sharedctypes import Value
from optparse import Values
from typing import ValuesView
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]


plt.pie(y, labels=mylabels)
plt.show() 