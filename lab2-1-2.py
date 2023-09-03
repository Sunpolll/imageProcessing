import cv2
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread(".images/peesaderd.jpg")

file_path = 'lab2-1-2.mp4'
fps = 5
frame_size = (768, 1024)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
writer = cv2.VideoWriter(file_path, fourcc, fps, frame_size)

y = [round(x/11,2) if x < 11 else x/10 for x in range(1,21)]
height, width, channels = image.shape

for i in y:
    adjusted_image = image.astype(float)
    adjusted_image **= i
    
    # Manually limit pixel values to [0, 255]
    adjusted_image[adjusted_image < 0] = 0
    adjusted_image[adjusted_image > 255] = 255
    
    adjusted_image = adjusted_image.astype(np.uint8)
    
    writer.write(adjusted_image)

writer.release()