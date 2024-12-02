# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import folium

# Load the dataset (replace with the correct path to your dataset)
df = pd.read_csv(r'C:\Users\kacha\Downloads\Prodigy\Task_5\RTA Dataset.csv')

#Inspect the dataset
print(df.head())
print(df.info())
# Data Cleaning (handle missing values, incorrect data types, etc.)
df.dropna(inplace=True)  
df['Time'] = pd.to_datetime(df['Time'], errors='coerce') 

# Extract relevant time features (hour, day of week)
df['hour'] = df['Time'].dt.hour
df['day_of_week'] = df['Time'].dt.dayofweek  # Monday=0, Sunday=6

# Univariate Analysis
plt.figure(figsize=(10, 6))
sns.countplot(x='hour', data=df)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Weather_conditions', data=df)
plt.title('Accidents by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Road_surface_type', data=df)
plt.title('Accidents by Road Surface Type')
plt.xlabel('Road Surface Type')
plt.ylabel('Number of Accidents')
plt.show()

# Bivariate Analysis f
plt.figure(figsize=(10, 6))
sns.heatmap(pd.crosstab(df['Weather_conditions'], df['Road_surface_type']), annot=True, cmap='coolwarm')
plt.title('Weather vs Road Surface Type')
plt.show()


