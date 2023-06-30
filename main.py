import random
import tkinter as tk

# Define some greetings
greetings = ['Hello!', 'Hi!', 'Hey there!', 'Greetings!']

# Define some responses
responses = {
    'what is your name?': 'My name is Chatbot.',
    'how are you?': 'I am doing well, thank you.',
    'what do you do?': 'I am a chatbot.',
    'bye': 'Goodbye!'
}

# Define a function to generate a response
def generate_response(user_input):
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand."

# Define a function to start the chat
def chat():
    # Define the chat window
    chat_window = tk.Tk()
    chat_window.title('Chatbot')

    # Define the chat log
    chat_log = tk.Text(chat_window, height=20, width=50)
    chat_log.grid(row=0, column=0, padx=10, pady=10)

    # Define the user input field
    user_input = tk.Entry(chat_window, width=50)
    user_input.grid(row=1, column=0, padx=10, pady=10)

    # Define the send button
    def send():
        user_message = user_input.get()
        chat_log.insert(tk.END, "You: " + user_message + "\n")
        chat_log.insert(tk.END, "Chatbot: " + generate_response(user_message) + "\n")
        user_input.delete(0, tk.END)

    send_button = tk.Button(chat_window, text='Send', command=send)
    send_button.grid(row=1, column=1, padx=10, pady=10)

    # Start the chat
    chat_window.mainloop()

chat()
