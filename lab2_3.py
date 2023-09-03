import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('.images/rock.jpeg')
template = cv2.imread('.images/sun.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

target_height, target_width = image.shape[:2]
template = cv2.resize(template, (target_width, target_height))

# Split the images into RGB channels
source_channels = cv2.split(image)
template_channels = cv2.split(template)
fig, axs = plt.subplots(3, 3, figsize=(6, 3))

colors = ('b', 'g', 'r')
matched_channels = []
for i,color in enumerate(colors):
    src_channel = source_channels[i]
    temp_channel = template_channels[i]
    # Calculate histograms
    source_hist = cv2.calcHist([src_channel], [0], None, [256], [0, 256])
    template_hist = cv2.calcHist([temp_channel], [0], None, [256], [0, 256])
    axs[0,1].plot(source_hist,color = color)
    axs[1,1].plot(template_hist,color = color)
    # Calculate cumulative distribution functions (CDFs)
    source_cdf = source_hist.cumsum() / source_hist.sum()
    template_cdf = template_hist.cumsum() / template_hist.sum()
    axs[0,2].plot(source_cdf,color = color)
    axs[1,2].plot(template_cdf,color = color)
    # Create mapping function
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        diff = np.abs(source_cdf[i] - template_cdf)
        mapping[i] = np.argmin(diff)
    
    # Apply mapping to the channel
    matched_channel = mapping[src_channel]
    matched_hist = cv2.calcHist([matched_channel], [0], None, [256], [0, 256])
    matched_cdf = matched_hist.cumsum() / matched_hist.sum()
    axs[2,1].plot(matched_hist,color = color)
    axs[2,2].plot(matched_cdf,color = color)
    matched_channels.append(matched_channel)

# Combine the matched channels to create the matched image
matched_image = cv2.merge(matched_channels)

axs[0,0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[1,0].imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
axs[2,0].imshow(cv2.cvtColor(matched_image, cv2.COLOR_BGR2RGB))

output_filename = 'lab2-3.jpg'
cv2.imwrite(output_filename, matched_image)

plt.show()
