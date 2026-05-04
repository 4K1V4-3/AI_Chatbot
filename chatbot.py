# Download Python 3.10
# Set up a virtual environment with Python 3.10

# Create and activate virtual environment.
# Install ChatterBot and dependencies.
# Dependencies = Code that other people wrote that we need.

# import nltk
# nltk.download('punkt_tab')

from chatterbot import ChatBot
# Train the chatbot quickly.
from chatterbot.trainers import ListTrainer
# Import the corpus-cleaning function that we built.
from cleaner import edible_corpus


# Create chatbot and name it.
chatbot = ChatBot("Chatpot")


# ListTrainer will teach the chatbot to respond meaningfully.
# Pass the chatbot to the chatbot_trainer
# '.train()' injects entries into the database, which grow's the chatbot's list of potential replies.
chatbot_trainer = ListTrainer(chatbot)

# A couple of training sessions.
# Since we pass in an iterable with two items, the first is considered to be a statement and the second is considered to be a reply.
chatbot_trainer.train([
    "Hi",
    "Welcome, friend!"
])
chatbot_trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!"
])


# Our WhatsApp conversational data.
CORPUS_FILE = "chat.txt"
# Clean the file.
chatbot_food = edible_corpus(CORPUS_FILE)
chatbot_trainer.train(chatbot_food)


exit_conditions = (":q", "quit", "exit")

while True:
    # User makes a query to the chatbot
    query = input("> ")

    if query in exit_conditions:
        break
    else:
        # Pass user query to the chatbot
        # Chatbot responds
        print("(8 -- ", chatbot.get_response(query))

# Not working.
# Worked when I installed Python 3.10.11.


# ChatterBot stores responses in a SQLite database.
# That's how it learnt to respond 'hi' to 'hello' even within the first few runs of the program.


# Now, let's train the chatbot.
# ListTrainer will make it smarter.


# Convert WhatsApp conversation data into a format that can be used for training the chatbot.
# Download TXT file that has WhatsApp conversation history.
# Using sample WhatsApp chat data file.

# Clean WhatsApp chat export data for use as input.
# Most training data will require cleaning.
