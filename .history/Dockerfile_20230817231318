FROM python:3.8
ADD requirements.txt ./random_gps_points/requirements.txt
COPY . /random_gps_points

WORKDIR /random_gps_points
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

ENV APP_SETTINGS settings.cfg

# ENTRYPOINT ["python"]
CMD ["flask", "run", "--host", "0.0.0.0"]

