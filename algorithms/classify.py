import cv2
import numpy as np
from PIL import Image
import pytesseract
import sys
import os

def LABConversion(img):
    height, width = img.shape[:2]
    labImg=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    green = 0.0
    yellow = 0.0
    brown = 0.0

    for i in range(height):
        for k in range(width):
            L,a,b = labImg[i][k]
            a = a - 128
            b = b - 128
            L = L * 100 / 225
            if L != 100 and L != 0:
                if a < 18 and b > 47 and a > -17:
                    yellow += 1
                elif a < -7:
                    green += 1
                elif a > 10 and b < 47 and L > 19:
                    brown += 1

    total = green + yellow + brown
    greenPer = (green/total)*100
    yellowPer = (yellow/total)*100
    brownPer = (brown/total)*100
    print("green: ", greenPer)
    print("yellow: ", yellowPer)
    print("brown: ", brownPer)
    if brownPer >= 35:
        if brownPer >= 50:
            classType = "Very Over Ripe"
            print("banana is very over ripe")
        else:
            classType = "Over Ripe"
            print("banana is over ripe")
    elif greenPer >= 30:
        if greenPer >= 60:
            classType = "Very Unripe"
            print("banana is very unripe")
        else:
            classType = "Unripe"
            print("banana is unripe")
    elif yellowPer > 50:
        classType = "Ripe"
        print("banana is ripe")
    else:
        classType = "Over Ripe"
        print("banana is over ripe")
    return classType

def rmvWhiteBackground(img):
    #use this if loading in bgr
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_rgb = img
    #image hsv
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

    #colour values for green
    G_lower = np.array([28,46,45])
    G_upper = np.array([70,255,255])

    #green mask
    green_mask = cv2.inRange(img_hsv, G_lower, G_upper)
    green_mask_inv = cv2.bitwise_not(green_mask)

    #yellow values
    Y_lower = np.array([18,85,0])
    Y_upper = np.array([28,255,255])

    #brown values
    B_lower = np.array([2,20,20])
    B_upper = np.array([12,255,150])

    #yellow mask
    yellow_mask = cv2.inRange(img_hsv, Y_lower, Y_upper)
    yellow_mask_inv = cv2.bitwise_not(yellow_mask)

    #brown mask
    brown_mask = cv2.inRange(img_hsv, B_lower, B_upper)
    brown_mask_inv = cv2.bitwise_not(brown_mask)

    #mask on rgb img. Each of these are only used for testing purposes.
    Y_banana = cv2.bitwise_and(img_rgb, img_rgb, mask=yellow_mask)
    Y_background = cv2.bitwise_and(img_rgb, img_rgb, mask=yellow_mask_inv)
    G_banana = cv2.bitwise_and(img_rgb, img_rgb, mask=green_mask)
    G_background = cv2.bitwise_and(img_rgb, img_rgb, mask=green_mask_inv)
    B_banana = cv2.bitwise_and(img_rgb, img_rgb, mask=brown_mask)
    B_background = cv2.bitwise_and(img_rgb, img_rgb, mask=brown_mask_inv)

    #Combine masks into one picture to get to total banana
    banana = cv2.bitwise_and(img_hsv, img_hsv, mask=green_mask+yellow_mask+brown_mask)
    background = cv2.bitwise_and(img_hsv, img_hsv, mask=brown_mask_inv+yellow_mask_inv+green_mask_inv)

    #showimg('background', background)
    #showimg('banana', banana)

    #convert the picure thie the background removed back to rgb for colour space LAB analysis
    banana = cv2.cvtColor(banana, cv2.COLOR_HSV2BGR)

    classType = LABConversion(banana)
    H, S, V = cv2.split(banana)
    return classType

# get image

def classifyBanana(fp):
    rawimg = cv2.imread(fp)
    #remove background
    classType = rmvWhiteBackground(rawimg)
    return classType
