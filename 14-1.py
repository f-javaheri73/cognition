
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

#1
x = 50

#2-1
np.square(x)

#2-2
np.cbrt(x)

#3
theta = 90

#4-1
np.sin(theta)

#4-2
np.cos(theta)

#4-3:
np.cos(np.radians(theta))

#4-4:
np.cos(np.degrees(theta))

#5:
meshpoints = np.linspace(-1, 1, 500)

#6
meshpoints[52]

#7
plt.plot(meshpoints,np.sin(2*np.pi*meshpoints))

plt.show()

plt.savefig('testplot.jpg')
