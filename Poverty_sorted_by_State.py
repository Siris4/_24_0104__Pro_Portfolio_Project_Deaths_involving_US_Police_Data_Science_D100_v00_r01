import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file with poverty data
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r01\Data\Pct_People_Below_Poverty_Level.csv'
df_poverty = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert the poverty_rate column to numeric values
df_poverty['poverty_rate'] = pd.to_numeric(df_poverty['poverty_rate'], errors='coerce')

# Group by state and calculate the mean poverty rate for each state
df_state_poverty = df_poverty.groupby('Geographic Area')['poverty_rate'].mean().reset_index()

# Sort the data by poverty rate in descending order
df_state_poverty = df_state_poverty.sort_values(by='poverty_rate', ascending=False)

# Create a bar chart using matplotlib
plt.figure(figsize=(10, 8))
plt.barh(df_state_poverty['Geographic Area'], df_state_poverty['poverty_rate'], color='skyblue')
plt.xlabel('Poverty Rate (%)')
plt.ylabel('State')
plt.title('Poverty Rate by US State (Highest to Lowest)')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest rate on top
plt.tight_layout()
plt.show()
