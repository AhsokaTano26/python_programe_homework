from matplotlib import pyplot as plt 
import numpy as np 

fig = plt.figure(figsize=(9,6))
plt.subplot2grid((3,4),(0,0),colspan=2,rowspan=2).set_title("ax0")
plt.subplot2grid((3,4),(2,0),colspan=3).set_title("ax1")
plt.subplot2grid((3,4),(2,3)).set_title("ax2")
plt.subplot2grid((3,4),(0,2),colspan=2).set_title("ax3")




plt.show()

