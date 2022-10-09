import cv2
import numpy as np

#Drawing on images

# Connecting callback functions
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # (x,y) center of circle, 100 radius
        cv2.circle(img, (x,y), 100, (0,255,255), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

## Showing the image

img = np.zeros((512,512,3), np.int8)
while True:
    cv2.imshow("my_drawing", img)

    # If we've waited at least 1 ms AND we've pressed key ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()