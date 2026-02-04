response = {
    "hello": "Hi! Welcome. How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "how are you": "I'm doing great, thank you for asking!",
    "who are you": "I am KotliBot, a smart AI assistant created to help you.",
    "what is your name": "My name is KotliBot.",
    "what can you do": "I can help you with basic questions, coding guidance, and simple conversations.",
    "thank you": "You're welcome! Happy to help.",
    "bye": "Goodbye! Have a great day.",
    "happy": "Keep going! Every bug in your project makes you a better developer.",
    "function kya hota hai": "A function is a reusable block of code that performs a specific task."
}

def get_response(user_question):
    user_question = user_question.lower().strip()

    for key, value in response.items():
        if key in user_question:
            return value

    return "I am still learning about that.."

user_input = input("Please ask your question: ")
reply = get_response(user_input)
print(reply)
