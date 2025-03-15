import requests

url = "https://api.sarvam.ai/translate"

input_text = input("Enter the text you want to translate: ")
source_language_code = input("Enter the source language code (e.g., 'en-IN'): ")
target_language_code = input("Enter the target language code (e.g., 'gu-IN'): ")

payload = {
    "input": input_text,
    "source_language_code": source_language_code,
    "target_language_code": target_language_code,
    "speaker_gender": "Female",
    "mode": "formal",
    "model": "mayura:v1",
    "enable_preprocessing": False,
    "output_script": "fully-native",
    "numerals_format": "international"
}

headers = {
    "api-subscription-key": "723d3b71-6d58-48ce-a1fe-eea9819daafb",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)



