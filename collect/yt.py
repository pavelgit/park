import pafy
import cv2

url = 'https://www.youtube.com/watch?v=RuSIx4fJvgw'
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="webm")

#start the video
cap = cv2.VideoCapture(play.url)
while (True):
    ret,frame = cap.read()
    """
    your code....
    """
    cv2.imshow('frame',frame)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break    

cap.release()
cv2.destroyAllWindows()