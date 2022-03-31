import matplotlib_inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,100)




plt.plot(x, x, label ='linear')
plt.plot(x, x**2, label = 'quadrat')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y labal')
plt.title('Siple Plot')
plt.legend()
plt.show()