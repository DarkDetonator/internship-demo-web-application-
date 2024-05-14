from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the translator1.html template"""
    return render_template('translator1.html')

@app.route('/translate', methods=['POST'])
def translate():
    """Handles translation requests and returns translated text"""
    if request.method == 'POST':
        text = request.form['text']
        src_lang = request.form['src_lang']
        dest_lang = request.form['dest_lang']
        
        # Translate text
        translator = Translator()
        translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text

        return render_template('translator1.html', translated_text=translated_text)
    
    return render_template('translator1.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
