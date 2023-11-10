import Augmentor
import os
from PIL import Image
import cv2
import numpy as np
import torchvision.transforms as transforms
from torchvision import datasets
from PIL import Image

# 创建ColorJitter变换
color_jitter = transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5)

origin_image_path = '../datasets/JPEGImages/'#原图路径
mask_image_path = '../datasets/SegmentationClassPNG/'#标签路径

origin_images = os.listdir(origin_image_path)
mask_images = os.listdir(mask_image_path)


# 图像转移后的文件夹
image_dir = '../datasets/JPEGImages_2/'
# mask图像复制转移后的的文件夹
mask_dir = '../datasets/SegmentationClassPNG_2/'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)

def aug(Augmentation_2=2140, multiple = 5):
    i = 0
    for origin_image in origin_images:
        original_image = Image.open(origin_image_path + origin_image)
        for mask_image in mask_images:
            if mask_image.split('.')[0] == origin_image.split('.')[0]:
                img_mask = Image.open(mask_image_path + mask_image)
                img_c = img_mask.copy()
        # 生成多张颜色变化的图像并保存
        for j in range(1,multiple+1):
            transformed_image = color_jitter(original_image)
            output_path = os.path.join(image_dir, f"{j+multiple*i+2140}.jpg")
            transformed_image.save(output_path)
            img_c.save(os.path.join(mask_dir, str(j+multiple*i+2140) + '.png'))
        i += 1


