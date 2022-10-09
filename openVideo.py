import cv2
import time

cap = cv2.VideoCapture("myVideoTry.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

if not cap.isOpened():
    print("Error: Video file not found or wrong codec used")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Writer at 20fps
        time.sleep(1/20)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
