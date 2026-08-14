import pyautogui
import numpy as np
import cv2
import matplotlib.pyplot as plt
###used to get a black-white picture of a certain region
def get_pic(regiojet):
    img = pyautogui.screenshot('my_screenshot.png', region = regiojet)
    print(img)
    img = np.array(img) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # black and white conversion
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1] # all values over 127 converted to 255(white)
    # plt.imshow(thresh,cmap='grey'),# unhash to view photo
    # plt.show()
    return thresh