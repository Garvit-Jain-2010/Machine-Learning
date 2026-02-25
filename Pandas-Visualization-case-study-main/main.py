# 1. Compare Sales by region for 2016 with 2015 using bar chart
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SalesData.csv")

region_sales = df.groupby("Region")[["Sales2015", "Sales2016"]].sum()
region_sales.plot(kind="bar")

plt.title("Sales Comparison by Region (2015 vs 2016)")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# 2. What are the contributing factors to the sales for each region in 2016. Visualize it using a pie Chart.

