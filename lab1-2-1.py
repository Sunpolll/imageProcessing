import cv2
import matplotlib.pyplot as plt

# Read the image using OpenCV
image = cv2.imread(".images/peesaderd.jpg")

fig, axs = plt.subplots(4, 4, figsize=(6, 3))

axs[0,0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
axs[0,0].set_title("RGB",fontsize=8)
axs[0,0].axis("off")

axs[0,1].imshow(image[:,:,0], cmap = 'gray')
axs[0,1].set_title("R",fontsize=8)
axs[0,1].axis("off")

axs[0,2].imshow(image[:,:,1], cmap = 'gray')
axs[0,2].set_title("G",fontsize=8)
axs[0,2].axis("off")

axs[0,3].imshow(image[:,:,2], cmap = 'gray')
axs[0,3].set_title("B",fontsize=8)
axs[0,3].axis("off")

image_HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

axs[1,0].imshow(image_HSV)
axs[1,0].set_title("HSV",fontsize=8)
axs[1,0].axis("off")

axs[1,1].imshow(image_HSV[:,:,0], cmap = 'gray')
axs[1,1].set_title("H",fontsize=8)
axs[1,1].axis("off")

axs[1,2].imshow(image_HSV[:,:,1], cmap = 'gray')
axs[1,2].set_title("S",fontsize=8)
axs[1,2].axis("off")

axs[1,3].imshow(image_HSV[:,:,2], cmap = 'gray')
axs[1,3].set_title("V",fontsize=8)
axs[1,3].axis("off")

image_HLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)

axs[2,0].imshow(image_HLS)
axs[2,0].set_title("HLS",fontsize=8)
axs[2,0].axis("off")

axs[2,1].imshow(image_HLS[:,:,0], cmap = 'gray')
axs[2,1].set_title("H",fontsize=8)
axs[2,1].axis("off")

axs[2,2].imshow(image_HLS[:,:,1], cmap = 'gray')
axs[2,2].set_title("L",fontsize=8)
axs[2,2].axis("off")

axs[2,3].imshow(image_HLS[:,:,2], cmap = 'gray')
axs[2,3].set_title("S",fontsize=8)
axs[2,3].axis("off")

image_YCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)

axs[3,0].imshow(image_YCrCb)
axs[3,0].set_title("YCrCb",fontsize=8)
axs[3,0].axis("off")

axs[3,1].imshow(image_YCrCb[:,:,0], cmap = 'gray')
axs[3,1].set_title("Y",fontsize=8)
axs[3,1].axis("off")

axs[3,2].imshow(image_YCrCb[:,:,1], cmap = 'gray')
axs[3,2].set_title("Cr",fontsize=8)
axs[3,2].axis("off")

axs[3,3].imshow(image_YCrCb[:,:,2], cmap = 'gray')
axs[3,3].set_title("Cb",fontsize=8)
axs[3,3].axis("off")
plt.show()
            