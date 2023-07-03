from datetime import date, datetime
import streamlit as st

# Day we started
start = date(year=2023, month=6, day=29)

# Get today's date
today = datetime.today().date()

# Specify the future date
future_date = datetime(2024, 3, 1).date() 

# Calculate the number of days
num_days = (future_date - today).days
days_since_start = (today - start).days


st.title("FranzCountdown")
st.metric(label="Remaining", value=f"{num_days} days", delta=f"-{days_since_start} days")

