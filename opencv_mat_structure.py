import cv2 as cv
import numpy as np
import sys

# Keycode definitions
ESC_KEY = 27
Q_KEY = 113

def main():
    # Data structure to store the image
    im = None
    # Default name of the image file
    imName = 'peppers-512.png'
    
    # If we give an argument then open it instead of the default image
    if len(sys.argv) == 2:
        imName = sys.argv[1]
    
    # Reading the image (and forcing it to grayscale)
    print("Reading image")
    im = cv.imread(imName, cv.IMREAD_GRAYSCALE)
    
    if im is None or im.size == 0:
        print("Could not load image!")
        print("Exiting now...")
        sys.exit(1)

    # Creating a window to display the original image
    cv.namedWindow("Original image")
    # Displaying the loaded image in the named window
    cv.imshow("Original image", im)
    
    # Manual resizing of the image
    # Get the dimensions of the image
    height, width = im.shape[:2]
    # Define the new dimensions
    new_width = 64
    new_height = 64
    # Create an empty image with the new dimensions
    resized_im = np.zeros((new_height, new_width), dtype=im.dtype)
    
    # Manual resizing - selecting one pixel out of every 4
    for i in range(new_height):
        for j in range(new_width):
            resized_im[i, j] = im[i * (height // new_height), j * (width // new_width)]
    
    # Creating a window to display the resized image
    cv.namedWindow("Resized image")
    # Displaying the resized image in the named window
    cv.imshow("Resized image", resized_im)

    # Waiting for the user to press ESCAPE or Q before exiting the application
    key = cv.waitKey(0)
    while key not in [ESC_KEY, Q_KEY]:
        key = cv.waitKey(1)

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
