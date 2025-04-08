import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and Clean Data

file_path = "blinkit_unstructured_dataset (1).xlsx"
try:
    df = pd.read_excel(file_path, sheet_name=0)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

# Replace blank/whitespace with NaN and clean
df.info()
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df_cleaned = df.dropna().drop_duplicates()

# Data Analysis
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
orders_per_category = df['Category'].value_counts()
revenue_per_category = df.groupby('Category')['Price'].sum()
top10_avg_quantity = df.groupby('Product Name')['Quantity'].mean().sort_values(ascending=False).head(10)
monthly_orders = df.groupby(df['Order Date'].dt.to_period('M')).size()

