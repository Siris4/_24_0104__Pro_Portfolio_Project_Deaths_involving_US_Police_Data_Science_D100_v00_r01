import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files for high school graduation rates and poverty rates
file_path_hs = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r01\Data\Pct_Over_25_Completed_High_School.csv'
file_path_poverty = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r01\Data\Pct_People_Below_Poverty_Level.csv'

# Load the data
df_hs = pd.read_csv(file_path_hs, encoding='ISO-8859-1')
df_poverty = pd.read_csv(file_path_poverty, encoding='ISO-8859-1')

# Convert the high school completion rate and poverty rate columns to numeric values
df_hs['percent_completed_hs'] = pd.to_numeric(df_hs['percent_completed_hs'], errors='coerce')
df_poverty['poverty_rate'] = pd.to_numeric(df_poverty['poverty_rate'], errors='coerce')

# Group by state and calculate the mean rates for each state
df_state_hs = df_hs.groupby('Geographic Area')['percent_completed_hs'].mean().reset_index()
df_state_poverty = df_poverty.groupby('Geographic Area')['poverty_rate'].mean().reset_index()

# Merge the two dataframes on 'Geographic Area' (State)
df_combined = pd.merge(df_state_hs, df_state_poverty, on='Geographic Area')

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 8))

# Plot the high school graduation rate on the left y-axis
ax1.set_xlabel('US State')
ax1.set_ylabel('High School Graduation Rate (%)', color='green')
ax1.plot(df_combined['Geographic Area'], df_combined['percent_completed_hs'], color='green', label='High School Graduation Rate')
ax1.tick_params(axis='y', labelcolor='green')
ax1.set_xticklabels(df_combined['Geographic Area'], rotation=90)

# Create a second y-axis to plot the poverty rate
ax2 = ax1.twinx()
ax2.set_ylabel('Poverty Rate (%)', color='blue')
ax2.plot(df_combined['Geographic Area'], df_combined['poverty_rate'], color='blue', label='Poverty Rate')
ax2.tick_params(axis='y', labelcolor='blue')

# Add a title and show the plot
plt.title('Comparison of High School Graduation Rate and Poverty Rate by US State')
fig.tight_layout()
plt.show()
