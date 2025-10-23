import streamlit as st
from meal_calorie_estimator import meal_calorie_estimator
from exercise_tracker import exercise_tracker
from nutrition_planner import nutrition_planner

import streamlit as st
import os

# Fetch API key securely
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Optional: also make it accessible to APIs expecting an environment var
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Set the Streamlit page config
st.set_page_config(page_title="FitBite", layout="centered")
st.title("🥗 FitBite - Your Fitness Buddy")

# Define session state for the selected option to persist after button click
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = "🍽️ Meal Calorie Estimator"

# Sidebar navigation with buttons that persist the selection
button1 = st.sidebar.button("🍽️ Meal Calorie Estimator")
button2 = st.sidebar.button("🏋️ Exercise Tracker")
button3 = st.sidebar.button("📊 Nutrition Planner")

if button1:
    st.session_state.selected_option = "🍽️ Meal Calorie Estimator"
elif button2:
    st.session_state.selected_option = "🏋️ Exercise Tracker"
elif button3:
    st.session_state.selected_option = "📊 Nutrition Planner"

# Show the appropriate content based on the selected option
if st.session_state.selected_option == "🍽️ Meal Calorie Estimator":
    meal_calorie_estimator()
elif st.session_state.selected_option == "🏋️ Exercise Tracker":
    exercise_tracker()
elif st.session_state.selected_option == "📊 Nutrition Planner":
    nutrition_planner()
