import matplotlib.pyplot as plt
import numpy as np
dotcount = 100
X = np.linspace(0, 2*np.pi, dotcount)
Y = np.sin(X)+0.2*np.random.rand(dotcount)-0.1
plt.scatter(X,Y,c='r')
plt.show()
