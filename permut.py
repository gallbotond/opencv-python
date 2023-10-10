import cv2
import numpy as np

# Kép beolvasása
image = cv2.imread('./img/eper.jpg')

# Színcsatornák permutálása
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# Permutációk elkészítése
permutations = [
    cv2.merge([blue_channel, green_channel, red_channel]),  # eredeti
    cv2.merge([blue_channel, red_channel, green_channel]),
    cv2.merge([green_channel, blue_channel, red_channel]),
    cv2.merge([green_channel, red_channel, blue_channel]),
    cv2.merge([red_channel, blue_channel, green_channel]),
    cv2.merge([red_channel, green_channel, blue_channel])
]

# Eredmények megjelenítése
for i, permuted_image in enumerate(permutations):
    window_name = f'Permutált {i+1}'
    cv2.imshow(window_name, permuted_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
