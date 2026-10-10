import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel("gemini-3.6-flash")

# Page configuration
st.set_page_config(
    page_title="AI Recipe Creator",
    page_icon="🍳"
)

# Title
st.title("🍳 AI Recipe Creator")
st.write("Enter the ingredients you have at home and AI will create a recipe for you!")

# User input
ingredients = st.text_area(
    "🥕 Enter your available ingredients",
    placeholder="Example: Egg, Onion, Tomato, Rice"
)

# Generate button
if st.button("🍽️ Generate Recipe"):

    if ingredients.strip() == "":
        st.warning("Please enter some ingredients.")

    else:
        prompt = f"""
        You are an AI recipe creator.

        The user has these ingredients:
        {ingredients}

        Create a simple recipe using these ingredients.

        Give the answer in exactly this format:

        Recipe Name:
        
        Cooking Time:

        Ingredients:
        - ingredient 1
        - ingredient 2

        Steps:
        1. Step one
        2. Step two
        3. Step three

        Keep the instructions simple and easy to understand.
        """

        # Send prompt to LLM
        response = model.generate_content(prompt)

        # Display result
        st.subheader("🍴 Your AI Generated Recipe")

        st.write(response.text)