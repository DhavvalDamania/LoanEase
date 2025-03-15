import requests
import base64

def tts(chunks):
    # initialize empty string to store sarvam response. Each sarvam 'audio' response will be appended to this string.
    base64_audio = ""
    
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
            "api-subscription-key": "723d3b71-6d58-48ce-a1fe-eea9819daafb",
            "Content-Type": "application/json"
        }

        # Make the API request
        response = requests.post(url, json=payload, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            #print(response.text)
            jsondata = response.json()
            
            # Append audio data of each response
            base64_audio += (jsondata['audios'])[0]
        else:
            print("Error:", response.status_code, response.text)
    #end of for loop
    
    # decode appended audio data. Note that this is FULL audio data of all chunks response
    audio_data = base64.b64decode(base64_audio[0])

    with open("output_audio.wav", "wb") as audio_file:
        audio_file.write(audio_data)
        print("Audio saved as 'output_audio.wav'")



        #hello
