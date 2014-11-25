from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib
import pylab as pl

# load digits data
digits = datasets.load_digits()
# clf = svm.SVC(gamma=0.001, C=100)

# clf.fit(digits.data, digits.target)
# for i in range(len(digits.data)):
# 	result = clf.predict(digits.data[i])
# 	print digits.target  [i], result

# joblib.dump(clf, "svm.pkl")
# clf = joblib.load("svm.pkl")
# print clf

data = digits.images.reshape(digits.images.shape[0], -1)
print data.shape