# My first data science project
import pandas as pd
import matplotlib.pyplot as plt

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

# Graph 1: Bar chart for top products
top_products.plot(kind='bar')
plt.title("Top Products Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Graph 2: Line chart for monthly sales
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
