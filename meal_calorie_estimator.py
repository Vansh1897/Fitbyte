import streamlit as st
from PIL import Image
from meal_estimator import estimate_nutrition

def meal_calorie_estimator():
    st.header("📸 Live Meal Calorie Estimator")
    clicked_photo = st.camera_input("Click a live photo of your dish")

    if clicked_photo:
        image = Image.open(clicked_photo)
        
        with st.spinner("Analyzing your meal..."):
            result = estimate_nutrition(image)

        if result.startswith("Error"):
            st.error(result)
        else:
            st.success("Nutrition Estimates:")
            st.write(result)
