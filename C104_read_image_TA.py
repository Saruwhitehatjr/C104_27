import cv2
import numpy as np
black=np.zeros([600,600])
#print(black)

black[200:400,200:400]=255
#print(black)
cv2.imshow('black',black)

cv2.waitKey(0)