responses = {
    "crop": "You can grow rice, wheat, maize based on your region.",
    "fertilizer": "Use organic fertilizers like compost for better soil health.",
    "pest": "Use neem oil or bio pesticides to control pests.",
    "weather": "Check local weather forecast before planting.",
    "soil": "Test soil quality before choosing crops."
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I didn't understand. Ask about crops, soil, fertilizer, etc."