from skimage.io import imread, imsave

def image_read(path, is_gray=False):
    image = imread(path, asgray = is_gray)
    return image

def image_save(image, path):
    imsave(path, image)

    