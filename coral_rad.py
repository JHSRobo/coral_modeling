import numpy as np
import cv2
window_name = 'image'

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        clicks_x.append(x)
        clicks_y.append(y)

clicks_x = []
clicks_y = []

img = cv2.imread('\\wsl.localhost\Ubuntu-20.04\home\jhsrobo\ROVMIND\ros_workspace\src\img_capture\img\coral\radius\rad.png', cv2.IMREAD_COLOR)
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, draw_circle)


while True:
    cv2.imshow(window_name,img)
    cv2.waitKey(1)
    if(len(clicks_x) and len(clicks_y) == 4):
        reference = ((((abs(clicks_x[0] - clicks_x[1]) ** 2) + (abs(clicks_y[0] - clicks_y[1])) ** 2)) ** 0.5)
        ratio = 40. / reference
        total = ((((abs(clicks_x[2] - clicks_x[3]) ** 2) + (abs(clicks_y[2] - clicks_y[3])) ** 2)) ** 0.5) * ratio
        displayImg = np.zeros((512,1024,3), dtype=np.uint8)
        cv2.putText(displayImg, "{:.2f} cm".format(total), (50,325), cv2.FONT_HERSHEY_SIMPLEX, 5, (50, 255, 50), 3)
        cv2.destroyWindow(window_name)
        break

while True:
    cv2.imshow('displayImage', displayImg)
    if cv2.waitKey(1) == ord('q'):
      cv2.destroyAllWindows()
      break
