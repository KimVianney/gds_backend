import json
from glob import glob

from flask import Flask, jsonify, request

import file_utils
from ai_model import utils
from uploads.ai_model.prediction import MODEL_PATH, predict

app = Flask(__name__)


IMAGE_UPLOADS = "image_uploads"
IMAGE_UPLOAD_RESULTS = "image_upload_results"

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    image_urls = data["images"]
    if not len(image_urls):
        return json([]), 200

    file_utils.download_images(urls=image_urls, uploads_dir=IMAGE_UPLOADS)

    images = glob(f"{IMAGE_UPLOADS}/*.jpg")
    for image in images:
        prob, label, description = predict(MODEL_PATH, image)

    file_utils.delete_uploads(uploads_dir=IMAGE_UPLOADS)

    #Upload to cloud and delete image locally
    result_uploads = file_utils.upload_results(IMAGE_UPLOAD_RESULTS)

    image_results = []


if __name__ == "__main__":
    app.run(debug=True)