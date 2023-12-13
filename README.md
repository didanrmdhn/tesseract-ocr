# Nutrion Food Detection
It uses OCR to extract text from image and find pattern of the extracted text using nutrition wordlist on `nutrions.txt`


# Requirement

### Pre-installed runtime OCR
it's use `tesseract` to extract text from image. you have to install this dependency on your isolated-container or OS-host. How to install? check this docs [tesseract](https://tesseract-ocr.github.io/).

```sh
# simple install on ubuntu
$ sudo apt update -y && sudo apt install tesseract-ocr -y
```

### Python libraries
```sh
pytesseract==0.3.10
opencv-contrib-python==4.8.0.76
pillow==9.4.0
flask==3.0.0
```

# How to run

### Using docker compose
Ensure you have installed docker compose. It will be execute `docker-compose.yaml` manifest file. You can change server `PORT` on `environment` section (value that define on `ports` and `expose` should same with PORT value). Default `PORT` running at `7000`
```sh
$ docker compose up -d
```

### Add nutrition wordlist key
You can also add nutrion list to detect. Already provide predefined wordlist below:
```sh
protein
fat
sodium
potassium
carbohydrate
etc
```