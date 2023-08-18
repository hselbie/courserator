from flask import Flask, send_file, url_for, request, jsonify, render_template
import random_points
import os
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    point_number = request.form['point_number']
    point_number = int(point_number)
    random_points.main(p_number=point_number)
    shutil.make_archive('course_files', 'zip', 'output/')
    download_files = os.listdir('output/')
    for file in download_files:
        os.remove(f'output/{file}')
    return send_file('course_files.zip', as_attachment=True)

@app.route('/new_shape', methods=['POST'])
def new_shape():
    # data_name = request.form['shape_name']
    # shape_coords = request.form['shape_coords']
    # start_coords = request.form['start_coords']
    # random_points.add_to_location_library(data_name=data_name, shape_coords=shape_coords, start_coords=start_coords)

    # processed_text = data_name.upper()
    return render_template('upload_shape.html') 

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')