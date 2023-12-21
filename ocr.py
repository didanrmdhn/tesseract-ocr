import pytesseract
import cv2
import numpy as np

NUTRION_KEY_FILE = "nutrions.txt"

def get_nutrion_key() -> list[str]:
    with open(NUTRION_KEY_FILE, "r") as nutrions:
        nutrition_key = nutrions.read().splitlines()
    
    return nutrition_key

def preprocess_image(image: np.array) -> np.array:
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding or other preprocessing techniques as needed
    # Example: thresholding
    _, threshold_img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return threshold_img

def process_ocr(image: np.array) -> dict:
    # Preprocess image
    processed_img = preprocess_image(image)

    # perform OCR on the image
    extracted_text: str = pytesseract.image_to_string(image=processed_img, config="--psm 6 --oem 1")

    # split the text by lines
    nutrion_lines: list[str] = extracted_text.split("\n")

    # import nutrition key
    nutrition_key = get_nutrion_key()
    
    # empty dict to collect nutrion that was detected
    nutrition_data = {}

    for nk_key in nutrition_key:
        key_finded = [nl.lower() for nl in nutrion_lines if 
                      (nk_key in nl.lower())
                      ]

        if(len(key_finded) > 0):
            for nt in key_finded:
                existed_key = list(nutrition_data.keys())
                splited_nt = nt.split(" ")

                if "total" in nt or "saturate" in nt:
                    contain_key = " ".join(splited_nt[:2])
                    contain_value = " ".join(splited_nt[2:])

                    if contain_key not in existed_key:
                        nutrition_data[contain_key] = contain_value
                    
                elif "from" in nt:
                    contain_key = " ".join(splited_nt[:3])
                    contain_value = " ".join(splited_nt[3:])

                    if contain_key not in existed_key:
                        nutrition_data[contain_key] = contain_value
                elif nt.startswith(nk_key):
                    contain_key = splited_nt[:1][0]
                    contain_value = " ".join(splited_nt[1:])
                    
                    if contain_key not in existed_key:
                        nutrition_data[contain_key] = contain_value

    return nutrition_data