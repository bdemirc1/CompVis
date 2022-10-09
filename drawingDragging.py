import cv2
import numpy as np

# Variables
# True while mouse button True, false if button up
drawing = False
ix, iy = -1, -1

def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # Starting vertex ix, iy, bottom right vertex(x,y)
            cv2.rectangle(img, (ix, iy), (x, y), (255, 132, 65), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 132, 65), -1)

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_rectangle)

## Showing the image

img = np.zeros((512,512,3), np.int8)
while True:
    cv2.imshow("my_drawing", img)

    # If we've waited at least 1 ms AND we've pressed key ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()