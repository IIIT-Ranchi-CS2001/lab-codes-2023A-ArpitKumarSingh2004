import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000], # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020], # Day 5
    [1800, 2300, 2100, 1500, 1050], # Day 6
    [1900, 2400, 2200, 1600, 1100], # Day 7
])      

# Define country labels
countries = ['Country_A', 'Country_B', 'Country_C', 'Country_D', 'Country_E']

# Convert data to a Pandas DataFrame for easier manipulation
df = pd.DataFrame(covid_data, columns=countries)

# Task 1: Basic Statistics
# Total cases for each country over the 7 days
total_cases_per_country = df.sum()
print("Total cases per country:\n", total_cases_per_country)

# Country with the highest total cases
country_with_max_cases = total_cases_per_country.idxmax()
max_cases = total_cases_per_country.max()
print(f"Country with the highest cases: {country_with_max_cases} ({max_cases} cases)")

# Task 2: Daily Analysis
# Average cases reported per day across all countries
average_cases_per_day = df.mean(axis=1)
print("Average cases per day across all countries:\n", average_cases_per_day)

# Day with the highest total cases across all countries
total_cases_per_day = df.sum(axis=1)
day_with_highest_cases = total_cases_per_day.idxmax() + 1  # +1 to convert to 1-based day number
print(f"Day with the highest cases: Day {day_with_highest_cases} ({total_cases_per_day.max()} cases)")

# Task 3: Trends
# Percentage increase or decrease in cases for each country from Day 1 to Day 7
percentage_change = ((df.iloc[-1] - df.iloc[0]) / df.iloc[0]) * 100
print("Percentage change in cases from Day 1 to Day 7:\n", percentage_change)

# Country with the highest percentage increase
country_with_highest_increase = percentage_change.idxmax()
highest_increase = percentage_change.max()
print(f"Country with the highest percentage increase: {country_with_highest_increase} ({highest_increase:.2f}%)")

# Task 4: Data Transformation
# Normalizing the data for each country (scaling between 0 and 1)
normalized_data = (df - df.min()) / (df.max() - df.min())
print("Normalized dataset:\n", normalized_data)

# Task 5: Visualization
plt.figure(figsize=(10, 6))

# Plot daily cases for each country
for country in countries:
    plt.plot(df.index + 1, df[country], marker='o', label=country)

# Highlight the day with the highest total cases across all countries
plt.axvline(day_with_highest_cases, color='red', linestyle='--', label=f'Highest Total Cases (Day {day_with_highest_cases})')
plt.text(day_with_highest_cases, total_cases_per_day.max(), f'Day {day_with_highest_cases}', color='red', ha='right')

# Chart labels and legend
plt.title("Daily COVID-19 Cases per Country")
plt.xlabel("Days")
plt.ylabel("Number of Cases")
plt.legend(loc='upper left')
plt.show()
