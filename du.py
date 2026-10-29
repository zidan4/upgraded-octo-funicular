from sklearn.dummy import DummyClassifier

dummy_clf = DummyClassifier()
dummy_clf.fit(X_train, y_train_5)
print( any(dummy_clf.predict(X_train)) )

# prints False: no 5s detected
