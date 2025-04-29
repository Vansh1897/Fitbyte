import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=YourAPIKey)

def convert_height_to_cm(feet):
    return round(feet * 30.48)

def calculate_macros(weight, goal, activity_level):
    if goal == "Weight Loss":
        base_cal = 22
        protein = weight * 2
    elif goal == "Weight Gain":
        base_cal = 35
        protein = weight * 2.2
    else:
        base_cal = 30
        protein = weight * 2.5

    activity_multiplier = {
        "No Exercise": 1.0,
        "Little": 1.1,
        "Moderate": 1.25,
        "Heavy": 1.4
    }

    calories = weight * base_cal * activity_multiplier[activity_level]
    fats = (0.25 * calories) / 9
    carbs = (calories - (protein * 4) - (fats * 9)) / 4

    return round(protein), round(carbs), round(fats), round(calories)

def generate_diet_plan(weight, height_cm, goal, diet_type, activity_level, protein, carbs, fats, calories):
    prompt = f"""
    Create a structured Indian {diet_type.lower()} diet plan for:
    - Height: {height_cm} cm
    - Weight: {weight} kg
    - Goal: {goal}
    - Activity Level: {activity_level}
    - Calories: {calories}
    - Protein: {protein}g, Carbs: {carbs}g, Fats: {fats}g

    Include 5 meals (breakfast, lunch, dinner, and 2 snacks) with:
    - Dish names & quantity
    - Macro breakdown per meal
    - Total macros at bottom
    - Present as table, no notes.
    - dont show any warning or another texts rather than the table 
    
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def nutrition_planner():
    st.header("📊 AI Nutrition Planner")
    weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, value=70)
    height_feet = st.number_input("Enter your height in feet", min_value=3.0, max_value=8.0, step=0.1, value=5.8)
    height_cm = convert_height_to_cm(height_feet)
    goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Muscle Building"])
    diet_type = st.radio("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Mixed"])
    activity_level = st.selectbox("Activity Level", ["No Exercise", "Little", "Moderate", "Heavy"])

    if st.button("Generate Diet Plan"):
        protein, carbs, fats, calories = calculate_macros(weight, goal, activity_level)

        with st.spinner("Generating your personalized diet plan..."):
            plan = generate_diet_plan(weight, height_cm, goal, diet_type, activity_level, protein, carbs, fats, calories)

        st.success("✅ Personalized Diet Plan")
        st.write("🔬 Estimated Nutritional Needs:")
        st.write(f"- Calories: {calories} kcal")
        st.write(f"- Protein: {protein}g")
        st.write(f"- Carbs: {carbs}g")
        st.write(f"- Fats: {fats}g")
        st.markdown("---")
        st.markdown(plan)
