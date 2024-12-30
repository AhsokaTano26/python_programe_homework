from sklearn import datasets
import matplotlib.pyplot as plt
digits = datasets.load_digits()
index = 1
plt.figure(figsize=(8, 8), dpi=120)
for img in digits.images[:12]:
    plt.subplot(3, 4, index)
    plt.imshow(img)
    label = digits.target[index - 1]
    plt.title('Number:%i' % label)
    index = index + 1
plt.show()




