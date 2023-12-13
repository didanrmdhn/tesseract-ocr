import pytesseract
import cv2
import pytesseract
import numpy as np

NUTRION_KEY_FILE = "nutrions.txt"

def get_nutrion_key() -> list[str]:
    with open(NUTRION_KEY_FILE, "r") as nutrions:
        nutrition_key = nutrions.read().splitlines()
    
    return nutrition_key

def process_ocr(image: np.array) -> dict:
    # convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # perform OCR on the image
    extracted_text: str = pytesseract.image_to_string(image=img_gray)
    
    # split the text by lines
    nutrion_lines: list[str] = extracted_text.split("\n")

    # import nutrition key
    nutrition_key = get_nutrion_key()
    
    # empty dict to collect nutrion that was detected
    nutrition_data = {}

    for nk_key in nutrition_key:
        key_finded = [nl.lower() for nl in nutrion_lines if nk_key in nl.lower()]

        if(len(key_finded) > 0):
            nutrion_contained = key_finded[0].split(nk_key)[-1].strip()
            nutrition_data[nk_key] = nutrion_contained
    
    return nutrition_data