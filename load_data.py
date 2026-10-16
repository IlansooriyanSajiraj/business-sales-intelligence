import pandas as pd

file_path = "data/raw/Samplesuperstore.csv"
df = pd.read_csv(file_path)

print(df.head())
print(df.columns)
print("Rows and columns:", df.shape)
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print(df.groupby("Category")["Sales"].sum())
print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum())
print("\nAverage Discount by Category:")
print(df.groupby("Category")["Discount"].mean())
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())
print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum())
from pathlib import Path

summary = df.groupby("Category")[["Sales", "Profit"]].sum()

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

summary.to_csv(output_folder / "category_summary.csv")
print("\nSaved: data/processed/category_summary.csv")