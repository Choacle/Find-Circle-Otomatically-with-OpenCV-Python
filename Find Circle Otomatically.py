import imutils
import cv2
import pyautogui

img = "draw.jpeg"

pic = cv2.imread(img)
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

x = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
x = imutils.grab_contours(x)

autoguilist = []
for c in x:
    M = cv2.moments(c)
    if (M["m00"] == 0):
        M["m00"]=1

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    autoguilist.append((cX,cY))
    cv2.putText(pic, "center", (cX - 20, cY - 20),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    cv2.drawContours(pic, [c], -1, (0, 255, 255), 2)
    cv2.circle(pic, (cX, cY), 7, (255, 255, 0), -1)
 
cv2.imshow("Image", pic)
cv2.imwrite("draw2.jpeg",pic)
for i in autoguilist:
    if i[0] <= 0:
        break
    cX = i[0]
    cY = i[1]
    
    #FINAL
    pyautogui.moveTo(cX, cY)
cv2.waitKey(0)