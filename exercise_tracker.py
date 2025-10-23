import streamlit as st
import google.generativeai as genai
from config import configure_genai

# Configure Gemini API from environment
configure_genai()

# AI workout generator function
def generate_ai_workout(goal, experience):
    prompt = f"""
    Create a personalized gym workout routine for a person whose goal is {goal} and has {experience} experience level.
    - Include push, pull, and legs movements based on days like monday, tuesday, wednesday, and so on excluding sunday.
    - Suggest 6-8 exercises.
    - Include sets and reps.
    - Format it in clean bullet points or table.
    - Do not give extra notes or alternatives.
    - Display it in a tabular format.
    - Do not show any warnings or any other text rather than the table.
    - Give the same output everytime by storing the previous results in memory.
    """
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating workout: {str(e)}"

# Main app function
def exercise_tracker():
    st.header("🏋️ Exercise Planner")

    # Initialize workout list if not in session state
    if "workout_list" not in st.session_state:
        st.session_state.workout_list = []

    # Tabs: Add Exercises and AI Workout
    tab1, tab2 = st.tabs(["➕ Add Exercises", "🤖 AI-Generated Workout"])

    with tab1:
        st.subheader("Manually Add Exercises")

        # Muscle groups and exercises dictionary
        muscle_group = st.selectbox("Target Muscle Group", [
            "Chest", "Back", "Legs", "Shoulders", "Biceps", "Triceps", "Abs"
        ])

        exercises = {
            "Chest": ["Flat Bench Press", "Incline Bench Press", "Decline Bench Press", "Dumbbell Fly", "Cable Crossover", "Chest Dips", "Push-Ups", "Incline Dumbbell Press"],
            "Back": ["Deadlift", "Lat Pulldown", "Seated Cable Row", "Bent-over Barbell Row", "Pull-Ups", "T-Bar Row", "One-Arm Dumbbell Row", "Hyperextensions"],
            "Legs": ["Barbell Squats", "Leg Press", "Walking Lunges", "Leg Extension (Machine)", "Hamstring Curl (Machine)", "Romanian Deadlifts", "Bulgarian Split Squats", "Standing Calf Raises"],
            "Shoulders": ["Overhead Press", "Arnold Press", "Lateral Raise", "Front Raise", "Rear Delt Fly", "Upright Row", "Dumbbell Shoulder Press", "Face Pulls"],
            "Biceps": ["Barbell Curl", "EZ Bar Curl", "Dumbbell Hammer Curl", "Concentration Curl", "Preacher Curl", "Cable Curl", "Incline Dumbbell Curl", "Spider Curl"],
            "Triceps": ["Close-Grip Bench Press", "Skull Crushers", "Tricep Dips", "Tricep Pushdown (Cable)", "Overhead Dumbbell Extension", "Rope Pushdown", "Kickbacks", "Diamond Push-Ups"],
            "Abs": ["Crunches", "Hanging Leg Raises", "Plank", "Russian Twists", "Bicycle Crunches", "Cable Crunches", "Mountain Climbers", "Toe Touches"]
        }

        selected_exercise = st.selectbox("Choose Exercise", exercises[muscle_group])
        sets = st.number_input("Sets", min_value=1, max_value=6, value=3)
        reps = st.number_input("Reps", min_value=1, max_value=20, value=12)

        if st.button("Add to Workout"):
            exercise_entry = f"{selected_exercise} - {sets} sets x {reps} reps"
            st.session_state.workout_list.append(exercise_entry)
            st.success(f"✅ Added: {exercise_entry}")

        if st.session_state.workout_list:
            st.write("### 📝 Current Workout Plan")
            for i, entry in enumerate(st.session_state.workout_list, 1):
                st.write(f"{i}. {entry}")

            if st.button("Clear Workout"):
                st.session_state.workout_list.clear()
                st.success("🗑️ Cleared workout list.")
        else:
            st.write("No workouts added yet.")

    with tab2:
        st.subheader("AI Workout Generator")

        goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Endurance"])
        experience = st.radio("Experience Level", ["Beginner", "Intermediate", "Advanced"])

        if st.button("Generate AI Workout"):
            with st.spinner("Generating workout plan..."):
                plan = generate_ai_workout(goal, experience)
            st.markdown("### 💡 Your AI-Generated Workout Plan")
            st.markdown(plan)


