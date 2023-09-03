import cv2
import matplotlib.pyplot as plt

# Read the image using OpenCV
image = cv2.imread(".images/peesaderd.jpg")

# Extracting individual color channels
Xb = image[:, :, 0]  # Blue channel
Xg = image[:, :, 1]  # Green channel
Xr = image[:, :, 2]  # Red channel

W = image.copy()
W[:, :, 0] = Xr  # Set Blue channel to Red channel (Xr)
W[:, :, 1] = Xg  # Set Green channel to Green channel (Xg)
W[:, :, 2] = Xb  # Set Red channel to Blue channel (Xb)

# Create subplots to compare images
fig, axs = plt.subplots(2, 4, figsize=(6, 3))

axs[0,0].imshow(image)
axs[0,0].set_title("BGR",fontsize=8)
axs[0,0].axis("off")

axs[0,1].imshow(Xb,cmap='gray')
axs[0,1].set_title("B",fontsize=8)
axs[0,1].axis("off")

axs[0,2].imshow(Xg,cmap='gray')
axs[0,2].set_title("G",fontsize=8)
axs[0,2].axis("off")

axs[0,3].imshow(Xr,cmap='gray')
axs[0,3].set_title("R",fontsize=8)
axs[0,3].axis("off")

axs[1,0].imshow(W)
axs[1,0].set_title("RGB",fontsize=8)
axs[1,0].axis("off")

axs[1,1].imshow(W[:, :, 0],cmap='gray')
axs[1,1].set_title("R",fontsize=8)
axs[1,1].axis("off")

axs[1,2].imshow(W[:, :, 1],cmap='gray')
axs[1,2].set_title("G",fontsize=8)
axs[1,2].axis("off")

axs[1,3].imshow(W[:, :, 2],cmap='gray')
axs[1,3].set_title("B",fontsize=8)
axs[1,3].axis("off")

plt.show()
