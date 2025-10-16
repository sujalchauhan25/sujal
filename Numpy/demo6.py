import numpy as np
import matplotlib.pyplot as plt 
theta = np.linspace(0,2*np.pi,1000)
r = 2 + np.sin(5*theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.plot(x,y)
plt.show()