import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(".images/jarnkai.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split the image into individual color channels
r, g, b = cv2.split(image)

# Apply histogram equalization to each channel
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)
# Merge the equalized channels back together
eq_image = cv2.merge((r_eq, g_eq, b_eq))

fig, axs = plt.subplots(2, 2, figsize=(6, 3))

axs[0,0].imshow(image)
axs[0,0].set_title("Original Color Image",fontsize=8)
axs[0,0].axis("off")

colors = ('r', 'g', 'b')
for i,color in enumerate(colors):   
    hist = cv2.calcHist([image],[i],None,[256],[0,256])
    axs[0,1].plot(hist,color = color)
axs[0,1].set_title("Hist Original Image",fontsize=8)
axs[0,1].axis("on")

axs[1,0].imshow(eq_image)
axs[1,0].set_title("Equalized Image",fontsize=8)
axs[1,0].axis("off")

for i,color in enumerate(colors):   
    eqhist = cv2.calcHist([eq_image],[i],None,[256],[0,256])
    axs[1,1].plot(eqhist,color = color)
axs[1,1].set_title("Hist Equalized Image",fontsize=8)
axs[1,1].axis("on")

plt.show()