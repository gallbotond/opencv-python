import cv2
import numpy as np

img = cv2.imread('./img/100px.png')
red = cv2.imread('./img/red.png')
green = cv2.imread('./img/green.png')

# using convolution go through the image and find the red and green pixels
