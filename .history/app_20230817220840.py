from flask import Flask, send_file, url_for, request, jsonify, render_template
import random_points

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    point_number = request.form['point_number']
    processed_text = point_number
    return processed_text

# @app.route('/', methods=['POST'])
# def my_form_post():
#     data_name = request.form['shape_name']
#     shape_coords = request.form['shape_coords']
#     start_coords = request.form['start_coords']
#     random_points.add_to_location_library(data_name=data_name, shape_coords=shape_coords, start_coords=start_coords)

#     processed_text = data_name.upper()
#     return processed_text

@app.route('/download')
def download():
    path = 'output/lower_wilder.kml'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')