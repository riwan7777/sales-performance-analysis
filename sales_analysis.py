import pandas as pd
import matplotlib.pyplot as plt

# CSV file load
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# Basic info
print("Rows and columns:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values:\n", df.isna().sum())

# Month column for grouping
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Grouped totals
sales_by_product = df.groupby("Product")["Total"].sum().sort_values(ascending=False)
sales_by_region = df.groupby("Region")["Total"].sum().sort_values(ascending=False)
sales_by_month = df.groupby("Month")["Total"].sum().sort_index()

print("\nSales by Product:\n", sales_by_product)
print("\nSales by Region:\n", sales_by_region)
print("\nSales by Month:\n", sales_by_month.head())

# Product sales chart
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()

# Region sales chart
plt.figure(figsize=(8, 5))
sales_by_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# Monthly sales chart
plt.figure(figsize=(10, 5))
sales_by_month.plot(kind="line", marker="o")
plt.title("Monthly Sales (Total)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Top records
print("\nTop Products:\n", sales_by_product.head())
print("\nTop Regions:\n", sales_by_region.head())
print("\nTop 10 Orders:\n", df.sort_values(by="Total", ascending=False).head(10))
