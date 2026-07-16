import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Banking Fraud Analysis",
    page_icon="🏦",
    layout="wide"
)

# Title
st.title("🏦 Banking Fraud Analysis")
st.subheader("Machine Learning Project")

st.write("""
This project analyzes banking transactions to identify fraudulent transactions
using Machine Learning and visual analytics.
""")

# Load dataset
try:
    df = pd.read_csv("Dataset/fraud_dataset.csv")

    st.header("📊 Dataset Preview")
    st.dataframe(df.head())

    st.header("Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.header("Statistics")
    st.write(df.describe())

except Exception as e:
    st.error("Dataset not found!")
    st.write(e)

st.header("🛠️ Technologies Used")

st.markdown("""
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Power BI
""")

st.success("Project Completed Successfully ✅")
