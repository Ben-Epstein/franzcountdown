from datetime import datetime
import streamlit as st

# Get today's date
today = datetime.today().date()

# Specify the future date
future_date = datetime(2024, 3, 1).date()  # Replace with your desired future date

# Calculate the number of days
num_days = (future_date - today).days


st.title("FranzCountdown")
st.metric(label="Remaining", value=f"{num_days} days", delta="1 day")

