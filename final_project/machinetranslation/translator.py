
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates English text to French using the MyMemoryTranslator API.

    Args:
        english_text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    print(french_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English using the MyMemoryTranslator API.

    Args:
        french_text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    print(english_text)
    return english_text
