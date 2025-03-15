import requests
from pydub import AudioSegment

def split_audio(audio_path, chunk_duration_ms):
    """
    Splits an audio file into smaller chunks of specified duration.

    Args:
        audio_path (str): Path to the audio file to be split.
        chunk_duration_ms (int): Duration of each chunk in milliseconds.

    Returns:
        list: A list of AudioSegment objects representing the audio chunks.
    """
    audio = AudioSegment.from_file(audio_path)  # Load the audio file
    chunks = []
    if len(audio) > chunk_duration_ms:
        # Split the audio into chunks of the specified duration
        for i in range(0, len(audio), chunk_duration_ms):
            chunks.append(audio[i:i + chunk_duration_ms])
    else:
        # If the audio is shorter than the chunk duration, use the entire audio
        chunks.append(audio)
    return chunks

# URL for the Sarvam API for speech-to-text
url = "https://api.sarvam.ai/speech-to-text"

# API subscription key
api_key = "723d3b71-6d58-48ce-a1fe-eea9819daafb"

# Path to the audio file
audio_file_path = "C:\Projects\LoanEase\output_audio.wav"

# max duration in ms
max_chunk_duration_ms = 30 * 1000

# split audio into multiple chunks
audio_chunks = split_audio(audio_file_path, max_chunk_duration_ms)

# variable to store full transcription
full_text = []

# iterate through each audio chunk and send to sarvam API to convert speech to text 
for chunk in audio_chunks:
    # Convert AudioSegment chunk to byte data
    with open("temp_audio.wav", "wb") as f:
        chunk.export(f, format="wav")

    # Additional parameters to send in the form data
    data = {
        "with_timestamps": "false",
        "with_diarization": "false",
        "model": "saarika:v2",
        "language_code": "en-IN",
        "num_speakers": "1"
    }

    # Prepare the file to send
    with open(temp_audio.wav, 'rb') as audio_file:
        files = {
            "file": (temp_audio.wav, audio_file, "audio/wav")
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
            full_text += response.json()
        else:
            print("Error:", response.status_code)
            print(response.text)
# end of for loop

print("Fully converted text: ",full_text)
