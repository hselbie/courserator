from flask import Flask, send_file, url_for, request, jsonify, render_template
import random_points
import location_db
import os
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    course_names = location_db.get_all_shape_names()
    return render_template('index.html', courses = course_names)

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

    
@app.route('/specific_course')
def specific_course():
    course_names = location_db.get_all_shape_names()
    return render_template('specific_course.html', courses=course_names)

@app.route('/specific_course', methods=['GET','POST'])
def specific_course_post():
    point_number = request.form['new_point_number']
    point_number = int(point_number)
    location_id = request.form['course_name']
    random_points.get_specific_course(location_string=location_id, p_number=point_number)
    shutil.make_archive('course_files', 'zip', 'output/')
    download_files = os.listdir('output/')
    for file in download_files:
        os.remove(f'output/{file}')
    return send_file('course_files.zip', as_attachment=True)

@app.route('/new_shape', methods=['GET', 'POST'])
def new_shape():
    if request.method == 'POST':
        data_name = request.form['shape_name']
        shape_coords = request.form['shape_coords']
        start_coords = request.form['start_coords']
        location_db.add_to_location_library(data_name=data_name, shape_coords=shape_coords, start_coords=start_coords)
    return render_template('new_shape.html') 

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')