import json
import argparse
from PIL import Image
import numpy as np
import torch
from torchvision import models, datasets, transforms
from .utils import load_gpu, load_checkpoint

MODEL_PATH = "gds_pytorch_model_new.pth"
FILE_SAVE_DIR = "image_uploads_results"


def process_image(image):
    image = Image.open(image).convert('RGB')
    image.thumbnail((256, 256))
    width, height = image.size
    
    # Crop the image
    n_width, n_height = 224, 224
    crop_params = np.array([
        (width - n_width),
        (height - n_height),
        (width + n_width),
        (height + n_height)]) / 2
    
    # Crop image to be fed into network
    image = image.crop((crop_params[0], crop_params[1], crop_params[2], crop_params[3]))
    
    # Transform image to tensor
    tensor = transforms.ToTensor()
    normalize = transforms.Normalize([0.485, 0.456, 0.406], 
                                     [0.229, 0.224, 0.225])
    
    image_tensor = normalize(tensor(image))
    return image_tensor

def predict(modelpath: str, image):
    """
    Run inference with the vgg16 model 
    """
    # Define class mapping
    mapping = {
        0: 'Normal Eyes / Glaucoma Negative',
        1: 'Glaucoma affected eyes'
    }
    # Load GPU if available
    device = load_gpu()

    # Load model using path
    model = load_checkpoint(modelpath, device)

    #Set topk value
    topk = 2

    # Process image and run inference
    processed_image = process_image(image)
    processed_image = torch.unsqueeze(processed_image, 0).to(device).float()

    # Prepare model for eval
    model.to(device)
    model.eval()

    # Begin evaluation
    logps = model(processed_image)
    ps = torch.exp(logps)
    top_ps, top_idx = ps.topk(topk, dim=1)

    top_ps = np.array(top_ps.detach().cpu())[0]
    top_idx = np.array(top_idx.detach().cpu())[0]

    top_labels = [mapping[idx] for idx in top_idx]

    results_description = ""
    
    if top_idx[0] == 0:
        results_description = f"""This eye image is normal with a confidence level of {top_ps[0] / 1 * 100} %. 
                                There has not been any significant sign of glaucoma found. Please continue doing regular 
                                eye check ups and practice eye care routines to protect your sight.
        """
        return top_ps[0], top_labels[0], results_description
    else:
        results_description = f"""This eye image presents significant signs of Glaucoma with a confidence level of {top_ps[0] / 1 * 100} %. 
                                We advise the patient to seek immediate medical attention to prevent any fatal complications from this
                                condition.
        """
        return top_ps[0], top_labels[0],  results_description




def print_predictions(probs, flowers):
    for idx, preds in enumerate(zip(probs, flowers)):
        print(f"Rank: {idx+1}")
        print(f"Flower: {preds[0]}, Likelihood(0 - Not likely, 1 - Likely): {preds[1]}")

