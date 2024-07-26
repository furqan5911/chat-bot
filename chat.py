
import streamlit as st
import os


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

API_KEY = "AIzaSyD4fcsx2GHbl4WNWgPkoJLof7uxmDf66MY"
genai.configure(api_key=API_KEY)



# Initialize Streamlit app
st.set_page_config(page_title="📅 Event Chatbot  ")

st.header(" ✨ Event Management Chat BOT")

# Initialize session state for chat history if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to interact with your model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Display previous messages
for message in st.session_state['messages']:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Chat input
prompt = st.chat_input("You:")

# Handle user input
if prompt:
    # Add user message to session state
    st.session_state['messages'].append({"role": "user", "content": prompt})

    # Get response from Gemini model
    response = get_gemini_response(prompt)

    # Add assistant message to session state
    st.session_state['messages'].append({"role": "assistant", "content": response})

    # Display user and assistant messages using st.chat_message
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
