import cv2
import numpy as np
from util import display_threshold_window, custom_div

img = cv2.imread('./img/jpeg/im1.jpeg')

r = custom_div(img[:, :, 2], img[:, :, 1])

cv2.imshow('r', r)