import numpy as np
from flask import Flask, jsonify, request, abort
import cv2
from ocr import process_ocr
import os

app = Flask(__name__)

SERVER_PORT = os.getenv("PORT", 7000)

@app.route("/ocr/process", methods=["POST"])
def align_document():
    if request.method == "POST":
        if request.files:
            try:
                image = request.files["image"]
                image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

                ocr_result = process_ocr(image)

                return jsonify(
                    {
                        "result": ocr_result
                    }
                )
            except Exception:
                abort(400, "image not valid")
        else:
            abort(404, "image not found")


if __name__ == "__main__":
    app.run("0.0.0.0", SERVER_PORT, debug=True)