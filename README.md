# Amazon Top 1000 Software Analysis

## Overview
This project performs an exploratory data analysis (EDA) on Amazon's top 1000 bestselling software and digital products across 10 major global markets for 2025. 

The goal is to understand product ratings, price distributions, and country-specific trends.

## Dataset
The dataset includes the following fields:

- `rank`: Bestseller ranking position (1-1000)
- `asin`: Amazon Standard Identification Number (unique product identifier)
- `product_title`: Complete product name and description
- `product_price`: Pricing in local currency
- `product_star_rating`: Customer satisfaction rating (1-5 stars)
- `product_num_ratings`: Total number of customer reviews
- `product_url`: Direct Amazon product page link
- `product_photo`: Product image URL
- `rank_change_label`: Ranking movement indicator
- `country`: Two-letter country/market code
- `page`: Data pagination reference number

## Analysis Performed
1. Descriptive statistics on numeric columns
2. Identification of top-rated products
3. Extraction of top 100 rated products
4. Count of products per country
5. Visualization:
   - Bar plot of product distribution by country
   - Histogram of product star ratings

## How to Run
1. Place `main.py` and the dataset `Amazon_bestsellers_items_2025.csv` in the same folder.
2. Open terminal or command prompt in that folder.
3. Run:


