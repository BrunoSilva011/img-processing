import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_diference_pair(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with the same shape"
    image1_gray = rgb2gray(image1)
    image2_gray = rgb2gray(image2)
    (score, image_diferent) = structural_similarity(image1_gray, image2_gray, full=True)
    print("Similarity of the image: ", score)
    image_diference_normalized = (image_diferent-np.min(image_diferent))/(np.max(image_diferent))-(np.min(image_diferent))
    return image_diference_normalized

def find_diference_triple(image1, image2, image3):
    assert image1.shape == image2.shape and image3.shape
    image1_gray = rgb2gray(image1)
    image2_gray = rgb2gray(image2)
    image3_gray = rgb2gray(image3)
    (score, image_diferent) = structural_similarity(image1_gray, image2_gray, image3_gray, full=True)
    image_diference_normalized = (image_diferent-np.min(image_diferent))/(np.max(image_diferent))-(np.min(image_diferent))
    return image_diference_normalized

def histogram_transfer_pair(image1, image2):
    corresponding_image = match_histograms(image1, image2, multichannel= True)
    return corresponding_image

def histogram_transfer_triple(image1,image2,image3):
    corresponding_image = match_histograms(image1,image2,image3, multichannel=True)
    return corresponding_image
