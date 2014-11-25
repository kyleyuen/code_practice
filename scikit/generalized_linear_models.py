from sklearn import linear_model

# linear regression
# ||y - Xw||^2_2
clf = linear_model.LinearRegression()
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print clf.coef_

# ridge is based on linear regression, which imposes a penalty on the size of coefficients
# ||y - Xw||^2_2 + alpha * ||w||^2_2
clf = linear_model.Ridge(alpha=0.5)
clf.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
print clf.coef_, clf.intercept_

# lasso is based on linear regression, which estimates sparse coefficients
# (1 / (2 * n_samples)) * ||y - Xw||^2_2 + alpha * ||w||_1
clf = linear_model.Lasso(alpha=0.1)
clf.fit([[0, 0], [1, 1]], [0, 1])
print clf.coef_, clf.intercept_