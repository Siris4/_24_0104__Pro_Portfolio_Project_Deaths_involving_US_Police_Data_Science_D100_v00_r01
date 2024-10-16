import pandas as pd
import seaborn as sns
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

# Create a Seaborn jointplot with scatter plot and KDE
sns.jointplot(x='percent_completed_hs', y='poverty_rate', data=df_combined, kind='scatter', marginal_kws=dict(bins=20, fill=True))
sns.jointplot(x='percent_completed_hs', y='poverty_rate', data=df_combined, kind='kde')

# Add titles and show the plots
plt.suptitle('Relationship Between High School Graduation Rate and Poverty Rate', y=1.02)
plt.show()
