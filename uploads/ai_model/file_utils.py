import os
import shutil
from glob import glob

import cloudinary
import cloudinary.uploader
import requests


cloudinary.config(
    # cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    # api_key=os.getenv('CLOUDINARY_API_KEY'),
    # api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    cloud_name="djw9uakpw",
    api_key="768436774682467",
    api_secret="AZwtp-pANj2gR2WVRywlj2eZNkw",
    secure=True
)


def download_images(urls, uploads_dir):
    """Download images from urls"""
    for url in urls:
        filename = f"{uploads_dir}/{urls.index(url)}.jpg"
        with open(filename, "wb") as f:
            f.write(requests.get(url).content)


def delete_uploads(uploads_dir):
    """Delete uploads from given directory"""
    for f in os.listdir(uploads_dir):
        path = os.path.join(uploads_dir, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def upload_results(results_dir):
    """Upload result images and return list of arrays"""
    result_images = glob(f"{results_dir}/*.jpg")
    defect_uploads = []
    for f in result_images:
        response = cloudinary.uploader.upload(f)
        defect_uploads.append(response["url"])
        os.remove(f)

    return defect_uploads
