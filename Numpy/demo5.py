import numpy as np
import matplotlib.pyplot as plt
a1 = np.random.randn(1000)
k = np.linspace(0,100,100)
print(type(k))
l = np.percentile(a1,k )