# Description: This is a simple Streamlit app created with help of AI that calculates the number of days you have lived in this world.

import streamlit as st
from datetime import datetime

# Set the background color
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, red, orange, #CCCC00, green, blue, indigo, violet);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 5px 10px;
        margin: 2px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1, h2, h3, h4, h5, h6 {
        color: black;
    }
    .non-editable {
        background-color: #f0f0f0;
        color: #333333;
        padding: 5px 10px;
        margin: 2px;
        border: 1px solid #ccc;
        border-radius: 4px;
        display: inline-block;
        width: 100%;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown("""<h1 style='color:black;'>Know your Days</h1>
            <h6 style='color:black;'>This app calculates the number of days you have lived in this world.</h6>""",
            unsafe_allow_html=True)

# Input fields for start date
st.markdown("### Select your Birth Date")
col1, col2, col3 = st.columns(3)
with col1:
    start_day = st.selectbox("Day", list(range(1, 32)), index=14)
with col2:
    start_month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=5)
with col3:
    current_year = datetime.now().year
    start_year = st.selectbox("Year", list(range(1925, current_year + 1)), index=20)

# Convert month name to month number
month_numbers = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}
start_month_num = month_numbers[start_month]

# Display today's date in three boxes
today = datetime.today()
st.markdown("### Today's Date")
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(f"<div class='non-editable'>{today.day}</div>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<div class='non-editable'>{today.month}</div>", unsafe_allow_html=True)
with col6:
    st.markdown(f"<div class='non-editable'>{today.year}</div>", unsafe_allow_html=True)

# Calculate the difference in days
if st.button("Calculate"):
    try:
        start_date = datetime(start_year, start_month_num, start_day)
        end_date = today
        delta = end_date - start_date
        days_lived = delta.days
        if days_lived < 0:
            st.markdown("<h3 style='color: red;'>Can't determine the days for future child</h3>", unsafe_allow_html=True)
        else:
            life_expectancy_days = 36525  # 100 years
            percentage_lived = (days_lived / life_expectancy_days) * 100
            if percentage_lived > 100:
                st.markdown("<h3 style='color: red;'>You have lived more than 100% of the expected lifespan.You are lucky, you are an Outlier</h3>", unsafe_allow_html=True)
            else:
                st.markdown(
                    f"""
                    <h4 style='color: red;'>You have spent {days_lived} days in this world.</h4>
                    <p>Average life expectancy of Human is 73 years today.</p>
                    <p>Assuming that the technology today will increase your lifespan such that you may live for 100 years which is 36525 days.So considering {start_year + 100}, {percentage_lived:.2f}% of your life is completed.</p>
                    <h4 style='color:black';>Life is too short, Be happy and let your dreams be bigger than your fears.</h4>
                    """,
                    unsafe_allow_html=True
                )
    except ValueError as e:
        st.error(f"Error: {e}")
