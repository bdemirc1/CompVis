import cv2

# Callback function rectangle
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_leftClicked, bot_RightClicked
    # Reset rectangle if drawn already
    if event == cv2.EVENT_LBUTTONDOWN:
        if top_leftClicked and bot_RightClicked:
            pt1 = pt2 = (0,0)
            top_leftClicked = bot_RightClicked = False
        if not top_leftClicked:
            pt1 = (x,y)
            top_leftClicked = True
        elif not bot_RightClicked:
            pt2 = (x,y)
            bot_RightClicked = True


# Global variables
pt1 = (0,0)
pt2 = (0,0)
top_leftClicked = bot_RightClicked = False

# Connect to the callback
cap = cv2.VideoCapture(0)

cv2.namedWindow("Test")
cv2.setMouseCallback("Test", draw_rectangle)


while True:

    ret, frame = cap.read()
    # Drawing the frame based off the global variables
    if top_leftClicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
    if top_leftClicked and bot_RightClicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 3)

    cv2.imshow("Test", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()