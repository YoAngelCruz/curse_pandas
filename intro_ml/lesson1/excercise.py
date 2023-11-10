import pandas as pd

# ----1-----
# Path of the file to read
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)

print(home_data)