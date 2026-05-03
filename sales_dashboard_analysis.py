import pandas as pd
import matplotlib.pyplot as plt

# 1. Creating Mock Data
data = {
    'Date': pd.date_range(start='2026-01-01', periods=5, freq='M'),
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Sales': [50000, 1500, 3000, 12000, 2500],
    'Region': ['North', 'South', 'East', 'West', 'North']
}
df = pd.DataFrame(data)

# 2. Analyzing Data (Total Sales)
total_revenue = df['Sales'].sum()
print(f"Total Revenue Generated: ₹{total_revenue}")

# 3. Visualizing Data
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Sales'], color='skyblue')
plt.title('Product Sales Overview')
plt.xlabel('Products')
plt.ylabel('Sales in ₹')
plt.show()
