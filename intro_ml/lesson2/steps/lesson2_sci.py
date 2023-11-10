from sklearn.tree import DecisionTreeRegressor
import pandas as pd

melbourne_file_path = '../../melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)


melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
print('\n prediction target')
print(y)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print('\n Features')
(X)

print(y.describe())


print(X.head())

#-------------------------------

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
print(melbourne_model.fit(X, y))


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))