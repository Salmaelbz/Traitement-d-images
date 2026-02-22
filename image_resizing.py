import cv2
import numpy as np

# Loading the original grayscale image
img_original = cv2.imread('peppers-512.png', cv2.IMREAD_GRAYSCALE)

# Checking the image if it has been loaded correctly
if img_original is None:
    print("Erreur : Image non trouvée.")
    exit()

# Creating a new empty image of size 64x64
img_redimensionnee = np.zeros((64, 64), dtype=img_original.dtype)

# Filling the new image with one pixel out of 4 of the original image
for i in range(0, img_redimensionnee.shape[0]):
    for j in range(0, img_redimensionnee.shape[1]):
        img_redimensionnee[i, j] = img_original[i * 4, j * 4]

# Saving the resized image
cv2.imwrite('pepper_resized.png', img_redimensionnee)

# Display images
cv2.imshow('Image Originale', img_original)
cv2.imshow('Image Redimensionnee', img_redimensionnee)
cv2.waitKey(0)
cv2.destroyAllWindows()
