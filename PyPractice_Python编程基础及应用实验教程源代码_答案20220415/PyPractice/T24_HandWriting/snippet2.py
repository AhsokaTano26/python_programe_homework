from sklearn import datasets
from sklearn.model_selection import train_test_split
digits = datasets.load_digits()
xtrain,xtest,ytrain,ytest = train_test_split(digits.data,\
    digits.target,test_size=0.2,random_state=2)
print(xtrain.shape,ytrain.shape)
print(xtest.shape,ytest.shape)

from sklearn import svm 
clf=svm.SVC(gamma=0.001,C=100.) 
print("training .....") 
clf.fit(xtrain,ytrain) 
print("testing .....") 
score=clf.score(xtest,ytest) 
print(score) 

ypred = clf.predict(xtest)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(4, 4, figsize=(8, 8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)
for i, ax in enumerate(axes.flat):
    ax.imshow(xtest[i].reshape(8, 8), cmap=plt.cm.gray_r, \
        interpolation='nearest')
    ax.text(0.05, 0.05, str(ypred[i]), fontsize=32,transform= \
        ax.transAxes,color='green' if ypred[i] == ytest[i] else 'red')
    ax.text(0.8, 0.05, str(ytest[i]), fontsize=32 ,transform= \
        ax.transAxes,color='black')
    ax.set_xticks([])     
    ax.set_yticks([])
plt.show()

import joblib
joblib.dump(clf, 'digits_svm.pkl')



