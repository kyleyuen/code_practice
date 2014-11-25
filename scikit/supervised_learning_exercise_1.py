from sklearn import datasets
from sklearn import neighbors
from sklearn import linear_model
import numpy as np

digits = datasets.load_digits()
digits_X = digits.data
digits_y = digits.target

n_samples = len(digits_X)
indices = np.random.permutation(n_samples)
digits_X_train = digits_X[indices[:0.9*n_samples]]
digits_y_train = digits_y[indices[:0.9*n_samples]]
digits_X_test = digits_X[indices[0.9*n_samples:]]
digits_y_test = digits_y[indices[0.9*n_samples:]]

knn = neighbors.KNeighborsClassifier()
knn.fit(digits_X_train, digits_y_train)
# print knn.predict(digits_X_test), digits_y_test
print knn.score(digits_X_test, digits_y_test)

regr = linear_model.LogisticRegression()
regr.fit(digits_X_train, digits_y_train)
print regr.score(digits_X_test, digits_y_test)