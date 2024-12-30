from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
import joblib

#查看训练数据集
digits = datasets.load_digits()
index = 1
plt.figure(figsize=(8, 6), dpi=120)
for img in digits.images[:6]:
    plt.subplot(2, 3, index)
    plt.imshow(img)
    label = digits.target[index - 1]
    plt.title('Number:%i' % label)
    index = index + 1
plt.show()

# 划分数据集
xtrain, xtest, ytrain, ytest = train_test_split(digits.data,\
    digits.target, test_size=0.2, random_state=2)

# 选取模型，训练、评估和预测
clf = svm.SVC(gamma=0.001, C=100.)
print("1.模型训练中.....")
clf.fit(xtrain, ytrain)

score = clf.score(xtest, ytest)
print("2.模型测试结果：", score)

ypred = clf.predict(xtest)
print("3.模型预测数字(显示6张图片)：", ypred[:6])

ypred = clf.predict(xtest)
print("4.图片原始数字(显示6张图片)：", ytest[:6])

# 对比预测和真实结果
fig, axes = plt.subplots(2, 3, figsize=(8, 6))
fig.subplots_adjust(hspace=0.1, wspace=0.1)
for i, ax in enumerate(axes.flat):
    ax.imshow(xtest[i].reshape(8, 8), cmap=plt.cm.gray_r,\
        interpolation='nearest')
    ax.text(0.05, 0.05, str(ypred[i]), fontsize=32, transform=\
        ax.transAxes,color='green' if ypred[i]==ytest[i] else 'red')
    ax.text(0.8, 0.05, str(ytest[i]), fontsize=32, transform=\
        ax.transAxes, color='black')
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()

# 保存模型
print("5.保存训练模型：digits_svm.pkl")
joblib.dump(clf, 'digits_svm.pkl')

# 使用保存的模型并评估模型效果
print("6.载入已有模型：digits_svm.pkl")
clf = joblib.load('digits_svm.pkl')

print("7.评估载入模型：", clf.score(xtest, ytest))
