import streamlit as st
from data_utils import load_data
import sys

# Append your path for modules (temporary fix if needed)
sys.path.append("E:\Work\Omdena\capstone-project-npanerugithub2024\pages")
from pages import data_exploration, model_training, prediction_page



# Set the page configuration
st.set_page_config(
    page_title="Nepal Climate Nexus: Weather, Earth & People",
    page_icon="🛰️",
    layout="wide"
)

# Title
st.title("Nepal Climate Nexus: Weather, Earth & People")
st.markdown("### Weather, Earth & People")

st.markdown("""
Welcome to **Nepal Climate Nexus**, a centralized platform designed to integrate and visualize diverse datasets related to climate change and its impacts in Nepal.

This application brings together **weather**, **environmental**, and **socioeconomic** data from reliable global and national sources to support climate research, policy-making, and community resilience efforts.

---

### 🔍 What You’ll Find Here:

#### 🌀 Weather & Climate Data
- Historical temperature, precipitation, and extreme weather records
- Satellite-based glacial monitoring from NASA Earth Data
- ERA5 reanalysis climate datasets
- Observations from global and local weather stations

#### 🌱 Environmental Data
- Land use and forest cover changes using satellite imagery
- River discharge and hydrological trends
- Glacial lake formation and evolution patterns

#### 👥 Socioeconomic Data
- Agriculture yield statistics from Nepal’s Ministry of Agriculture
- Population and infrastructure mapping in vulnerable regions
- Economic losses from past climate-related disasters

---

### 🛠️ How to Use the Platform:
Navigate through the sidebar to:
- **Explore datasets** in detail
- **Visualize climate trends** across Nepal
- **Generate predictions** using machine learning models
- **Compare regions** based on risk and resilience indicators

---

### 📢 A Note of Thanks:
This project is part of a broader initiative to **empower decision-makers, researchers, and citizens** with accessible, data-driven insights to tackle the climate crisis in Nepal.

""")

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
