import streamlit as st
from salary_predict_page import salary_predict

def main():
    # page = st.sidebar.selectbox("Select", ("Car price predictor", "Salary Predictor"))

    salary_predict()

    