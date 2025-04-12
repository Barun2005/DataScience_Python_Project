import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm  # For gradient colors

# Set a modern style
plt.style.use('ggplot')  # Switch to ggplot for a sleek look without Seaborn

# Load and Clean Data
file_path = "blinkit_unstructured_dataset (1).xlsx"
try:
    df = pd.read_excel(file_path, sheet_name=0)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

# Replace blank/whitespace with NaN and clean
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df_cleaned = df.dropna().drop_duplicates()
df.info()
# Data Analysis
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
orders_per_category = df['Category'].value_counts()
revenue_per_category = df.groupby('Category')['Price'].sum()
top10_avg_quantity = df.groupby('Product Name')['Quantity'].mean().sort_values(ascending=False).head(10)
monthly_orders = df.groupby(df['Order Date'].dt.to_period('M')).size()
price_distribution = df['Price']
category_quantity = df.groupby('Category')['Quantity'].sum()
daily_orders = df.groupby(df['Order Date'].dt.date).size()

# Plot 1: Orders per Category (Enhanced Bar Plot)
plt.figure(figsize=(12, 7))
colors = cm.Blues(np.linspace(0.9, 0.3, len(orders_per_category)))
plt.bar(orders_per_category.index, orders_per_category.values, color=colors, edgecolor='black', linewidth=1.2)
plt.title('Orders per Category', fontsize=18, weight='bold', pad=20, color='darkblue')
plt.ylabel('Number of Orders', fontsize=14, color='darkblue')
plt.xlabel('Category', fontsize=14, color='darkblue')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
plt.tight_layout()
plt.show()

# Plot 2: Revenue per Category (Enhanced Bar Plot with Labels)


# Plot 3: Top 10 Products by Average Quantity (Horizontal Bar Plot)
plt.figure(figsize=(10, 6))
plt.bar(revenue_per_category.index, revenue_per_category.values, color='blue')
plt.title('Revenue per Category')
plt.ylabel('Revenue (₹)')
plt.xlabel('Category')
plt.xticks(rotation=45, ha='right')
plt.show()

# Plot 4: Monthly Sales Trend (Line Plot with Gradient)
plt.figure(figsize=(12, 7))
plt.plot(monthly_orders.index.astype(str), monthly_orders.values, marker='o', 
         color='orange', linewidth=3, markersize=10, linestyle='-', label='Orders')
plt.title('Monthly Sales Trend', fontsize=18, weight='bold', pad=20, color='darkorange')
plt.ylabel('Number of Orders', fontsize=14, color='darkorange')
plt.xlabel('Month', fontsize=14, color='darkorange')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.legend(loc='upper right', fontsize=12, frameon=True, edgecolor='black')
plt.grid(axis='both', linestyle='--', alpha=0.5, color='gray')
plt.tight_layout()
plt.show()

# Plot 5: Price Distribution (Histogram with Gradient)
plt.figure(figsize=(12, 7))
plt.hist(price_distribution, bins=30, color=cm.Purples(0.7), edgecolor='black', linewidth=1.2)
plt.title('Price Distribution of Products', fontsize=18, weight='bold', pad=20, color='purple')
plt.xlabel('Price (₹)', fontsize=14, color='purple')
plt.ylabel('Frequency', fontsize=14, color='purple')
plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
plt.tight_layout()
plt.show()

# Plot 6: Total Quantity Sold per Category (Pie Chart with Enhanced Colors)
plt.figure(figsize=(10, 10))
colors = cm.Set2(np.linspace(0, 1, len(category_quantity)))
plt.pie(category_quantity, labels=category_quantity.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, wedgeprops={'edgecolor': 'black', 'linewidth': 1.2}, 
        textprops={'fontsize': 12, 'weight': 'bold'})
plt.title('Total Quantity Sold per Category', fontsize=18, weight='bold', pad=20, color='teal')
plt.tight_layout()
plt.show()

# Plot 7: Daily Orders Trend (Rolling Average with Dual Lines)
plt.figure(figsize=(12, 7))
rolling_avg = daily_orders.rolling(window=7, center=True).mean()
plt.plot(daily_orders.index, daily_orders.values, color='gray', alpha=0.4, label='Daily Orders', linewidth=1.5)
plt.plot(daily_orders.index, rolling_avg, color='blue', linewidth=3, label='7-Day Rolling Avg')
plt.title('Daily Orders Trend with Rolling Average', fontsize=18, weight='bold', pad=20, color='darkblue')
plt.ylabel('Number of Orders', fontsize=14, color='darkblue')
plt.xlabel('Date', fontsize=14, color='darkblue')
plt.legend(loc='upper right', fontsize=12, frameon=True, edgecolor='black')
plt.grid(axis='both', linestyle='--', alpha=0.5, color='gray')
plt.tight_layout()
plt.show()
