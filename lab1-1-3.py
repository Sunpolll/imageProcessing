import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image using OpenCV
image = cv2.imread(".images/peesaderd.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
max_value = 2**4 - 1
# Normalize the image intensity to the range [0, 1]
normalized_image = image / 255.0

# Quantize the image by scaling and rounding
q_image = (normalized_image * max_value).round()

# Rescale the image back to the range [0, 255]
q_image = (q_image * (255 / max_value)).astype(np.uint8)

fig, axs = plt.subplots(1, 2, figsize=(6, 3))

axs[0].imshow(image, cmap = 'gray')
axs[0].set_title("original",fontsize=8)
axs[0].axis("off")

axs[1].imshow(q_image, cmap = 'gray')
axs[1].set_title("Quantization",fontsize=8)
axs[1].axis("off")

plt.show()
            
    
