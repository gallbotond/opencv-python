import cv2
import numpy as np

# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Képek méreteinek lekérdezése
height, width, _ = image.shape

# Nagy mozaikkép létrehozása
imBig = np.zeros((height * 3, width * 6, 3), dtype=np.uint8)

# 1. Állítsunk elő olyan színes képeket, amelyekben egy-egy színcsatornát konstans nullával helyettesítünk.
red_channel = image.copy()
red_channel[:, :, 0] = 0  # Piros csatorna nullázása

green_channel = image.copy()
green_channel[:, :, 1] = 0  # Zöld csatorna nullázása

blue_channel = image.copy()
blue_channel[:, :, 2] = 0  # Kék csatorna nullázása

# 2. Állítsunk elő olyan színes képeket, amelyekben két-két színcsatornát konstans nullával helyettesítünk.
red_green_channel = image.copy()
red_green_channel[:, :, 0] = 0  # Piros és zöld csatorna nullázása
red_green_channel[:, :, 1] = 0

green_blue_channel = image.copy()
green_blue_channel[:, :, 1] = 0  # Zöld és kék csatorna nullázása
green_blue_channel[:, :, 2] = 0

blue_red_channel = image.copy()
blue_red_channel[:, :, 0] = 0  # Piros és kék csatorna nullázása
blue_red_channel[:, :, 2] = 0

# 3. Permutáljuk meg a színes kép színcsatornáit.
permuted_image = cv2.merge([image[:, :, 2], image[:, :, 0], image[:, :, 1]])

# 4. Állítsunk elő olyan színes képeket, amelyekben az egyik színkomponenst helyettesítjük a saját negatívjával.
negated_red_channel = 255 - image[:, :, 0]
negated_green_channel = 255 - image[:, :, 1]
negated_blue_channel = 255 - image[:, :, 2]

# 5. Állítsunk elő azt a színes képet, amelyikben az Y komponenset helyettesítjük a saját negatívjával.
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(yuv_image)
negated_y = 255 - y
negated_yuv_image = cv2.merge([negated_y, cr, cb])
negated_image = cv2.cvtColor(negated_yuv_image, cv2.COLOR_YCrCb2BGR)

# 6. Tegyük fel az eredeti kép negatívját is a nagy képre.
negative_image = 255 - image

# A képek mozaikképbe való helyezése
images = [image, red_channel, green_channel, blue_channel,
          red_green_channel, green_blue_channel, blue_red_channel,
          permuted_image, negated_red_channel, negated_green_channel, negated_blue_channel,
          negated_image, negative_image]

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
