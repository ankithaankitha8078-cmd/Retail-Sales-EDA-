import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv")

top5 = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .sort_values()
)

plt.figure(figsize=(9, 5))
plt.barh(top5.index, top5.values)
plt.title("Top 5 Products by Revenue")
plt.xlabel("Total Sales (Rs.)")
plt.tight_layout()
plt.savefig("top5_products.png", dpi=150)
plt.close()

print("SUCCESS! Top 5 products chart created.")
