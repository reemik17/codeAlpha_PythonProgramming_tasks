# Function for the chatbot
def chatbot():

    print("ChatBot!")
    print("Enter 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("ChatBot: Hi!")

        elif user_input == "good morning":
            print("ChatBot: Good morning!")

        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("ChatBot: My name is BOT.")

        elif user_input == "tell me a random color":
            print("ChatBot: A random color is green.")

        elif user_input == "have a nice day":
            print("ChatBot: You too!")

        elif user_input == "bye":
            print("ChatBot: Goodbye!")
            break

        else:
            print("ChatBot: Sorry, I can't understand you.")

# Call the function
chatbot()