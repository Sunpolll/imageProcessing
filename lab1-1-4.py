import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the image using OpenCV
image = cv2.imread(".images/peesaderd.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
g_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
g_image = cv2.resize(g_image,(200,200))
# Create a meshgrid of x and y coordinates
x, y = np.mgrid[0:g_image.shape[0], 0:g_image.shape[1]]

# Flatten the grayscale image and z-coordinate for plot_surface()
z = g_image.flatten()

# Create a 3D figure and add a 3D axis

fig = plt.figure(figsize=(12, 5))

# Plot the original color image in the first subplot
ax1 = fig.add_subplot(131)
ax1.imshow(image)
ax1.set_title("Original", fontsize=12)
ax1.axis("off")

# Plot the grayscale image in the second subplot
ax2 = fig.add_subplot(132)
ax2.imshow(g_image, cmap='gray')
ax2.set_title("Gray 200x200", fontsize=12)
ax2.axis("off")

# Create a new 3D axis for the surface plot
ax3 = fig.add_subplot(133, projection='3d')

# Plot the surface using plot_surface()
ax3.plot_surface(x, y, z.reshape(g_image.shape), cmap='gray')
ax3.set_title("3D", fontsize=12)
ax3.view_init(elev=70, azim=-20)

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.3)
plt.show()