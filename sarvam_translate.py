import requests

url = "https://api.sarvam.ai/translate"


def translation(input_string,source_lang,target_lang):
    payload = {
        "input": input_string,
        "source_language_code": source_lang,
        "target_language_code": target_lang,
        "speaker_gender": "Female",
        "mode": "formal",
        "model": "mayura:v1",
        "enable_preprocessing": False,
        "output_script": "fully-native",
        "numerals_format": "international"
    }


    headers = {
        "api-subscription-key": "API-KEY",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

