from text_to_speech import tts
from sarvam_translate import translation
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
source_language_code = input("Enter the source language code (e.g., 'en-IN'): ")
target_language_code = input("Enter the target language code (e.g., 'gu-IN'): ")
input_text = input("Enter the text you want to translate: ")
response = ask_cohere(input_text)
print("AI Response:", response)
chunks = split_string(response)
tts(chunks)

chunk_list_len = len(chunks)
for i in range(chunk_list_len+1):
    translated_string = ()
    translated_string += translation(chunks[i],source_language_code,target_language_code)