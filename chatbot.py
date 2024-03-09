import nltk
from nltk.chat.util import Chat, reflections

chatbot_rules = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am a chatbot, so I don\'t have feelings, but I\'m here to help.']),
    (r'what is your name', ['I am a chatbot created with NLTK.', 'You can call me ChatBot.']),
    (r'bye|goodbye', ['Goodbye!', 'It was nice chatting with you.']),
]

chatbot = Chat(chatbot_rules, reflections)

def start_chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)

nltk.download('punkt')

start_chat()