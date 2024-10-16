import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file with high school graduation data
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r01\Data\Pct_Over_25_Completed_High_School.csv'
df_hs = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert the high school completion rate to numeric values
df_hs['percent_completed_hs'] = pd.to_numeric(df_hs['percent_completed_hs'], errors='coerce')

# Group by state and calculate the mean high school completion rate for each state
df_state_hs = df_hs.groupby('Geographic Area')['percent_completed_hs'].mean().reset_index()

# Sort the data by high school completion rate in ascending order
df_state_hs = df_state_hs.sort_values(by='percent_completed_hs', ascending=True)

# Display the state with the lowest and highest graduation rates
lowest_hs_state = df_state_hs.iloc[0]
highest_hs_state = df_state_hs.iloc[-1]

print(f"State with the lowest high school graduation rate: {lowest_hs_state['Geographic Area']}, {lowest_hs_state['percent_completed_hs']:.2f}%")
print(f"State with the highest high school graduation rate: {highest_hs_state['Geographic Area']}, {highest_hs_state['percent_completed_hs']:.2f}%")

# Create a bar chart using matplotlib to show the graduation rate in ascending order
plt.figure(figsize=(10, 8))
plt.barh(df_state_hs['Geographic Area'], df_state_hs['percent_completed_hs'], color='lightgreen')
plt.xlabel('High School Graduation Rate (%)')
plt.ylabel('State')
plt.title('High School Graduation Rate by US State (Lowest to Highest)')
plt.tight_layout()
plt.show()
