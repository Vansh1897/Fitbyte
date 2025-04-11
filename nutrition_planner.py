import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCYSlWGpX0BzDiXH_S9tWC9lxXiivt5k88")  # Replace with your key

# Convert height in feet to cm
def convert_height_to_cm(feet):
    return round(feet * 30.48)

# Calculate daily macros based on activity level
def calculate_macros(weight, goal, activity_level):
    # Base multiplier depending on goal
    if goal == "Weight Loss":
        base_cal = 22
        protein = weight * 2
    elif goal == "Weight Gain":
        base_cal = 35
        protein = weight * 2.2
    else:  # Muscle Building
        base_cal = 30
        protein = weight * 2.5

    # Activity level multiplier
    activity_multiplier = {
        "No Exercise": 1.0,
        "Little": 1.1,
        "Moderate": 1.25,
        "Heavy": 1.4
    }

    # Final calorie estimate
    calories = weight * base_cal * activity_multiplier[activity_level]
    fats = (0.25 * calories) / 9
    carbs = (calories - (protein * 4) - (fats * 9)) / 4

    return round(protein), round(carbs), round(fats), round(calories)

# Generate diet plan using Gemini
def generate_diet_plan(weight, height_cm, goal, diet_type, activity_level, protein, carbs, fats, calories):
    prompt = f"""
    Create a standard and personalized Indian {diet_type.lower()} diet plan for someone with the following info:

    Height: {height_cm} cm
    Weight: {weight} kg
    Goal: {goal}
    Activity Level: {activity_level}
    Daily Calorie Target: {calories} kcal
    Macronutrient Targets:
    - Protein: {protein}g
    - Carbs: {carbs}g
    - Fats: {fats}g

    The plan should include:
    - 5 meals: breakfast, lunch, dinner, and 2 snacks.
    - Be precise and concise (just give dish names and serving size in grams).
    - Indian food suggestions with realistic portion sizes.
    - Macro breakdown per meal (approximate).
    - Also give the total (protein, fats, etc) of all the 5 meals in the same table .
    - Balanced options to suit the fitness goal.
    - Do NOT include notes or dish alternatives.
    - Present everything in a tabular format.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Streamlit App
def nutrition_planner():
    st.header("📊 AI Nutrition Planner")

    weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200)
    height_feet = st.number_input("Enter your height in feet ", min_value=3.0, max_value=8.0, step=0.1)
    height_cm = convert_height_to_cm(height_feet)

    goal = st.selectbox("What's your goal?", ["Weight Loss", "Weight Gain", "Muscle Building"])
    diet_type = st.radio("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Mixed"])
    activity_level = st.selectbox("Activity Level", ["No Exercise", "Little", "Moderate", "Heavy"])

    if st.button("Generate Diet Plan"):
        protein, carbs, fats, calories = calculate_macros(weight, goal, activity_level)

        with st.spinner("🔍 Generating your personalized diet plan..."):
            plan = generate_diet_plan(weight, height_cm, goal, diet_type, activity_level, protein, carbs, fats, calories)

        st.success("✅ Personalized Diet Plan")
        st.write("🔬 Estimated Nutritional Needs:")
        st.write(f"- Calories: {calories} kcal")
        st.write(f"- Protein: {protein}g")
        st.write(f"- Carbs: {carbs}g")
        st.write(f"- Fats: {fats}g")

        st.markdown("---")
        st.markdown(plan)

# Run the app
nutrition_planner()
