import numpy as np
from sklearn import datasets
from sklearn import neighbors
from sklearn import linear_model
from sklearn import svm

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# split iris data in train and test data
# A random permutation, to split the data randomly
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

# # create and fit a nearest-neighbor classifier
# knn = neighbors.KNeighborsClassifier()
# knn.fit(iris_X_train, iris_y_train)

# # predict iris test data
# print knn.predict(iris_X_test)
# print iris_y_test


diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data
diabetes_y = diabetes.target

# split diabetes data in train and test data
# A random permutation, to split the data randomly
indices = np.random.permutation(len(diabetes_X))
diabetes_X_train = diabetes_X[indices[:-20]]
diabetes_y_train = diabetes_y[indices[:-20]]
diabetes_X_test = diabetes_X[indices[-20:]]
diabetes_y_test = diabetes_y[indices[-20:]]

# regr = linear_model.LinearRegression()
# regr.fit(diabetes_X_train, diabetes_y_train)

# # the mean square error and score
# print np.mean((regr.predict(diabetes_X_test)-diabetes_y_test) ** 2)
# print regr.score(diabetes_X_test, diabetes_y_test)

# alphas = np.logspace(-4, -1, 6)
# regr = linear_model.Lasso()
# scores = [regr.set_params(alpha=alpha).fit(diabetes_X_train, diabetes_y_train) \
# .score(diabetes_X_test, diabetes_y_test) for alpha in alphas]
# print scores

# logistic = linear_model.LogisticRegression()
# # clf = logistic.fit(iris_X_train, iris_y_train)
# # print clf.score(iris_X_test, iris_y_test)
# clf = logistic.fit(diabetes_X_train, diabetes_y_train)
# print clf.score(diabetes_X_test, diabetes_y_test)

svc = svm.SVC(kernel="linear")
svc.fit(iris_X_train, iris_y_train)
print svc.score(iris_X_test, iris_y_test)
# svc.fit(diabetes_X_train, diabetes_y_train)
# print svc.score(diabetes_X_test, diabetes_y_test)