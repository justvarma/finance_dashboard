import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Simple Finance App", page_icon="💸", layout="wide")


def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to.datetime(df["Date"], format="%d %b %Y")
        st.write(df)
        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None


def main():
    st.title("Finance Dashboard")
    uploadede_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])
    if uploadede_file is not None:
        df = load_transactions(uploadede_file)
        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()

            tab1, tab2 = str.tabs(["Expenses (Debits)", "Payments (Credits)"])

main()
