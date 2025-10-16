import numpy as np
import matplotlib.pyplot as plt
x=np.random.randn(1000)
y = 2*x+10
l= np.linspace(0,100,100)
k= np.percentile(y,l)
plt.scatter(l,k)
plt.show()
