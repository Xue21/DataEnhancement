1.先运行  批量处理图片大小.py   将datasets/JPEGImages文件里面图像尺寸修改为512x512，文件夹的名称根据自己的名称更改
2.利用Labelme标注修改完尺寸后的图像，并将josn格式标注转变成png格式。
将原图以及标注的josn一起放在data_annotated文件夹里面（将data_annotated和data_dataset_voc原有的内容删掉），labels.txt里面只保留__ignore__、_background_、line
在anaconda命令行里在labelme下载源码路径运行指令""" python labelme2voc.py data_annotated data_dataset_voc --labels labels.txt"""
====》最终得到两个文件夹：JPEGImages，SegmentationClassPNG，将这两个文件放在datasets里面
3.运行    图像增广.py         通过旋转、翻转、裁剪增强图像
4.运行    图像增广_颜色亮度.py  通过颜色进行数据增强
====》最终得到四个文件夹 JPEGImages_1,JPEGImages_2(jpg图像增强后的)
SegmentationClassPNG_1,SegmentationClassPNG_2(png标注图图像增强后的)
将JPEGImages_1,JPEGImages_2合在一个文件夹JPEGImages
将SegmentationClassPNG_1,SegmentationClassPNG_2合在一个文件夹SegmentationClass
