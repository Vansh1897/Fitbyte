import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=YourAPiKey)

def estimate_nutrition_gemini(image):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([
            "Identify the food in this image and give an approximate estimate of calories, protein, carbohydrates, and fats. Also mention per serving quantity (e.g., 2 bhature and 100 gm chole). Be concise and structured.and give each detail on new line.",
            image
        ])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def meal_calorie_estimator():
    st.header("📸 Live Meal Calorie Estimator")
    clicked_photo = st.camera_input("Click a live photo of your dish")

    if clicked_photo:
        image = Image.open(clicked_photo)
        
        with st.spinner("Estimating nutrition..."):
            result = estimate_nutrition_gemini(image)

        if result.startswith("Error"):
            st.error(result)
        else:
            st.success("Nutrition Estimates:")
            st.write(result)
