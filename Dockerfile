FROM python:3.8
ADD requirements.txt ./random_gps_points/requirements.txt
COPY . /random_gps_points

WORKDIR /random_gps_points
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

ENV APP_SETTINGS settings.cfg

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 file_serve:app
