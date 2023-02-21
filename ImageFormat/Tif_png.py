# 以tiff转jpg为例，其他格式同理，
# 代码中路径更改为自己图像存放路径即可

import os
import cv2 as cv2
import numpy as np
import tifffile
# from libtiff import TIFF
imagesDirectory = r"D:\Data\backups\test_npz"  # tiff图片所在文件夹路径
distDirectory = os.path.dirname(imagesDirectory)  #

distDirectory = os.path.join(distDirectory, "PngImages")  # 要存放bmp格式的文件夹路径
os.makedirs(distDirectory,exist_ok=True)
print(distDirectory)

for imageName in os.listdir(imagesDirectory):
    print("imageName", imageName)
    imagePath = os.path.join(imagesDirectory, imageName)
    print("imagePath", imagePath)
    image_16bit = cv2.imread(imagePath,-1)
    # img2 = TIFF.open(imagePath, mode='r').read_image()
    img2 = tifffile.imread(imagePath)
    try:
        image_16bit.shape
        min_16bit = np.min(image_16bit)
        max_16bit = np.max(image_16bit)
        image_8bit = np.array(np.rint(255 * ((image_16bit - min_16bit) / (max_16bit - min_16bit))), dtype=np.uint8)
        print("cv2  img shape:",image_16bit.shape)
        print("tif  img shape:", img2.shape)
    except:
        print('读取图片失败')
        break

    print("imageName.split('.')[0]", imageName.split('.')[0])
    distImagePath = os.path.join(distDirectory, imageName.split('.')[0] + '.png')  # 更改图像后缀为.jpg，并保证与原图像同名
    print("distImagePath", distImagePath)
    cv2.imwrite(distImagePath, image_8bit)

