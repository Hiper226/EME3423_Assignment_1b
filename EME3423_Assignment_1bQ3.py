import cv2
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    s, img = capture.read()
    im2 = cv2.flip(img,1) # mirror
    im3 = cv2.flip(img, 0) # flip
    im4 = cv2.flip(img, -1) # mirror flip

    combine1 = np.concatenate((img, im2), axis=1)
    combine2 = np.concatenate((im3, im4), axis=1)
    combine3 = np.concatenate((combine1, combine2), axis=0)

    cv2.imshow("Q3", combine3)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()