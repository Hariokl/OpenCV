import cv2 as cv
import numpy as np


def nothing(t):
    ...


def draw(im, b=False):
    global mode
    c = [(255-x) for x in bgc]
    if b:
        c = bgc
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(im, mode, (0, len(im)-10), font, 1, c, 1)


def mouse(event, x, y, flags, param):
    global bul, mode
    if event == cv.EVENT_LBUTTONDOWN:
        bul = True
    if event == cv.EVENT_LBUTTONUP:
        bul = False
    if bul:
        if event == cv.EVENT_MOUSEMOVE:
            if mode == 'Draw':
                c = (255, 255, 255)
            else:
                c = bgc
            cv.circle(img, (x, y), cv.getTrackbarPos('Thickness', 'image'), c, -1)



img = np.zeros((512, 512, 3), np.uint8)

cv.namedWindow('image')
cv.createTrackbar('Thickness', 'image', 1, 20, nothing)

cv.setMouseCallback('image', mouse)
bul = False
mode = 'Draw'
bgc = (0, 0, 0)
while True:
    draw(img)
    cv.imshow('image', img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break
    if k == ord('m'):
        draw(img, True)
        mode = 'Erase' if mode == 'Draw' else 'Draw'
cv.destroyAllWindows()
