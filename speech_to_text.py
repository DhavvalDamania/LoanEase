import requests
import base64
from text_to_speech import tts
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

# Function to split a string into chunks (for TTS)
def split_string(input_string):
    chunks = []
    if len(input_string) > 500:
        for i in range(0, len(input_string), 500):
            chunks.append(input_string[i:i+500])
    else:
        chunks.append(input_string)
    return chunks

# Function to convert speech to text using Sarvam API
def speech_to_text(audio_file_path):
    url = "https://api.sarvam.ai/speech-to-text"
    
    headers = {
        "api-subscription-key": "723d3b71-6d58-48ce-a1fe-eea9819daafb",  # Replace with your subscription key
        "Content-Type": "application/json"
    }
    
    # Read the audio file
    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()

    # Prepare payload with audio in base64
    payload = {
        "audio": base64.b64encode(audio_data).decode("utf-8"),
        "language_code": "en-IN",  # Change this to the correct language code
        "model": "s2t:v1"  # Specify the model if required by the API
    }

    response = requests.post(url, json=payload, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        jsondata = response.json()
        return jsondata['text']
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Main function to run the assistant
def run_assistant():
    # Step 1: Record speech input and save it as an audio file
    audio_file_path = "output_audio.wav"  # Replace with actual file path if necessary
    print("Please speak into the microphone...")
    # In practice, you can use your microphone to record the audio, or upload an audio file.
    # (You might use a microphone library to save the input as an audio file.)

    # Step 2: Convert speech to text
    user_input = speech_to_text(audio_file_path)
    if user_input is None:
        return

    print(f"User Input (Text): {user_input}")

    # Step 3: Ask Cohere AI for a response
    response = ask_cohere(user_input)
    print("AI Response:", response)

    # Step 4: Split the response for TTS
    chunks = split_string(response)

    # Step 5: Convert AI response to speech
    tts(chunks)

# Run the assistant
run_assistant()