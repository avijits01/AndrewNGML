import cv2
import numpy as np
imgL=cv2.cvtColor(cv2.imread('right.png'),cv2.COLOR_BGR2GRAY)
print(imgL.shape)
