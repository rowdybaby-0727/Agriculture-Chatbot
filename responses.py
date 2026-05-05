def get_response(user_input):
    user_input = user_input.lower()

    if "crop" in user_input:
        return "You can grow rice, wheat, maize based on your region."

    elif "soil" in user_input:
        return "Soil should be fertile and well-drained."

    elif "water" in user_input:
        return "Crops need proper irrigation depending on type."

    elif "fertilizer" in user_input:
        return "Use organic or chemical fertilizers based on soil condition."

    else:
        return "Sorry, I don't understand. Please ask agriculture-related questions."