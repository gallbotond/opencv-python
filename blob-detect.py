import cv2
import numpy as np

color_img = cv2.imread('./img/jpeg/im1.jpeg')

# print the size of the image
print(color_img.shape)

# rescale the image
rescale = 8
color_img = cv2.resize(color_img, (color_img.shape[1]//rescale, color_img.shape[0]//rescale))

# print the size of the image
print(color_img.shape)
cv2.waitKey(0)

# split the image into 3 channels
b, g, r = cv2.split(color_img)
cv2.imshow('g', g)
cv2.imshow('r', r)

result3 = np.zeros((g.shape[0], g.shape[1]), dtype='uint8')

def custom_div(im1, im2):
    result = np.zeros((im1.shape[0], im1.shape[1]), dtype='uint8')
    # iterate over the whole image and subtract im2 from im1
    for i in range(im1.shape[0]):
        for j in range(im1.shape[1]):
            val1 = im1[i][j].astype('int8')
            val2 = im2[i][j].astype('int8')
            res = val1 - val2
            # make sure the value is not negative
            if res < 0:
                result[i][j] = 0
            else:
                result[i][j] = res

    return result

g_minus_r = custom_div(g, r)
cv2.imshow('g_minus_r', g_minus_r)

r_minus_g = custom_div(r, g)
cv2.imshow('r_minus_g', r_minus_g)


def threshold_slider(im, name):
    def threshold_image(im, threshold):
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        return thresholded

    def on_threshold_change(value):
        threshold = value
        thresholded_image = threshold_image(im, threshold)
        cv2.imshow(name, thresholded_image)

    initial_threshold = 128
    cv2.namedWindow(name)
    cv2.createTrackbar(name, name, initial_threshold, 255, on_threshold_change)
    thresholded_image = threshold_image(im, initial_threshold)
    cv2.imshow(name, thresholded_image)
    cv2.waitKey(0)
    final = cv2.getTrackbarPos(name, name)
    return final

im = cv2.cvtColor(g_minus_r, cv2.COLOR_GRAY2BGR)

final = threshold_slider(im, 'Thresholded Image')
# thresholded_image = threshold_image(image, final)
_, thresholded_image = cv2.threshold(im, final, 255, cv2.THRESH_BINARY)

# erode the thresholded image
eroded_image = cv2.erode(thresholded_image, None, iterations=10)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)

bv = 25
# apply blur to the thresholded image
blurred_image = cv2.GaussianBlur(eroded_image, (bv, bv), 0)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)

# final = threshold_slider(blurred_image, 'Thresholded Image after blur')
_, thresholded_image_after = cv2.threshold(blurred_image, final, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded Image after blur', thresholded_image_after)
cv2.waitKey(0)


gray_image = cv2.cvtColor(thresholded_image_after, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_with_contours = cv2.drawContours(color_img, contours, -1, (0, 255, 0), 3)

cv2.imshow('img_with_contours', img_with_contours)
cv2.waitKey(0)

cv2.destroyAllWindows()
