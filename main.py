import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
segmentor = SelfiSegmentation()

paths=os.listdir("Resources")
for i in range(len(paths)):
    paths[i]="Resources/"+paths[i]

image_index=0

while True:
    success, img = cap.read()

    bgimg = cv2.imread(paths[image_index])
    bgimg = cv2.resize(bgimg, (640, 480))

    no_bg_img = segmentor.removeBG(img, bgimg,0.8)
    no_bg_img = cv2.flip(no_bg_img, 1)
    no_bg_img = cv2.resize(no_bg_img,(640,480))

    cv2.imshow("video", no_bg_img)

    key=cv2.waitKey(1)
    if key==ord('d'):
        image_index=(image_index+1)%len(paths)
    elif key==ord('a'):
        image_index=(image_index-1)%len(paths)
    elif key == ord('q') or cv2.getWindowProperty('video', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
