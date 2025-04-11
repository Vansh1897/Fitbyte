import streamlit as st
from PIL import Image
import google.generativeai as genai

# Set your Gemini API key here
genai.configure(api_key="AIzaSyCYSlWGpX0BzDiXH_S9tWC9lxXiivt5k88")  # Replace with your API key

# Function to get nutrition estimates using Gemini 1.5 Flash
def estimate_nutrition_gemini(image):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([
            "Identify the food in this image and give an approximate estimate of calories, protein, carbohydrates, and fats. And also tell that whats the per serving quantity (ex. in chole bhature per serving is 2 bhature and 100 gm chole ) Be concise and structured.",
            image
        ])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
def meal_calorie_estimator():
    st.header("📸 Live Meal Calorie Estimator (Gemini 1.5 Flash)")

    # Use live camera input
    clicked_photo = st.camera_input("Click a live photo of your dish")

    if clicked_photo is not None:
        image = Image.open(clicked_photo)
        st.image(image, caption="Captured Dish", use_column_width=True)
        st.write("🔍 Estimating nutrition using Gemini 1.5 Flash...")

        result = estimate_nutrition_gemini(image)

        if result.startswith("Error"):
            st.error(result)
        else:
            st.success("Nutrition Estimates:")
            st.write(result)
