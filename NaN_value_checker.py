import pandas as pd

# Load the CSV file
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r00\Data\police_shootings_export.csv'
df = pd.read_csv(file_path)

# Check for NaN values in each column
nan_values = df.isna().sum()
print("Number of NaN values in each column:")
print(nan_values)

# Optionally, display rows with NaN values
print("\nRows with NaN values:")
print(df[df.isna().any(axis=1)])
