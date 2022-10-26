import cv2
vidcap = cv2.VideoCapture(r'E:\비타소프트\파트라슈 촬영\VideoToImage\수정파일\original.avi')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("original/%06d.png" % count, image)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print("finish! convert video to frame")