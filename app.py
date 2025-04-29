import streamlit as st
from data_utils import load_data
import sys

# Append your path for modules (temporary fix if needed)
sys.path.append("E:\Work\Omdena\capstone-project-npanerugithub2024\pages")
from pages import data_exploration, model_training, prediction_page

# Set the page configuration
st.set_page_config(
    page_title="Capstone Project",
    page_icon=" ",
    layout="wide"
)

# Title
st.title("Capstone Project by Nav Paneru")
st.markdown("Develop an end-to-end data analysis system that monitors, analyzes, and predicts climate change impacts in Nepal with a focus on vulnerable regions.")

# Load data
with st.spinner('Loading data...'):
    df = load_data()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Data Exploration", "Model Training", "Prediction"])

# Display the selected page
if page == "Data Exploration":
    data_exploration.show(df)
elif page == "Model Training":
    model_training.show(df)
else:  # Prediction
    prediction_page.show(df)

# Footer (optional)
st.markdown("""---""")
st.caption("Created as part of Omdena Nepal Chapter 🌏")
