import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="Banking Fraud Analysis",
    page_icon="🏦",
    layout="wide"
)

# ---------------- Load Dataset ----------------

@st.cache_data
def load_data():
    return pd.read_csv("Dataset/fraud_dataset.csv")

df = load_data()

# ---------------- Sidebar ----------------

st.sidebar.title("🏦 Banking Fraud Analysis")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "📋 Dataset", "🤖 ML Model", "ℹ️ About"]
)

st.sidebar.markdown("---")
st.sidebar.success("Project Status: Completed ✅")

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.title("🏦 Banking Fraud Analysis Dashboard")

    st.markdown("""
    Welcome to the **Banking Fraud Analysis Dashboard**.

    This project analyzes banking transactions to identify fraudulent
    activities using **Machine Learning** and **Data Analytics**.
    """)

    total_transactions = len(df)
    fraud_cases = len(df[df["fraud_label"] == 1])
    normal_transactions = len(df[df["fraud_label"] == 0])
    avg_amount = df["transaction_amount"].mean()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Transactions", total_transactions)
    c2.metric("Fraud Cases", fraud_cases)
    c3.metric("Normal Transactions", normal_transactions)
    c4.metric("Average Amount", f"₹{avg_amount:.2f}")

    st.divider()

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📈 Statistical Summary")
    st.dataframe(df.describe())

# ---------------- DASHBOARD ----------------

elif page == "📊 Dashboard":

    st.title("📊 Fraud Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Fraud vs Normal Transactions")

        fraud_counts = df["fraud_label"].value_counts()

        fig, ax = plt.subplots()

        ax.bar(
            ["Normal", "Fraud"],
            [fraud_counts.get(0, 0), fraud_counts.get(1, 0)]
        )

        ax.set_ylabel("Transactions")

        st.pyplot(fig)

    with col2:

        st.subheader("Transaction Amount Distribution")

        fig2, ax2 = plt.subplots()

        ax2.hist(df["transaction_amount"], bins=10)

        ax2.set_xlabel("Amount")

        ax2.set_ylabel("Frequency")

        st.pyplot(fig2)

    st.subheader("📍 Fraud by Location")

    location = (
        df[df["fraud_label"] == 1]
        .groupby("location")
        .size()
    )

    fig3, ax3 = plt.subplots()

    ax3.bar(location.index, location.values)

    plt.xticks(rotation=45)

    st.pyplot(fig3)

# ---------------- DATASET ----------------

elif page == "📋 Dataset":

    st.title("📋 Dataset Explorer")

    search = st.text_input("Search Merchant")

    if search:

        filtered = df[
            df["merchant"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

        st.dataframe(filtered)

    else:

        st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Dataset",
        csv,
        "fraud_dataset.csv",
        "text/csv"
    )

# ---------------- ML MODEL ----------------

elif page == "🤖 ML Model":

    st.title("🤖 Machine Learning Model")

    st.success("Model Used: Logistic Regression")

    st.markdown("""
### Workflow

- Data Collection
- Data Cleaning
- Feature Engineering
- Train/Test Split
- Logistic Regression
- Model Evaluation

### Evaluation

- Accuracy Score
- Confusion Matrix
- Classification Report
""")

# ---------------- ABOUT ----------------

elif page == "ℹ️ About":

    st.title("ℹ️ About Project")

    st.markdown("""
### 🏦 Banking Fraud Analysis

**Objective**

Detect fraudulent banking transactions using Machine Learning.

### Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Power BI

### Developer

**Gangi Reddy Charitha**
""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🏦 Banking Fraud Analysis | Machine Learning Project | Developed by Gangi Reddy Charitha"
)
