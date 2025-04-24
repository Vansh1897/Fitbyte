import streamlit as st
from meal_calorie_estimator import meal_calorie_estimator
from exercise_tracker import exercise_tracker
from nutrition_planner import nutrition_planner

st.set_page_config(page_title="FitBite", layout="centered")
st.title("🥗 FitBite - Your Fitness Buddy")

menu = st.sidebar.selectbox("Choose an option", ["🍽️ Meal Calorie Estimator", "🏋️ Exercise Tracker", "📊 Nutrition Planner"])

if menu == "🍽️ Meal Calorie Estimator":
    meal_calorie_estimator()
elif menu == "🏋️ Exercise Tracker":
    exercise_tracker()
elif menu == "📊 Nutrition Planner":
    nutrition_planner()
