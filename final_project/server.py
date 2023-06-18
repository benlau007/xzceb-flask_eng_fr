from flask import Flask, render_template, request
import machinetranslation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french():
    # get the input text from the request parameter
    input_text = request.form['input_text']
    
    # translate the text using the machinetranslation package
    translated_text = machinetranslation.english_to_french(input_text)
    
    # return the translated text as a response
    return translated_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    # get the input text from the request parameter
    input_text = request.form['input_text']
    
    # translate the text using the machinetranslation package
    translated_text = machinetranslation.french_to_english(input_text)
    
    # return the translated text as a response
    return translated_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
