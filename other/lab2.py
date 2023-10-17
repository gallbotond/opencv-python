import cv2
import numpy as np

# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Piros csatorna nullázása
red_channeln = image.copy()
red_channeln[:, :, 0] = 0  # Piros csatorna nullázása

# Zöld csatorna nullázása
green_channeln = image.copy()
green_channeln[:, :, 1] = 0  # Zöld csatorna nullázása

# Kék csatorna nullázása
blue_channeln = image.copy()
blue_channeln[:, :, 2] = 0  # Kék csatorna nullázása

# Eredmények megjelenítése (opcionális)
# cv2.imshow('red null', red_channeln)
# cv2.imshow('green null', green_channeln)
# cv2.imshow('blue null', blue_channeln)
# cv2.waitKey(0)

# Piros és zöld csatornák nullázása
red_green_channel = image.copy()
red_green_channel[:, :, 0] = 0  # Piros csatorna nullázása
red_green_channel[:, :, 1] = 0  # Zöld csatorna nullázása

# Zöld és kék csatornák nullázása
green_blue_channel = image.copy()
green_blue_channel[:, :, 1] = 0  # Zöld csatorna nullázása
green_blue_channel[:, :, 2] = 0  # Kék csatorna nullázása

# Kék és piros csatornák nullázása
blue_red_channel = image.copy()
blue_red_channel[:, :, 0] = 0  # Piros csatorna nullázása
blue_red_channel[:, :, 2] = 0  # Kék csatorna nullázása

# Eredmények megjelenítése (opcionális)
# cv2.imshow('red and green null', red_green_channel)
# cv2.imshow('green and blue null', green_blue_channel)
# cv2.imshow('blue and red null', blue_red_channel)
# cv2.waitKey(0)

# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Színcsatornák permutálása
red_channelp = image[:, :, 0]  # Piros csatorna
green_channelp = image[:, :, 1]  # Zöld csatorna
blue_channelp = image[:, :, 2]  # Kék csatorna

# Színcsatornák permutálása (vörös -> kék, zöld -> vörös, kék -> zöld)
permuted_image = cv2.merge([blue_channelp, red_channelp, green_channelp])

# Eredmények megjelenítése
# cv2.imshow('Eredeti', image)
# cv2.imshow('permut', permuted_image)
# cv2.waitKey(0)


# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Színcsatornák permutálása (vörös negálása)
negated_red_channel = 255 - image[:, :, 0]

# Színcsatornák permutálása (zöld negálása)
negated_green_channel = 255 - image[:, :, 1]

# Színcsatornák permutálása (kék negálása)
negated_blue_channel = 255 - image[:, :, 2]

# Új képek létrehozása a neg színcsatornákkal
negated_red_image = cv2.merge([negated_red_channel, image[:, :, 1], image[:, :, 2]])
negated_green_image = cv2.merge([image[:, :, 0], negated_green_channel, image[:, :, 2]])
negated_blue_image = cv2.merge([image[:, :, 0], image[:, :, 1], negated_blue_channel])

# Eredmények megjelenítése
# cv2.imshow('neg red', negated_red_image)
# cv2.imshow('neg green', negated_green_image)
# cv2.imshow('neg blue', negated_blue_image)
# cv2.waitKey(0)

neg = cv2.merge([  negated_red_channel, negated_green_channel, negated_blue_channel])
# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Átalakítás YCrCb térbe
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Színcsatornák szétválasztása
y, cr, cb = cv2.split(yuv_image)

# Y komponens negálása
negated_y = 255 - y

# Új kép létrehozása a negált Y komponenssel
result_image = cv2.merge([negated_y, cr, cb])

# Visszaalakítás BGR térbe
result_image = cv2.cvtColor(result_image, cv2.COLOR_YCrCb2BGR)

# Eredmény megjelenítése
# cv2.imshow('Eredeti', image)
# cv2.imshow('Y komponens negáltja', result_image)
# cv2.waitKey(0)

# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Átalakítás YCrCb térbe
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Színcsatornák szétválasztása
y, cr, cb = cv2.split(yuv_image)

# Y komponens negálása
negated_y = 255 - y

# Új kép létrehozása a negált Y komponenssel
result_image = cv2.merge([negated_y, cr, cb])

# Visszaalakítás BGR térbe
result_image = cv2.cvtColor(result_image, cv2.COLOR_YCrCb2BGR)

# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Színcsatornák permutálása
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# Permutációk elkészítése
p1 = cv2.merge([blue_channel, green_channel, red_channel])
p2 = cv2.merge([blue_channel, red_channel, green_channel])
p3 = cv2.merge([green_channel, blue_channel, red_channel])
p4 = cv2.merge([green_channel, red_channel, blue_channel])
p5 = cv2.merge([red_channel, blue_channel, green_channel])
p6 = cv2.merge([red_channel, green_channel, blue_channel])



# Kép méretének lekérdezése
height, width, _ = image.shape

# Nagy kép létrehozása
imBig = np.zeros((height * 3, width * 6, 3), dtype=np.uint8)
images = [
    image, 
    red_channeln, 
    green_channeln, 
    blue_channeln,
    red_green_channel, 
    green_blue_channel, 
    blue_red_channel, 
    p1, p2, p3, p4, p5, p6, 
    negated_red_image, 
    negated_green_image, 
    negated_blue_image,
    neg, 
    result_image]

index = 0
for i in range(3):
    for j in range(6):
        im = images[index]
        if len(im.shape) == 2:  # Egy csatornás képek esetén
            imBig[i*height:(i+1)*height, j*width:(j+1)*width, 0] = im
            imBig[i*height:(i+1)*height, j*width:(j+1)*width, 1] = im
            imBig[i*height:(i+1)*height, j*width:(j+1)*width, 2] = im
        else:
            imBig[i*height:(i+1)*height, j*width:(j+1)*width] = im
        index = (index + 1) % len(images)

# Eredmény megjelenítése
cv2.imshow('Ablak', imBig)
cv2.waitKey(0)
cv2.destroyAllWindows()