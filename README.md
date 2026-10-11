# Retail Sales Exploratory Data Analysis (EDA)

## Project Overview
This project analyzes retail sales data using Python, Pandas, and Matplotlib to discover sales trends and business insights.

The dataset contains 100 synthetic transactions and 9 columns.

## Technologies Used
- Python
- Pandas
- Matplotlib
- CSV
- Git and GitHub

## Project Objectives
- Analyze total sales and average transaction value.
- Identify top-performing products.
- Compare revenue by category.
- Analyze monthly sales trends.
- Compare revenue across cities.
- Understand payment method preferences.
- Create charts to visualize findings.

## Key Findings

### Overall Sales
- Total Revenue: Rs. 32,51,620
- Total Transactions: 100
- Average Transaction Value: Rs. 32,516.20
- Highest Transaction Value: Rs. 3,07,500
- Lowest Transaction Value: Rs. 40

### Top 5 Products by Revenue
| Rank | Product | Revenue |
|---|---|---:|
| 1 | Laptop | Rs. 18,27,800 |
| 2 | Smartphone | Rs. 8,19,400 |
| 3 | Desk | Rs. 1,80,000 |
| 4 | Office Chair | Rs. 1,66,000 |
| 5 | Headphones | Rs. 1,15,900 |

### Category Analysis
Electronics generated the highest category revenue: Rs. 26,47,200.

### Monthly Sales
- Best month: March 2025 - Rs. 5,33,820
- Lowest month: May 2025 - Rs. 77,380

### City Analysis
- Highest revenue city: Mysuru - Rs. 6,52,500
- Lowest revenue city: Hyderabad - Rs. 40,260

### Payment Methods
Net Banking was the most frequently used payment method, with 26 transactions.

## Project Files
- `create_dataset.py` - creates the sample dataset
- `retail_sales.csv` - retail sales dataset
- `eda.py` - generates three analysis charts
- `monthly_sales.py` - generates the monthly sales trend chart
- `top5_products.py` - generates the top five products chart
- `business_insights_report.md` - detailed business insights report

## Visualizations
- `revenue_by_product.png`
- `revenue_by_category.png`
- `payment_methods.png`
- `monthly_sales_trend.png`
- `top5_products.png`

## How to Run

Install the required Python libraries:

```bash
py -m pip install pandas matplotlib
```

Run the analysis scripts from the project directory:

```bash
py eda.py
py monthly_sales.py
py top5_products.py
```

The charts will be saved as PNG files in the project folder.

## Business Recommendations
1. Study the strong revenue performance of laptops and smartphones.
2. Investigate monthly sales fluctuations.
3. Explore opportunities in lower-revenue cities.
4. Monitor category performance and payment preferences.
5. Validate findings using real-world sales data before making business decisions.

## Conclusion
This project demonstrates exploratory data analysis and data visualization using Python. It identifies leading products, categories, cities, payment preferences, and monthly sales patterns.

**Note:** The dataset is synthetic and does not represent actual retail business performance.

## Author
Ankitha K V  
Computer Science and Engineering Student
