import cv2

image2 = cv2.imread(".images/maithai.jpg")
image1 = cv2.imread(".images/peesaderd.jpg")

w1 = [round(x/19,2) for x in range(20)]
w2 = w1[::-1]
file_path = 'output_video.mp4'
fps = 5
frame_size = (768, 1024)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
writer = cv2.VideoWriter(file_path, fourcc, fps, frame_size)

for i in range(20):
    blended_frame = cv2.addWeighted(image1, w2[i], image2, w1[i], 0)
    writer.write(blended_frame)
for i in range(20):
    blended_frame = cv2.addWeighted(image1, w1[i], image2, w2[i], 0)
    writer.write(blended_frame)
writer.release()
