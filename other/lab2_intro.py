import cv2
import numpy as np

im = cv2.imread('./img/eper.jpg')

# Kép szétválasztása színcsatornákra
b, g, r = cv2.split(im)

# Összeállítás színcsatornákból egy színes képet
result = cv2.merge([b, g, r])

# Új kép létrehozása
imBig = np.zeros((im.shape[0] * 3, im.shape[1] * 6, im.shape[2]), dtype=np.uint8)
z = np.zeros((im.shape[0], im.shape[1]), dtype=np.uint8)

# Színes háttér
imBig[:, :] = (128, 128, 255)

# Eredmények megjelenítése (opcionális)
cv2.imshow('Eredeti', im)
cv2.imshow('R', r)
cv2.imshow('G', g)
cv2.imshow('B', b)
cv2.imshow('Összeállított', result)
cv2.imshow('imBig', imBig)
cv2.waitKey(0)
cv2.destroyAllWindows()
