import joblib
mind = joblib.load("marks secured.pk1")
mind.predict([[2]])
