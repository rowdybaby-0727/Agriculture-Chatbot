import streamlit as st
from responses import get_response

st.set_page_config(page_title="Agriculture Chatbot")

st.title("🌾 Agriculture Chatbot")
st.write("Ask your farming-related questions!")

user_input = st.text_input("Enter your question:")

if user_input:
    response = get_response(user_input)
    st.success(response)