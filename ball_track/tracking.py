import cv2
import numpy as np

#hsv range
lowerbound =np.array([20,100,100])
upperbound =np.array([30,255,255])

cap=cv2.VideoCapture(0)

while True:
    #read from frame
    ret,frame=cap.read()
    #check if frame is captured
    if not ret:
        break
    
    #convert frame to hsv
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #create mask
    mask=cv2.inRange(hsv,lowerbound,upperbound)
    #detecting contours
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #iterating contours
    for contour in contours:
        if cv2.contourArea(contour)>500:
            (x,y),radius=cv2.minEnclosingCircle(contour)
            center=(int(x),int(y))
            radius=int(radius)

            cv2.circle(frame,center,radius,(0, 255, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            text="Yellow Ball"
            font=cv2.FONT_HERSHEY_SIMPLEX
            font_scale=0.8
            colour=(0,255,255)
            thickness=2
            #calculating text size for position

            text_size=cv2.getTextSize(text,font,font_scale,thickness)[0]
            text_x=int(center[0]-text_size[0]/2)
            text_y=int(center[1]-radius-10)

            cv2.putText(frame,text,(text_x,text_y),font,font_scale,colour,thickness)

    cv2.imshow("yellow ball tracking",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
           
