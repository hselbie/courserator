from flask import Flask, send_file, url_for, request, jsonify, render_template
import random_points

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    data_name = request.form['name']
    data_coords = request.form['coords']
    processed_text = data_name.upper()
    return processed_text

# @app.route('/handle_data', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         shape_name = request.form['shape_name']
#         shape_coords = request.form['shape_coords']
#         start_coords = request.form['start_coords']
#     return render_template('index.html')

@app.route('/download')
def download():
    path = 'output/lower_wilder.kml'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')