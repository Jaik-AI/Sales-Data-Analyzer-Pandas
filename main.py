import pandas as pd

df = pd.read_csv('sales.csv')
df['Revenue'] = df['Price']*df['Quantity']
print(df)

print("\n=== Total Revenue ===")
print(f"Total revenue : ₹{df['Revenue'].sum()}")

expensive_product = df['Price'].idxmax()
print("\n=== Most Expensive product ===")
print(f"Product name : {df.loc[expensive_product,'Product']}\nPrice : ₹{df.loc[expensive_product,'Price']}")

print("\n=== Cheapest Product ===")
cheapest_product = df['Price'].idxmin()
print(f"Product name : {df.loc[cheapest_product,'Product']}\nPrice : ₹{df.loc[cheapest_product,'Price']}")

print("\n=== Best selling product ===")
best_selling = df['Quantity'].idxmax()
print(f"Product name : {df.loc[best_selling,'Product']}\nPrice : ₹{df.loc[best_selling,'Price']}\nQuantity : {df.loc[best_selling,'Quantity']}\nRevenue : ₹{df.loc[best_selling,'Revenue']:,}")

print("\n=== Highest Revenue product ===")
highest_revenue = df['Revenue'].idxmax()
print(f"Product name : {df.loc[highest_revenue,'Product']}\nRevenue : ₹{df.loc[highest_revenue,'Revenue']:,}\nQuantity : {df.loc[highest_revenue,'Quantity']}")

category_revenue = df.groupby('Category')['Revenue'].sum()
print("\n=== Category-wise Revenue ===")
for category,revenue in category_revenue.items():
    print(f"{category} : ₹{revenue:,}")

print("\n=== Average Product Price ===")
print(f"Price : ₹{df['Price'].mean():,.2f}")

print("\n=== Top 3 Highest Revenue Products ===")
top_revenue = df.sort_values('Revenue',ascending=False).head(3)
for i,(_,row) in enumerate(top_revenue.iterrows(),start=1):
    print(f"{i}. {row['Product']} ")
    print(f"   Price : ₹{row['Price']:,}")
    print(f"   Quantity : {row['Quantity']}")
    print(f"   Revenue : ₹{row['Revenue']:,}")

print("\n=== Sales Report ===")
print(f"Total Products : {len(df)}")
print(f"Total Revenue : ₹{df['Revenue'].sum():,}")
print(f"Highest Revenue Product : {df.loc[highest_revenue,'Product']}")
print(f"Highest Revenue Category : {category_revenue.idxmax()}")
print(f"Best Selling Product : {df.loc[best_selling,'Product']}")
print(f"Average Product Price : ₹{df['Price'].mean():,.2f}")