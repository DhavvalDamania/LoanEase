from flask import Flask, request, jsonify
from flask_cors import CORS
from loan_guidance import ask_cohere
from sarvam_translate import translation
from speech_to_text import speech_to_text  # Assuming function exists
from text_to_speech import tts

app = Flask(__name__)
print("heyy1")
CORS(app)  # Allow requests from React



@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.json
    print("translate_text")
    text = data.get("text")
    source_lang = data.get("source_lang")
    target_lang = data.get("target_lang")

    if not text or not source_lang or not target_lang:
        return jsonify({"error": "Invalid input"}), 400
    
    translated_text = translation(text, source_lang, target_lang)
    return jsonify({"translated_text": translated_text})

@app.route("/loan_guidance", methods=["POST"])
def loan_guidance():
    data = request.json
    print("loan_guidance")
    question = data.get("question")
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    #response = ask_cohere(question)
    return jsonify({"response": "response"})


@app.route("/speech_to_text", methods=["POST"])
def convert_speech():
    print("convert_speech")
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    audio_file = request.files["file"]
    transcript = speech_to_text(audio_file)
    return jsonify({"transcript": transcript})

@app.route("/text_to_speech", methods=["POST"])
def convert_text_to_speech():
    data = request.json
    print("convert_text_to_speech")
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    tts([text])  # Convert text to speech
    return jsonify({"message": "Audio generated", "file": "output_audio.wav"})

if __name__ == "__main__":
    print("heyy")
    app.run(debug=True)
