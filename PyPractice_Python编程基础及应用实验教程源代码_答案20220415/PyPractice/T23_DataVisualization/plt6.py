import matplotlib.pyplot as plt

data = [5, 25, 50, 20]
plt.subplot(121)
plt.pie(data)

data = [5, 35, 40, 20]
explode = [0.05,0.05,0.05,0.05]
labels = ['banana','apple','orange','grape']
plt.subplot(122)
plt.pie(data,explode=explode,labels=labels)
plt.show()
