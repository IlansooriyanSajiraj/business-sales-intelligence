import pandas as pd
import streamlit as st

st.title("Business Sales Intelligence")
st.write("Sample Superstore sales data")

df = pd.read_csv("data/raw/Samplesuperstore.csv")
st.dataframe(df.head())
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Business Sales Intelligence", layout="wide")
st.title("Business Sales Intelligence")

df = pd.read_csv("data/raw/Samplesuperstore.csv")

regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Choose a Region", regions)

if selected_region == "All":
    filtered_df = df
else:
    filtered_df = df[df["Region"] == selected_region]

sales_total = filtered_df["Sales"].sum()
profit_total = filtered_df["Profit"].sum()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${sales_total:,.2f}")
col2.metric("Total Profit", f"${profit_total:,.2f}")

st.subheader("Sales by Category")
sales_by_category = filtered_df.groupby("Category")["Sales"].sum()
st.bar_chart(sales_by_category)

st.subheader("Data Preview")
st.dataframe(filtered_df.head(10))