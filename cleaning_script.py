# This script cleans up and analyzes the e-commerce csv file 

# Cleaning Steps 

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\thale\\OneDrive\\Área de Trabalho\\Data Analysis\\E-commerce Analysis Mockup Project\\ecommerce_mockup.csv")

# Check for duplicates
duplicates = df.duplicated()
print(f"Duplicates found: {duplicates.sum()}")
df = df.drop_duplicates()

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Drop or fill missing values
# df = df.dropna()  # to remove rows with nulls
# df['Column'] = df['Column'].fillna(value)  # if you want to fill them

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Strip whitespace and normalize text 
df["Category"] = df["Category"].str.strip().str.title()
df["Sub-Category"] = df["Sub-Category"].str.strip().str.title()

# Add new columns
df["Profit Margin"] = df["Profit"] / df["Sales"]
df["Price per Unit"] = df["Sales"] / df["Quantity"]
df["High Discount"] = df["Discount"].apply(lambda x: "Yes" if x > 0.2 else "No")
df["Month"] = df["Order Date"].dt.to_period("M")

# Confirm clean structure
print("\nCleaned data preview:\n", df.head())

# Save cleaned file
df.to_csv("C:\\Users\\thale\\OneDrive\\Área de Trabalho\\Data Analysis\\E-commerce Analysis Mockup Project\\ecommerce_mockup.csv", index=False)

#Analysis

# Total Sales by Category
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values()
sales_by_category.plot(kind="barh", title="Total Sales by Category", color="skyblue")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()


# Monthly Sales Trend
monthly_sales = df.groupby(df["Month"].astype(str))["Sales"].sum()
monthly_sales.plot(kind="bar", figsize=(12,6))
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit vs Discount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category")
plt.title("Profit vs Discount by Category")
plt.tight_layout()
plt.show()

# Top 10 Products by Sales
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
top_products.plot(kind="bar", title="Top 10 Products by Sales", color="coral")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

