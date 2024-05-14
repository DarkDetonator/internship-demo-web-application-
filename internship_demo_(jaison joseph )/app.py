from flask import Flask
from flask import render_template
from flask import request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        translated_text = translator.translate(text, src='en', dest='es').text
        return render_template('translator1.html', original=text, translated=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
