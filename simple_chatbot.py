response = {
    "hello": "Hi there! How can I assist you?",
    "tell me about": "Sure! What would you like to know about?",
    "bye": "Goodbye! Have a great day!",
}

def get_bot_response(user_message):
    """Returns a response based on user input."""
    return response.get(user_message, "I'm not sure how to respond to that.")

def main():
    """Handles the chatbot interaction."""
    print("Welcome to the chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        response = get_bot_response(user_input)
        print("Bot:",response)

if __name__ == "__main__":
    main()

