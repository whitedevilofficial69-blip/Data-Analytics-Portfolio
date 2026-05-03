import pandas as pd
import numpy as np

# Mock Messy Data
messy_data = {
    'Employee_ID': [101, 102, 102, 104, 105],
    'Name': ['Amit', 'Rahul', 'Rahul', np.nan, 'Priya'],
    'Salary': [45000, 50000, 50000, 60000, np.nan]
}
df = pd.DataFrame(messy_data)

print("Original Messy Data:\n", df)

# 1. Remove Duplicates
df_cleaned = df.drop_duplicates()

# 2. Handle Missing Values (Fill NaN names with 'Unknown', Salary with average)
df_cleaned['Name'].fillna('Unknown', inplace=True)
avg_salary = df_cleaned['Salary'].mean()
df_cleaned['Salary'].fillna(avg_salary, inplace=True)

print("\nCleaned Data:\n", df_cleaned)
# To export: df_cleaned.to_csv('cleaned_data.csv', index=False)
