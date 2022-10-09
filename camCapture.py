import cv2

cap = cv2.VideoCapture(0) # 0 default webcam, or file path

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# For writing the video - 20 fps
writer = cv2.VideoWriter("myVideoTry.mp4", cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

while True:
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    writer.write(frame)
    cv2.imshow("frame", frame)

    # Exit pressing q, or 27 for esc
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

writer.release()
cap.release()
cv2.destroyAllWindow()


