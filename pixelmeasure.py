import numpy as np
import cv2

print("Running fish")
window_name = 'image'
def add_clicks(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
	    clicks.append((x, y))

clicks = []
vid_capture = cv2.VideoCapture("http://192.168.1.99:5000")

while vid_capture.isOpened():
  ret, frame = vid_capture.read()
  cv2.imshow('video', frame)
  if cv2.waitKey(1) == ord('p'):
    cv2.imwrite('pix.png', frame)
    cv2.destroyAllWindows()
    vid_capture.release()
    break

img = cv2.imread('pix.png', cv2.IMREAD_COLOR)
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, add_clicks)

while True:
    cv2.imshow(window_name, img)
    cv2.waitKey(1)
    for click in clicks:
       img = cv2.circle(img,(click[0],click[1]),10,(255,0,0),-1)

    if len(clicks) == 2:
        total = (abs(clicks[0][0] - clicks[1][0]) ** 2) + (abs(clicks[0][1] - clicks[1][1]) ** 2) ** 0.5
        displayImg = np.zeros((512,1024,3), dtype=np.uint8)
        cv2.putText(displayImg, "{:.2f} px".format(total), (50,325), cv2.FONT_HERSHEY_SIMPLEX, 5, (50, 255, 50), 3)
        cv2.destroyWindow(window_name)
        break
        
while True:
    cv2.imshow('displayImage', displayImg)
    if cv2.waitKey(1) == ord('q'):
      cv2.destroyAllWindows()
      break