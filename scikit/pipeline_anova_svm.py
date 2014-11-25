from sklearn import svm
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import make_pipeline

# import data
X, y = samples_generator.make_classification(n_features=20,
	n_informative=3, n_redundant=0, n_classes=4, n_clusters_per_class=2)

# anova svm-c
anavo_filter = SelectKBest(f_regression, k=3)
# svm
clf = svm.SVC(kernel="linear")

anavo_svm = make_pipeline(anavo_filter, clf)
anavo_svm.fit(X, y)
print anavo_svm.predict(X)