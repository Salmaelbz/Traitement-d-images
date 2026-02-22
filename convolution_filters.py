import cv2
import numpy as np

# Loading the image
img = cv2.imread('peppers-512.png')

# Definition of convolution kernels
kernel_gaussian = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], np.float32) / 16
kernel_box = np.ones((3, 3), np.float32) / 9
kernel_edges = np.array([[1, -3, 1], [-3, 9, -3], [1, -3, 1]])
kernel_sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_custom = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]]) * 3
kernel_laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Applying filters
img_gaussian = cv2.filter2D(img, -1, kernel_gaussian)
img_box = cv2.filter2D(img, -1, kernel_box)
img_edges = cv2.filter2D(img, -1, kernel_edges)
img_sobel_x = cv2.filter2D(img, -1, kernel_sobel_x)
img_custom = cv2.filter2D(img, -1, kernel_custom)
img_laplacian = cv2.filter2D(img, -1, kernel_laplacian)

# Displaying results
cv2.imshow('Gaussian Blur', img_gaussian)
cv2.imshow('Box Blur', img_box)
cv2.imshow('Edge Enhancement', img_edges)
cv2.imshow('Sobel X', img_sobel_x)
cv2.imshow('Custom Filter', img_custom)
cv2.imshow('Laplacian', img_laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()