import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv("C:/Users/snega/OneDrive/Desktop/BDM TERM 3/Netrual Networks/ml-with-python-course-project/train.csv")

st.title("Campus Placement Dashboard")

# 1. Summary Statistics
st.header("Summary Statistics")
placement_counts = data['status'].value_counts()
st.write("Placement Status Counts:")
st.write(placement_counts)

# 2. Placement Rate by Degree Type
st.header("Placement Rate by Degree Type")
placement_by_degree = data.groupby("degree_t")['status'].apply(lambda x: (x == "Placed").mean()).reset_index()
fig1 = px.bar(placement_by_degree, x="degree_t", y="status", title="Placement Rate by Degree Type", labels={"status": "Placement Rate"})
st.plotly_chart(fig1)

# 3. SSC Score Distribution by Placement Status
st.header("SSC Score Distribution by Placement Status")
fig2 = px.histogram(data, x="ssc_p", color="status", barmode="overlay", title="SSC Score Distribution")
st.plotly_chart(fig2)
