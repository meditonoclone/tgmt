import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def loadImg(path):
    try:
        img = Image.open(path)
        return img
    except Exception as e:
        print('Lỗi khi đọc ảnh từ: ', path, ' ', e )

def isImgFile(path):
    extensions =(".jpg", ".jpeg", ".png", ".gif", ".bmp")
    return path.lower().endswith(extensions)

def getImgs(path):
    imgs = []
    if os.path.exists(path) and os.path.isdir(path):
        filenames = os.listdir(path)
        for filename in filenames:
            file_path=os.path.join(path, filename)
            if  os.path.isfile(file_path) and isImgFile(file_path):
                img = loadImg(file_path)
                imgs.append(img)
    return imgs

def histogram_equalization(image, nbr_bins=256):
    if image.mode != 'L':
        image = image.convert('L')
    image_array = np.array(image)
    histogram, bins = np.histogram(image_array, bins=nbr_bins, range=(0, 256), density=True)
    cdf = histogram.cumsum()
    cdf = 255 * cdf / cdf[-1]
    image_equalized = np.interp(image_array, bins[:-1], cdf)
    equalized_image = Image.fromarray(image_equalized.astype('uint8'))

    return equalized_image
        