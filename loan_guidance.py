from text_to_speech import tts
from translate import translate_text
import cohere

# Initialize Cohere with your API key
co = cohere.Client("ciyLysedyglHcElwYwdof1d4dTarreqS9AuttM6d")  # Replace with your actual API key

# Function to ask a question
def ask_cohere(question):
    response = co.generate(
        model="command",  # Free-tier model
        prompt=question,
        max_tokens=300  # Adjust response length
    )
    return response.generations[0].text.strip()

def split_string(input_string):
    # List to hold the chunks of 500 characters each
    chunks = []
    
    # Check if the string is longer than 500 characters
    if len(input_string) > 500:
        # Break the string into chunks of 500 characters each
        for i in range(0, len(input_string), 500):
            chunks.append(input_string[i:i+500])
    else:
        # If the string is less than 500 characters, just append the entire string as one chunk
        chunks.append(input_string)
    return chunks

# Test the assistant
source_lang = input("which language do you want to write the question in:")
question = input("What question do you want to ask to our chatbot:")
response = ask_cohere(question)
print("AI Response:", response)
chunks = split_string(response)
tts(chunks)