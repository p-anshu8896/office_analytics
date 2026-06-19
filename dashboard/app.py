import streamlit as st
import pandas as pd

df = pd.read_csv("D:\\Download Content\\office_analytics\\data\\processed\\processed_data.csv")

st.title("Office Analytics Dashboard")

st.header("filter")
dept = st.sidebar.selectbox("Department", df["Department"].unique())

filtered = df[df["Department"] == dept]

st.metric("Total Sales", int(filtered['sales_amount'].sum()))
st.metric("Avg productivity", round(filtered['productivity'].mean(), 2))

st.subheader("Sales trend")
st.line_chart(filtered.groupby("date")["sales_amount"].sum())
st.subheader("Task performance")
st.bar_chart(filtered.groupby("employee_id")["task_completed"].sum())