# Ecommerce Sales Analysis

Objective:
To analyze an e-commerce sales dataset, uncover key business insights, and visualize them in an interactive Power BI dashboard.

1. Dataset Acquisition
    Created a mock CSV dataset simulating e-commerce transactions.

    Fields included: Order ID, Product, Category, Sales, Profit, Discount, Order Date, and more.

2. Data Cleaning & Preprocessing (Python)
    Loaded data using pandas:

    Removed duplicates

    Handled null values (dropped or filled based on context)

    Converted date fields to datetime format

    Verified numerical columns and scaled if necessary

3. Exploratory Analysis (Python)
    Used matplotlib and seaborn for visual exploration:

    Sales and profit distribution

    Correlation between discount and profitability

    Category-wise performance
   
4. Visualization & Dashboard (Power BI)
    Imported cleaned CSV into Power BI

    Created key visuals:

    KPI cards: Total Sales, Profit, Average Profit Margin, Orders

    Time series: Monthly Sales Trend

    Bar/Column Charts: Sales by Category, Profit Margin by Category

    Built slicers for dynamic filtering: Category, Date
