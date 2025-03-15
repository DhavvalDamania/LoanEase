from googletrans import Translator

# Initialize Google Translator
translator = Translator()

def translate_text():
    """Takes user input for text, source language, and target language, then translates."""
    source_lang = input("Enter the source language code (or 'auto' for auto-detect): ")
    text = input("Enter the text to translate: ")
    target_lang = input("Enter the target language code: ")

    try:
        # Perform translation
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        print(f"\nTranslated Text ({source_lang} → {target_lang}): {translated.text}")
    
    except Exception as e:
        print(f"Error: {e}")

# Run the translation
translate_text()
