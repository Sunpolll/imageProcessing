import cv2
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread(".images/peesaderd.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width = 1024, 768
mask = np.zeros((height, width,3), dtype=np.uint8)

top_left = (200, 150)
bottom_right = (500, 500)

mask[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0], :] = [255, 255, 255]
fig, axs = plt.subplots(1, 3, figsize=(6, 3))

axs[0].imshow(image)
axs[0].set_title("original",fontsize=8)
axs[0].axis("off")

axs[1].imshow(mask)
axs[1].set_title("Image Mask",fontsize=8)
axs[1].axis("off")

result = cv2.bitwise_and(image, mask)
axs[2].imshow(result)
axs[2].set_title("Bitwise_AND() result",fontsize=8)
axs[2].axis("off")

plt.show()