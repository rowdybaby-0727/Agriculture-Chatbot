import streamlit as st

def get_response(user_input):
    user_input = user_input.lower()

    if "crop" in user_input:
        return "You can grow rice, wheat, maize based on your region."

    elif "soil" in user_input:
        return "Soil should be fertile and well-drained."

    elif "water" in user_input:
        return "Crops need proper irrigation."

    elif "fertilizer" in user_input:
        return "Use organic or chemical fertilizers."

    else:
        return "Sorry, I don't understand. Ask farming questions."

st.title("🌾 Agriculture Chatbot")

user_input = st.text_input("Enter your question:")

if user_input:
    st.success(get_response(user_input))