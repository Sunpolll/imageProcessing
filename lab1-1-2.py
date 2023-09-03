import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

# Read the image using OpenCV
image = cv2.imread(".images/peesaderd.jpg")

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
Xr = image[:,:,0]
Y_transpose = np.transpose(image)
Y_moveaxis = np.moveaxis(image,2,0)
Y_reshape = np.reshape(image,(3, image.shape[0], image.shape[1]))

fig, axs = plt.subplots(2, 4, figsize=(3, 3))
plt.subplots_adjust(hspace=0.5)

# show Original image shape and red plane
axs[0,0].text(0.5, 0.5, f"Original\n{image.shape}\n|\n|\n|\nv", fontsize=12, ha='center', va='center')
axs[0,0].axis("off")

axs[1,0].imshow(Xr, cmap = 'gray')
axs[1,0].set_title("Original_Xr",fontsize=8)
axs[1,0].axis("off")

# show Y_transpose shape and red plane
axs[0,1].text(0.5, 0.5, f"Y_transpose\n{Y_transpose.shape}\n|\n|\n|\nv", fontsize=12, ha='center', va='center')
axs[0,1].axis("off")

axs[1,1].imshow(Y_transpose[0,:,:], cmap = 'gray')
axs[1,1].set_title("Y_transpose (Red)",fontsize=8)
axs[1,1].axis("off")

# show Y_moveaxis shape and red plane
axs[0,2].text(0.5, 0.5, f"Y_moveaxis\n{Y_moveaxis.shape}\n|\n|\n|\nv", fontsize=12, ha='center', va='center')
axs[0,2].axis("off")

axs[1,2].imshow(Y_moveaxis[0,:,:], cmap = 'gray')
axs[1,2].set_title("Y_moveaxis (Red)",fontsize=8)
axs[1,2].axis("off")

# show Y_reshape shape and red plane
axs[0,3].text(0.5, 0.5, f"Y_reshape\n{Y_reshape.shape}\n|\n|\n|\nv", fontsize=12, ha='center', va='center')
axs[0,3].axis("off")

axs[1,3].imshow(Y_reshape[0,:,:], cmap = 'gray')
axs[1,3].set_title("Y_reshape (Red)",fontsize=8)
axs[1,3].axis("off")

plt.tight_layout()
plt.show()