# My first data science project
import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")

print("First 5 rows:")
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Top products
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("Top Products:")
print(top_products)

# Monthly sales
df['Month'] = pd.to_datetime(df['Date']).dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()
print("Monthly Sales:")
print(monthly_sales)
