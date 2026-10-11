
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": ("Electronics", 45000, 75000),
    "Smartphone": ("Electronics", 12000, 45000),
    "Headphones": ("Accessories", 800, 5000),
    "Keyboard": ("Accessories", 500, 2500),
    "Office Chair": ("Furniture", 3500, 12000),
    "Desk": ("Furniture", 4000, 15000),
    "Notebook": ("Stationery", 40, 150),
    "Backpack": ("Accessories", 700, 3000),
    "Water Bottle": ("Lifestyle", 200, 1000),
    "Mouse": ("Accessories", 300, 1800)
}

cities = ["Bengaluru", "Mangaluru", "Mysuru", "Mumbai", "Chennai",
          "Hyderabad", "Pune", "Delhi", "Kochi", "Coimbatore"]

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"]

rows = []

start_date = datetime(2025, 1, 1)

for i in range(1, 101):
    product = random.choice(list(products.keys()))
    category, min_price, max_price = products[product]

    quantity = random.randint(1, 5)
    unit_price = random.randrange(min_price, max_price + 1, 100)
    order_date = start_date + timedelta(days=random.randint(0, 364))

    rows.append({
        "Order_ID": f"ORD{i:04d}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Total_Sales": quantity * unit_price,
        "Payment_Method": random.choice(payment_methods),
        "City": random.choice(cities)
    })

df = pd.DataFrame(rows)

df.to_csv("retail_sales.csv", index=False)

print("Dataset created successfully!")
print("Number of transactions:", len(df))
print("CSV file: retail_sales.csv")
print("\nFirst 5 rows:")
print(df.head())
