# Sales-Data-Analyzer-Pandas
A Python project that uses Pandas to analyze sales data from a CSV file. The project calculates revenue, identifies top-performing products, performs category-wise analysis, and generates a detailed sales report.

## Features

- Read sales data from a CSV file
- Calculate revenue for each product
- Find total revenue
- Identify the most expensive product
- Identify the cheapest product
- Find the best-selling product
- Find the highest revenue product
- Category-wise revenue analysis using GroupBy
- Calculate average product price
- Display the top 3 highest revenue products
- Generate a summarized sales report

## Technologies Used

- Python
- Pandas

## Dataset

The dataset contains:

- Product
- Category
- Price
- Quantity

The program creates a new **Revenue** column using:

```
Revenue = Price × Quantity
```

## Concepts Practiced

- Reading CSV files
- DataFrames
- Creating new columns
- Data filtering
- Sorting
- GroupBy
- Aggregation (`sum`, `mean`)
- `idxmax()` and `idxmin()`
- `iterrows()`
- `enumerate()`
- Formatted output using f-strings

## How to Run

1. Install Pandas

```
pip install pandas
```

2. Place `sales.csv` in the project folder.

3. Run:

```
python main.py
```

## Sample Output

- Total Revenue
- Best Selling Product
- Highest Revenue Product
- Category-wise Revenue
- Top 3 Highest Revenue Products
- Sales Report

## What I Learned

- Working with CSV files using Pandas
- Creating calculated columns
- Business data analysis
- Using GroupBy for category-wise insights
- Formatting reports for better readability
