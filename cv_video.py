import numpy as np
import cv2 as cv

cap = cv.VideoCapture('Hambleton.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    height, width = frame.shape[:2]
    frame = cv.resize(frame, (int(0.5*width), int(0.5*height)), interpolation = cv.INTER_CUBIC)
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    target = [
        [100, 100],
        [400, 500],
        [200, 500],
        [500, 100],
    ]

    pts1 = np.float32([[0, 0], [width, height], [0, height], [width, 0]])
    pts2 = np.float32(target)

    matrix = cv.getPerspectiveTransform(pts1, pts2)
    frame = cv.warpPerspective(frame, matrix, (800, 500))

    cv.circle(frame, tuple(target[0]), 5, (0, 0, 255), -1)
    cv.circle(frame, tuple(target[1]), 5, (0, 0, 255), -1)
    cv.circle(frame, tuple(target[2]), 5, (0, 0, 255), -1)
    cv.circle(frame, tuple(target[3]), 5, (0, 0, 255), -1)
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()