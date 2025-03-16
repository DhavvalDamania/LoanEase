import requests
import base64
from pydub import AudioSegment
from io import BytesIO

# Solution-2: Creates 1 audio file by combining audio using pydub/AudioSegment

def merge_audio(audio_chunks):
    # Create an empty audio file
    combined_audio = None
    
    for audio_chunk in audio_chunks:
        # Create an AudioSegment from the binary audio data
        audio = AudioSegment.from_wav(BytesIO(audio_chunk))
        
        if combined_audio is None:
            combined_audio = audio
        else:
            # Concatenate to the existing audio
            combined_audio += audio
    
    return combined_audio

def tts(chunks):
    # initialize empty string to store sarvam response. Each sarvam 'audio' response will be appended to this string.
    base64_decoded_audio_chunks = []
    
    # loop through each chunk. Call sarvam API for each chunk.
    for chunk in chunks:
        url = "https://api.sarvam.ai/text-to-speech"

        payload = {
            "inputs": [chunk],
            "target_language_code": "en-IN",
            "speaker": "meera",
            "pitch": 0,
            "pace": 1.65,
            "loudness": 1.5,
            "speech_sample_rate": 8000,
            "enable_preprocessing": False,
            "model": "bulbul:v1",
            "eng_interpolation_wt": 123,
            "override_triplets": {}
        }
        headers = {
            "api-subscription-key": "API-KEY",
            "Content-Type": "application/json"
        }

        # Make the API request
        response = requests.post(url, json=payload, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            #print(response.text)
            jsondata = response.json()
            
            # decode audio data.
            audio_data = base64.b64decode((jsondata['audios'])[0])
            # append decoded data to our list 
            base64_decoded_audio_chunks.append(audio_data)
        
        else:
            print("Error:", response.status_code, response.text)
    #end of for loop
    
    # combine decoded audio chunks
    merged_audio = merge_audio(base64_decoded_audio_chunks)
    
    #with open("output_audio.wav", "wb") as audio_file:
    #    audio_file.write(merged_audio)
    #    print("Audio saved as 'output_audio.wav'")
    
    # Export the merged audio to a file
    merged_audio.export("output_audio.wav", format="wav")
    print("Audio saved as 'output_audio.wav'")

