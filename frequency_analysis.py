import cv2
import numpy as np
import sys
def dft_and_shift(image_path):
   # Grayscale image loading
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Application of the Discrete Fourier Transform (DFT)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    
    # Offset of the result to place the frequency zero in the center
    dft_shift = np.fft.fftshift(dft)
    
   # Amplitude spectrum calculation and normalization
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    
    # Flip the amplitude spectrum
    return magnitude_spectrum

# Paths to images
images = ['D1r.pgm', 'D11r.pgm', 'D46r.pgm', 'peppers-512.png']

# Performing the DFT for each image and displaying the amplitude spectra
for image_path in images:
    magnitude_spectrum = dft_and_shift(image_path)
    cv2.imshow(f'Spectre de {image_path}', magnitude_spectrum)

# Rotate the image peppers-512.png
img_peppers = cv2.imread('peppers-512.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img_peppers.shape
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1) # Rotation de 90 degrés
img_rotated = cv2.warpAffine(img_peppers, M, (cols, rows))

# Perform the DFT of the shot image
magnitude_spectrum_rotated = dft_and_shift(img_rotated)
cv2.imshow('Spectre de peppers-512.png tournée', magnitude_spectrum_rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
