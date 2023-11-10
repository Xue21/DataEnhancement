import Augmentor
import os
from PIL import Image
import cv2
import numpy as np
import torchvision.transforms as transforms
from torchvision import datasets
from PIL import Image
from MakeDataset.PictureColorEnhancement import aug
from MakeDataset.PictureShapeEnhancement import jpg_png,augment_data,split_image_mask

if __name__ == "__main__":
    img_path = 'datasets/JPEGImages/'
    output_path = '../datasets/JPEGImages_png/'
    jpg_png(img_path=img_path,output_path=output_path)
    # Data augmentation is performed through rotation, flipping, and random cropping.
    #Augmentation_1=2140 is the number of images after data enhancement.
    augment_data(Augmentation_1=2140)
    split_image_mask()
    # augmentation is achieved by altering brightness, contrast, saturation, and hue.
    # Augmentation_2=2140 is the number of the first data enhancements. multiple=5 is the multiple of the second data enhancement.
    aug(Augmentation_2=2140,multiple=5)  # Augmentation_2 is the number