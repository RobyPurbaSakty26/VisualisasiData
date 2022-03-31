
import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
sudut = np.linspace(0,2*PI,100)
radius =5;
x = radius * np.cos(sudut)
y = radius * np.sin(sudut)


plt.plot(x,y, '-o')
plt.show()