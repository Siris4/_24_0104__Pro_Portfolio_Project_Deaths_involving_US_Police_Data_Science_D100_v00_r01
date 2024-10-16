import pandas as pd

# Load the CSV file
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r01\Data\police_shootings_export.csv'
df = pd.read_csv(file_path)

# Replace all NaN values with 0
df_filled = df.fillna(0)

# Save the updated DataFrame to the same location
output_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r01\Data\police_shootings_export_filled.csv'
df_filled.to_csv(output_path, index=False)

print("All NaN values have been replaced with 0 and the updated file has been saved.")
