# cleaner module to be used in chatbot file.
# Clean data before using it to train the chatbot.
# Date, time, and username are all pieces of metadata that make the chat history dirty.
# We need to preprocess the data and clean that off.

import re
# Work with regular expressions
# Regular Expressions = Rules regarding matching text.

# Function for removing metadata from each line of the chat log.
# Metadata format: '9/15/22, 14:50 - Philipp:'
def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # "9/16/22, 06:34"
    # '\d' = Digit, '+' = 1 or more, '\s' = Whitespace
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Martin"
    # '\w' = letters/numbers
    # '[\w\s]' = One letter/number or one space
    # ([\w\s]+) = One or more letter, or one or more number.
    # ?
    metadata_end = r":\s"  # ": "
    # 
    message_pattern = date_time + dash_whitespace + username + metadata_end

    # Open 'chat.txt' file
    # Open for purposes of reading the file.
    # Corpus File = File that the chatbot consumes to become more powerful.
    # Use 'with' to ditch the need for automatic file handling after the program ends.
    with open(chat_export_file, "r") as corpus_file:
        # Read the data into 'content'.
        content = corpus_file.read()
    # Subtitution
    # Take the 'content', substitute every instance of 'message_pattern' with '""'.
    cleaned_corpus = re.sub(message_pattern, "", content)
    # First, we make 'cleaned_corpus' into a giant list, with every element being a line in the 'cleaned_corpus'.
    # Then, we convert that list into a tuple.
    # We want to feed the bot line by line.
    return tuple(cleaned_corpus.split("\n"))


# Function for removing other unwanted text
def remove_non_message_text(export_text_lines):
    # 1 to -1, not including -1.
    # This removes line 0 and the last line.
    # Message with first and last line excluded, since they have unwanted data.
    messages = export_text_lines[1:-1]
    # The comma makes this a tuple.
    # Add messages that should be filtered out.
    filter_out_msgs = ("<Media omitted>",)
    # Generator expression + condition.
    # Generator expressions are helpful because they don't require space in memory for loading the tuple.
    # This returns a generator object and loads it into the tuple. No memory is accessed in the process.
    # As long as 'msg' is not found in the list of messages that we filter out, for each message in the list of messages, add the message to the tuple.
    return tuple((msg for msg in messages if msg not in filter_out_msgs))


# This function does the cleaning work.
def edible_corpus(chat_export_file):
    clean_corpus = remove_chat_metadata(chat_export_file)
    even_cleaner_corpus = remove_non_message_text(clean_corpus)
    return even_cleaner_corpus