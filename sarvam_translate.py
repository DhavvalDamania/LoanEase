import requests

url = "https://api.sarvam.ai/translate"

payload = {
    "input": "hello how are you",
    "source_language_code": "en-IN",
    "target_language_code": "gu-IN",
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