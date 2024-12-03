import pandas as pd
import numpy as np

# Load the dataset
path = 'AQI_Data.csv'  
data = pd.read_csv(path)

print("\n\n\n\n")

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head(5))
print("\n\n\n\n")

# Display the last 6 rows
print("\nLast 6 rows of the dataset:")
print(data.tail(6))
print("\n\n\n\n")

# Show summary statistics for all numeric columns
print("\nSummary statistics for all numeric columns:")
print(data.describe())
print("\n\n\n\n")

# Compute the mean AQI, PM2.5, and PM10 values for each city using NumPy
cities = data['City'].unique()
mean_values = {}

for city in cities:
    city_data = data[data['City'] == city]
    mean_aqi = np.mean(city_data['AQI'])
    mean_pm25 = np.mean(city_data['PM2.5'])
    mean_pm10 = np.mean(city_data['PM10'])
    mean_values[city] = {
        'Mean AQI': mean_aqi,
        'Mean PM2.5': mean_pm25,
        'Mean PM10': mean_pm10
    }

# Convert the mean values dictionary to a DataFrame
mean_df = pd.DataFrame.from_dict(mean_values, orient='index')
print("\nMean AQI, PM2.5, and PM10 values for each city:")
print(mean_df)
print("\n\n")

# Manually find the highest and lowest average AQI using a dictionary approach
highest_city = None
lowest_city = None
highest_aqi = -np.inf  # Initialize to a very low number
lowest_aqi = np.inf  # Initialize to a very high number

for city, values in mean_values.items():
    if values['Mean AQI'] > highest_aqi:
        highest_aqi = values['Mean AQI']
        highest_city = city
    if values['Mean AQI'] < lowest_aqi:
        lowest_aqi = values['Mean AQI']
        lowest_city = city

print("\nCity with the highest average AQI:")
print(f"{highest_city} with an AQI of {highest_aqi}")
print("\n")
print("\nCity with the lowest average AQI:")
print(f"{lowest_city} with an AQI of {lowest_aqi}")
