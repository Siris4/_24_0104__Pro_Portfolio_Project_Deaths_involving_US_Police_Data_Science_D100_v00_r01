import pandas as pd

# Load the CSV file
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r00\Data\police_shootings_export.csv'
df = pd.read_csv(file_path)

# Check for duplicate rows in the DataFrame
duplicate_rows = df.duplicated()
print("Number of duplicate rows:", duplicate_rows.sum())

# Optionally, display the duplicate rows (if any)
if duplicate_rows.sum() > 0:
    print("Duplicate rows:")
    print(df[duplicate_rows])
else:
    print("No duplicate rows found.")
