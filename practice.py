import sys
import cv2
img = cv2.imread('C:\Users\lifeg\OneDrive\Pictures\210913_CMS_LemonadeStands.jpg', cv2.IMREAD_ANYCOLOR)

while True:
    cv2.imshow('People' img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
cv2.destroyAllWindows() # destroy all windows
print ('Welcome to the IQ GAME OF CHAMP ')