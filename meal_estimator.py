"""
Meal nutrient estimator using Gemini API for food image analysis.

This module uses Google's Gemini API to analyze food images and estimate
nutritional content. No external APIs (like Hugging Face) required.
"""

import google.generativeai as genai
from PIL import Image
import os
from config import configure_genai

# Configure Gemini
configure_genai()

def estimate_nutrition(image: Image.Image) -> str:
    """
    Estimate meal nutrition by analyzing an image using Gemini API.
    
    Args:
        image: PIL Image object
    
    Returns:
        Formatted nutrition string with food details and macro estimates
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    
    if not gemini_api_key:
        return "Error: GEMINI_API_KEY not found in environment. Please set it in .env file."
    
    try:
        model = genai.GenerativeModel("gemini-pro-vision")
        
        prompt = """Analyze this food image and provide:
        1. Food item name
        2. Estimated serving size
        3. Approximate calories
        4. Protein (grams)
        5. Carbohydrates (grams)
        6. Fats (grams)
        
        Format the response clearly with each detail on a new line.
        Be concise and structured."""
        
        response = model.generate_content([prompt, image])
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"
