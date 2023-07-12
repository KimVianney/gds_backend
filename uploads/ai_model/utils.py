from collections import OrderedDict
from os.path import isdir

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, models, transforms


def load_gpu():
    # if not gpu:
    #     return torch.device("cpu")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"DEVICE: {device}")

    if device == "cpu":
        print("WARNING: GPU Not Found! Load CUDA enabled device")
    
    return device


def load_pretrained_model(arch="vgg16"):
    model = models.vgg16(pretrained=True)
    model_name = arch
    
    for param in model.parameters():
        param.requires_grad = False
        
    return model



def classifier(model, output_features):
    # Define new classifier
    classifier = nn.Sequential(OrderedDict([
        ('fc1', nn.Linear(25088, 8192)),
        ('relu', nn.ReLU()),
        ('dropout', nn.Dropout(p=0.5)),
        ('fc3', nn.Linear(8192, output_features)),
        ('output', nn.LogSoftmax(dim=1))]))

    model.classifier = classifier
    return model.classifier            
            
def load_checkpoint(filepath, device):
    # Load saved checkpoints
    checkpoint = torch.load(filepath, map_location=torch.device(device))
    
    # Load pretrained model
    model = models.vgg16(pretrained=True)
    for param in model.parameters():
        param.requires_grad = False
        
    # Initialize model with saved state_dict
    model.classifier = classifier(model, 2)
    model.load_state_dict(checkpoint['state_dict'])
    return model

def imsave(image, filepath, ax=None):
    """Imshow for Tensor."""
    if ax is None:
        fig, ax = plt.subplots()

    # PyTorch tensors assume the color channel is the first dimension
    # but matplotlib assumes is the third dimension
    image = image.numpy().transpose((1, 2, 0))
    
    # Undo preprocessing
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    image = std * image + mean

    # Image needs to be clipped between 0 and 1 or it looks like noise when displayed
    image = np.clip(image, 0, 1)
    plt.imsave(filepath, image)
    