from PIL import Image
import os.path
import glob

def convert_image(file,width=512,height=512):
    """将图像尺寸转换成512X512,并保存在另一个文件夹"""
    img=Image.open(file)
    new_img=resize_image(img,(width,height))
    new_img.save(os.path.join(image_dir,os.path.basename(file)))#os.path.basename(file)返回file最后的文件名

#---------------------------------------------------#
#   对输入图像进行resize
"""在Image中
# shape:HxWxC
# size:WxH"""
#---------------------------------------------------#
def resize_image(image, size):
    """不改变图像形状的尺寸变换"""
    iw, ih= image.size
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)
    image_1 = image.resize((nw,nh))
    new_image = Image.new('RGB', size, (128,128,128))
    new_image.paste(image_1, ((w-nw)//2, (h-nh)//2))
    return new_image
    #new_image.save('./resize.png')

if __name__ == "__main__":
    # 图像尺寸裁剪后的文件夹
    image_dir = '../datasets/image_size512/'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    for file in glob.glob('../datasets/JPEGImages/*.jpg'):  # 来源文件夹
        # print(file)#file代表文件路径
        convert_image(file)  # 目标文件夹
