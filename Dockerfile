FROM python:3.10.13-slim-bullseye

# Install tesseract-ocr
RUN apt-get update \
  && apt-get -y install tesseract-ocr

# Install ubuntu image reader dependencies
RUN apt-get update \
  && apt-get install ffmpeg libsm6 libxext6 -y

# Upgrade pip
RUN pip3 install --upgrade pip

WORKDIR /app
COPY requirements.txt .

# Install python libraries
RUN pip install -r requirements.txt

# copy project file
COPY . .

CMD [ "python3", "/app/server.py" ]