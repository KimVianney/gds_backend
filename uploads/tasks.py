import os
import json
from glob import glob

from celery import shared_task
from decouple import config

import requests
from django.conf import settings

from .models import ImageUpload, UploadResult
from .ai_model import prediction, utils
from .ai_model.prediction import process_image, predict
from .ai_model import file_utils
from .serializers import CreateUploadResultSerializer

# AI_MODEL_API = config('AI_MODEL_API')

# @shared_task
# def get_image_upload_results(pk):
#     """
#     Get image upload results
#     """
#     try:
#         image_upload = ImageUpload.objects.get(pk=pk)
#     except ImageUpload.DoesNotExist:
#         return 

#     data = {'images': image_upload.images}
#     headers = {'Content-Type': 'application/json'}

#     response = requests.post(AI_MODEL_API, json=data, headers=headers)
#     results = response.json()
#     for i in results:
#         i['results'] = json.dumps(i['results'])

#     serializer = CreateUploadResultSerializer(data=results, many=True)
#     if  not serializer.is_valid():
#         return 

#     serializer.save(image_upload=image_upload)

# MODEL_PATH = './ai_model/gds_pytorch_model_new.pth'

# MODEL_PATH = settings.MODEL_PATH + "\gds_pytorch_model_new.pth"

@shared_task
def get_image_upload_results(pk):
    """
    Get image upload results
    """
    try:
        image_upload = ImageUpload.objects.get(pk=pk)
    except ImageUpload.DoesNotExist:
        return
    results = []

    image_urls = image_upload.images
    print(len(image_urls))
    
    file_utils.download_images(urls=image_urls, uploads_dir=settings.IMAGE_UPLOADS)

    images = glob(f"{settings.IMAGE_UPLOADS}/*.jpg")
    for i, image in enumerate(images):
        print(image)
        prob, label, result_description = predict(settings.MODEL_PATH, image)
       

        # Upload to cloud and delete image locally
        # res_filepath = f"{settings.RESULT_IMAGE_UPLOADS}/{i}.jpg"
        res_filepath = f"{settings.RESULT_IMAGE_UPLOADS}\{i}.jpg"
        result_uploads = utils.imsave(process_image(image), res_filepath)
        result_uploads = file_utils.upload_results(settings.RESULT_IMAGE_UPLOADS)

        file_utils.delete_uploads(uploads_dir=settings.IMAGE_UPLOADS)
         
        image_result = {
            "image": image_urls[i],
            "image_class": label,
            "results": result_description,
            "result_image": result_uploads
        }
        
        results.append(image_result)
    
    print(f"===========================TASK COMPLETE: ==============================")
    for i in range(len(results)):
        UploadResult.objects.create(
            image_upload=image_upload,
            image=results[i]["image"],
            image_class=results[i]["image_class"],
            results=results[i]["results"],
            # result_image=results[i]["result_image"]
        )



    


    

    

    

    



    