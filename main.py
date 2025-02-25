import os
import streamlit as st
import google.generativeai as genai

# Set up the Streamlit page configuration
st.set_page_config(page_title="Event Planning Chatbot", layout="centered")

# Set up the Google AI environment
os.environ["GEMINI_API_KEY"] = "AIzaSyDtd8ew9QCQsvy2BOV1SRYYF2gCkhoYzKg"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=(
        "You are a model built for the users of a startup that wants you to give personalized "
        "suggestions on events like color schemes, seating arrangements, budget aspects, and current "
        "trends for more reach based on the user's input dont ask any questions to the user."
    ),
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Streamlit app layout
st.title("Event Planning Chatbot")
st.write("Get personalized suggestions for your event!")

# User input
user_input = st.text_input("Enter your question or event details:")

# Chatbot response
if user_input:
    response = chat_session.send_message(user_input)
    st.write("Chatbot Response:")
    st.write(response.text)
