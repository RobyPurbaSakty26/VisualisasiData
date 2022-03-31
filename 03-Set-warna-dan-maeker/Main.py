import numpy as np
import matplotlib.pyplot as plt

# mabuat data
def sinusGenerator(amplitudo, frekuensi, waktu, thetha):
    t = np.arange(0,waktu,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(thetha))
    return t,y

# membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1, y1, 'y')

t2, y2 =sinusGenerator(1,1,4,30)
plt.plot(t2, y2, 'r')

t3, y3 = sinusGenerator(1,1,4,60)
plt.plot(t3, y3, 'b--')

t4, y4 = sinusGenerator(1,1,4,90)
plt.plot(t4, y4, 'b-o')

# manampilkan plot
plt.grid()
plt.show()
