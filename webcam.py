import cv2 , time 
video = cv2.VideoCapture(0)
a = 0 
while 1 : 
    a = a + 1 
    cheak,frame = video.read()
    print(cheak)
    print(frame)
    # show the frame 
    cv2.imshow('capturing' , frame)
    key = cv2.waitKey(1) 
    if key == ord('e') : 
        break 
# show number of frames tooked
print(a)
# shutdown the cam
video.release()
cv2.destroyAllWindows