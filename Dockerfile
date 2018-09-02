FROM python:3.6

WORKDIR /var/app

# Dependencies
RUN apt-get update && \
    apt-get install -y \
        libblas-dev \
        liblapack-dev \
        liblapacke-dev \
        gfortran && \
    pip install --upgrade pip setuptools wheel

COPY requirements_docker.txt ./
RUN pip install --no-cache-dir -r requirements_docker.txt

RUN pip wheel numpy
RUN pip install numpy

RUN pip wheel scipy
RUN pip install scipy

# Project files
COPY . .

# Run the migrations upfront because the sqlite database is stored in a file.
RUN python manage.py migrate

# Server
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
