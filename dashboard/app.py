import streamlit as st
import pandas as pd
from auth.login import login

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
st.sidebar.title("login")
username = st.sidebar.text_input("username")
password = st.sidebar.text_input("password", type="password")

role = login(username, password)

if role :
    st.success(f"Logged in as {role}")

    if role == "admin":
        st.title("Admin Panel")
        st.write("Here you can manage users and view detailed analytics.")

    elif: role == "user1":
        st.title("User Dashboard")
        st.write("Welcome to your dashboard! Here you can view your performance metrics and tasks.")

    elif role == "user2":
        st.title("User Dashboard")
        st.write("Welcome to your dashboard! Here you can view your performance metrics and tasks.")
else:
    st.warning("Invalid credentials. Please try again.")
    