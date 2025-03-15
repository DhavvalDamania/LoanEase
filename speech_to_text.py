import requests

# URL for the Sarvam API
url = "https://api.sarvam.ai/speech-to-text"

# API subscription key (replace with your actual key)
api_key = "723d3b71-6d58-48ce-a1fe-eea9819daafb"

# Path to the audio file
audio_file_path = "C:\Projects\LoanEase\output_audio.wav"

# Additional parameters to send in the form data
data = {
    "with_timestamps": "false",
    "with_diarization": "false",
    "model": "saarika:v2",
    "language_code": "en-IN",
    "num_speakers": "1"
}

# Prepare the file to send
with open(audio_file_path, 'rb') as audio_file:
    files = {
        "file": (audio_file_path, audio_file, "audio/wav")
    }
    
    # Set headers, including the API key for authentication
    headers = {
        "api-subscription-key": api_key
    }
    
    # Send POST request
    response = requests.post(url, data=data, files=files, headers=headers)
    
    # Check the response
    if response.status_code == 200:
        print("Request was successful!")
        print(response.json())  # Print the response JSON (e.g., transcribed text)
    else:
        print("Error:", response.status_code)
        print(response.text)
