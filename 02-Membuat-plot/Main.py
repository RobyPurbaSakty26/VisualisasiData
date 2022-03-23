import numpy as np
import matplotlib.pyplot as plt

# mambuat data
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([1,16,81,256,625])


# mambuat plot
plt.plot(x,y, '-o')
plt.plot(x,y2, 'r-o')

# manampikan plot
plt.show()