import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv")

# Chart 1: Revenue by Product
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values()
plt.figure(figsize=(10, 6))
plt.barh(product_sales.index, product_sales.values)
plt.title("Revenue by Product")
plt.xlabel("Total Sales (Rs.)")
plt.tight_layout()
plt.savefig("revenue_by_product.png", dpi=150)
plt.close()
print("Chart 1 saved: revenue_by_product.png")

# Chart 2: Revenue by Category
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values()
plt.figure(figsize=(9, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Revenue by Category")
plt.ylabel("Total Sales (Rs.)")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("revenue_by_category.png", dpi=150)
plt.close()
print("Chart 2 saved: revenue_by_category.png")

# Chart 3: Payment Method Distribution
payments = df["Payment_Method"].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(payments.values, labels=payments.index, autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig("payment_methods.png", dpi=150)
plt.close()
print("Chart 3 saved: payment_methods.png")

print("SUCCESS! All 3 charts have been created.")
