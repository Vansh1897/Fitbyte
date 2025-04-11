import streamlit as st
import datetime

# Exercise Tracker module
def exercise_tracker():
    st.header("🏋️ Exercise Tracker")

    exercises = ["Push-ups", "Squats", "Bicep Curls", "Shoulder Press", "Deadlifts", "Crunches"]
    selected = st.multiselect("Select exercises you've done today", exercises)
    
    if selected:
        st.write("📅 Date:", datetime.date.today())
        st.success("You've performed the following exercises:")
        for ex in selected:
            st.write(f"✅ {ex}")

    else:
        st.write("No exercises selected. Please choose exercises you've done today.")
