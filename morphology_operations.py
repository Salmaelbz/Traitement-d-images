import cv2
import numpy as np

# Loading the image and converting it to a binary imageimg = cv2.imread('peppers-512.png', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Structuring element (e.g. a 3x3 square)
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

def erosion(image, kernel)
    eroded_image = np.zeros_like(image)
    padding = kernel.shape[0]  2
    for i in range(padding, image.shape[0] - padding)
        for j in range(padding, image.shape[1] - padding)
            region = image[i-paddingi+padding+1, j-paddingj+padding+1]
            eroded_image[i, j] = np.min(region) if np.all(region == kernel) else 0
    return eroded_image

def dilation(image, kernel)
    dilated_image = np.zeros_like(image)
    padding = kernel.shape[0]  2
    for i in range(padding, image.shape[0] - padding)
        for j in range(padding, image.shape[1] - padding)
            region = image[i-paddingi+padding+1, j-paddingj+padding+1]
            dilated_image[i, j] = np.max(region) if np.any(region == 255) else 0
    return dilated_image

# Erosion and expansion applicationimg_eroded = erosion(img_bin, kernel)
img_dilated = dilation(img_bin, kernel)

# Opening (erosion followed by expansion)
img_opening = dilation(erosion(img_bin, kernel), kernel)

# Closure (expansion followed by erosion)
img_closing = erosion(dilation(img_bin, kernel), kernel)

# Difference between expansion and erosion
img_difference = cv2.absdiff(img_dilated, img_eroded)

# Displaying results
cv2.imshow('Image Originale Binaire', img_bin)
cv2.imshow('erosion', img_eroded)
cv2.imshow('Dilatation', img_dilated)
cv2.imshow('Ouverture', img_opening)
cv2.imshow('Fermeture', img_closing)
cv2.imshow('Difference', img_difference)
cv2.waitKey(0)
cv2.destroyAllWindows()
