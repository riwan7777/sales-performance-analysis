import pandas as pd
import matplotlib.pyplot as plt

# CSV file load (make sure sales_data.csv file is in same folder)
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# Month column for grouping (YYYY-MM format)
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Group data
sales_by_product = df.groupby("Product")["Total"].sum().sort_values(ascending=False)
sales_by_region = df.groupby("Region")["Total"].sum().sort_values(ascending=False)
sales_by_month = df.groupby("Month")["Total"].sum().sort_index()

# Plot 1: Sales by Product
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()
plt.close()

# Plot 2: Sales by Region
plt.figure(figsize=(8,5))
sales_by_region.plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
plt.close()

# Plot 3: Monthly Sales
plt.figure(figsize=(10,5))
sales_by_month.plot(kind='line', marker='o')
plt.title("Monthly Sales (Total)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()
plt.close()
