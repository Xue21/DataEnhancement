import Augmentor
import os
from PIL import Image
import cv2
import numpy as np

"""
图像模式转换 Image模块
# img_path_class = '../datasets/SegmentationClassPNG/'
# for im_name in os.listdir(img_path_class):
#     img_mode = Image.open(img_path_class + im_name)
#     print(img_mode.mode)
#     #已经是RGB模式了
#     img = img_mode.convert('RGB')#图像模式转换
#     #print(img.mode)
#     img.save(img_path_class + im_name)
"""

"""
一般mask图像是png格式的，Augmentor需要保证原始图像与mask图像格式一致
将原图像由jpg格式转化成png格式
"""

def jpg_png(img_path,output_path):
    """将jpg格式图像转换成png格式图像"""
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for im_name in os.listdir(img_path):
        # print(img_path + im_name)
        img = cv2.imread(img_path + im_name)
        im_name_new = im_name.split('.')[0] + '.png'
        cv2.imwrite(output_path + im_name_new, img)

def augment_data(Augmentation_1 = 2140):
    """图像增强
    图片名字及后缀与掩码名字及后缀必须相同，否者不能进行数据增强
    """
    p = Augmentor.Pipeline('../datasets/JPEGImages_png')#原图由jpg转换成png后的路径
    p.ground_truth('../datasets/SegmentationClassPNG')#掩膜路径
    p.rotate(probability=1,max_left_rotation=15,max_right_rotation=15)#图像旋转
    p.flip_left_right(probability=0.5)#水平翻转
    p.flip_top_bottom(probability=0.5)#上下翻转
    p.zoom_random(probability=1, percentage_area=0.7)
    """当原图是三通道，标签是单通道时没法进行颜色方面的改变"""
    #p.random_brightness(probability=0.5,min_factor=0.6,max_factor=0.8)
    #p.random_color(probability=0.5,min_factor=0.3,max_factor=0.8)
    p.sample(Augmentation_1)

def split_image_mask():
    """将增强后的图像和掩码分开"""
    # 分开后原始图像的文件夹
    orgin_dir = '../datasets/JPEGImages_1'
    # 分开后mask图像的文件夹
    mask_dir = '../datasets/SegmentationClassPNG_1'
    if not os.path.exists(orgin_dir):
        os.makedirs(orgin_dir)
    if not os.path.exists(mask_dir):
        os.makedirs(mask_dir)

    output_dir = '../datasets/JPEGImages_png/output' # 上面生成的增强图像都在这个目录下
    all_img_list = os.listdir(output_dir)
    count = 1
    for img_name in all_img_list:
        """找到对应的img和mask"""
        if img_name.startswith('_groundtruth_'):
            # 将掩码移到mask_dir文件夹下
            img_path = img_name.split('_', maxsplit=5)[-1]
            os.rename(os.path.join(output_dir, img_name), os.path.join(mask_dir, str(count) + '.png'))
            # 图像移动到orgin_dir下
            os.rename(os.path.join(output_dir, 'JPEGImages_png_original_' + img_path),
                      os.path.join(orgin_dir, str(count) + '.jpg'))
            count += 1

def countColors(img):
    """输出图像所有不同的像素值"""
    m,n = img.shape[:2]
    pxtype = list if img.ndim >2 else int
    colors = []
    for i in range(m):
        for j in range(n):
            px = pxtype(img[i,j])
            if px in colors:
                continue
            else:
                colors.append(px)
    print(colors)

# """opencv无法正确读取用于语义分割的mask图像，因为opencv在读取png格式的
# 图像时，自动将单通道转换成三通道，像素值也发生改变"""
# """在Image中
# shape:HxWxC
# size:WxH"""
# """避坑指南: 使用 Pillow 库读取图像"""
#
# # path = '../images/1.png'
# #
# # """转换的像数值"""
# # img = cv2.imread(path)
# # print(img.shape)#(634, 950, 3)
# # countColors(img)#[[0, 0, 0], [0, 0, 64]]
# #
# # """真实的像素值"""
# # img = np.array(Image.open(path))
# # print(img.shape)#(634, 950)
# # img = cv2.merge([img,img,img])
# # countColors(img)#[[0, 0], [0, 8]]
# #
# # """opencv单通道读取,后面加0,但是即使单通道读取图像像素值也发生改变"""
# # img = cv2.imread(path,0)
# # print(img.shape)#(634, 950)
# # img = cv2.merge([img,img,img])
# # countColors(img)#[[0, 0, 0], [19, 19, 19]]






