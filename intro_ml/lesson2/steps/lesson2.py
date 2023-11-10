import pandas as pd

melbourne_file_path = '../../melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
print(melbourne_data.columns)

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)


# 1 select prediction tarjet Y 
y = melbourne_data.Price
print('\n prediction target')
print(y)

# 2 choose features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print('\n Features')
print(X)

print(y.describe())


print(X.head())
