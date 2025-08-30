# ===============================
# Amazon Top 1000 Software Analysis
# ===============================

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Load data
# -------------------------------
amazon_bs = pd.read_csv(
    "C:\\Users\\osama\\Desktop\\amazon\\Amazon_bestsellers_items_2025.csv"
)

# Drop rows with missing critical values
amazon_bs = amazon_bs.dropna(subset=['product_star_rating', 'country', 'product_price'])

# -------------------------------
# Basic statistics
# -------------------------------
print("Data Description:")
print(amazon_bs.describe())

mean_values = amazon_bs.mean(numeric_only=True)
print("\nMean Values:\n", mean_values)

# -------------------------------
# Top-rated products
# -------------------------------
highest_rating = amazon_bs['product_star_rating'].max()
print("\nHighest Rating:", highest_rating)

top_rated_products = amazon_bs[amazon_bs['product_star_rating'] == highest_rating]
print("\nTop Rated Products:")
print(top_rated_products[['product_title', 'product_price', 'country', 'product_star_rating']])

# Top 100 rated products
top_100_rated = amazon_bs.nlargest(100, 'product_star_rating')
print("\nTop 100 Rated Products:")
print(top_100_rated[['product_title', 'product_price', 'country', 'product_star_rating']])

# -------------------------------
# Country analysis
# -------------------------------
country_counts = amazon_bs['country'].value_counts()
print("\nProduct Counts by Country:")
print(country_counts)

most_common_country = country_counts.idxmax()
print("\nMost Frequent Country:", most_common_country)

# Bar plot of product distribution by country
plt.figure(figsize=(12,6))
country_counts.plot(kind='bar', color='skyblue', title='Distribution of Products by Country')
plt.xlabel('Country')
plt.ylabel('Number of Products')
plt.grid(axis='y')
plt.show()

# -------------------------------
# Product rating distribution
# -------------------------------
plt.figure(figsize=(10,5))
amazon_bs['product_star_rating'].hist(bins=10, color='orange', edgecolor='black')
plt.title('Histogram of Product Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.grid(axis='y')
plt.show()


