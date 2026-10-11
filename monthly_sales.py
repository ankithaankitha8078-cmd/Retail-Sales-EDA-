import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Total Sales (Rs.)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150)
plt.close()

print("SUCCESS! Monthly sales chart created.")
print("File: monthly_sales_trend.png")
