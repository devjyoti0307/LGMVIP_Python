import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there!']),
    (r'what is your name?', ['I am a chatbot created in Python.', 'You can call me Python Bot.']),
    (r'how are you?', ['I am just a program, but I am doing fine. How can I assist you?', 'I am doing well, thank you!']),
    (r'what can you do?', ['I can have a conversation with you and answer some basic questions.', 'I can chat with you about various topics.']),
    (r'quit|exit|bye', ['Goodbye! Have a nice day!', 'See you later!']),
    (r'(.*)', ['Sorry, I did not understand that.', 'Can you please rephrase?'])
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat_with_bot():
    print("Hello! I am your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_bot()
