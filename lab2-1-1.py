import cv2
import numpy as np

image = cv2.imread(".images/peesaderd.jpg")

file_path = 'lab2-1-1.mp4'
fps = 5
frame_size = (768, 1024)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
writer = cv2.VideoWriter(file_path, fourcc, fps, frame_size)

a = [round(x/5, 2) for x in range(-10, 10)]
b = [x for x in range(200, -1, -10)]

height, width, channels = image.shape

for i in range(len(a)):
    adjusted_image = image.astype(float)
    adjusted_image *= a[i]
    adjusted_image += b[i]
    
    # Manually limit pixel values to [0, 255]
    adjusted_image[adjusted_image < 0] = 0
    adjusted_image[adjusted_image > 255] = 255
    
    adjusted_image = adjusted_image.astype(np.uint8)
    
    writer.write(adjusted_image)

writer.release()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image= cv2.imread("./peesaderd.jpg")

# file_path = 'lab2-1-1.mp4'
# fps = 5
# frame_size = (768, 1024)
# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# writer = cv2.VideoWriter(file_path, fourcc, fps, frame_size)

# a = [round(x/5,2) for x in range(-10,10)]
# b = [x for x in range(200,-1,-10)]

# height, width, channels = image.shape

# for i in range(len(a)):
#     most,least = None,None
#     temp = image.astype(float)
#     for y in range(height):
#         for x in range(width):
#             for c in range(channels):
#                 temp[y, x, c] = a[i] * image[y, x, c] + b[i]
#             l = min(temp[y, x])
#             m = max(temp[y, x])
#             if least is None or l < least: least = l
#             if most is None or m > most: most = m
#     diff = most-least
#     if diff == 0:diff+=1
#     temp = ((temp+least)/(diff)*255).astype(np.uint8)
#     writer.write(temp)

# writer.release()