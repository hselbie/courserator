from flask import (Flask, send_file, url_for, jsonify, render_template)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/download')
def download():
    path = 'output/lower_wilder.kml'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')