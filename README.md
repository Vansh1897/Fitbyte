# 🥗 FitBite - Your Fitness Buddy

FitBite is an AI-powered fitness application that helps you track your nutrition and plan workouts using Google's Gemini AI.

## Features

- 🍽️ **Meal Calorie Estimator**: Take a photo of your meal and get instant nutritional estimates
- 🏋️ **Exercise Tracker**: Generate personalized workout plans based on your goals
- 🥗 **Nutrition Planner**: Get customized meal plans tailored to your dietary needs

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash
- **Image Processing**: PIL (Pillow)
- **Language**: Python 3.11+

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/Vansh1897/Fitbyte.git
cd Fitbyte
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run fitbite_app.py
```

## Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key and add it to your `.env` file or Streamlit secrets

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Vansh Ambalal Patil
