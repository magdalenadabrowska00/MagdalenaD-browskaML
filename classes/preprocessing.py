# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:16:14 2022

@author: Magda
"""
import cv2
import numpy as np

film = cv2.VideoCapture(
    'C:\\Users\\Magda\\Desktop\\Magda nauka\\Informatyka\\Semestr 5\\Uczenie maszynowe\\box.MP4')
w = int(film.get(3))
h = int(film.get(4))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('C:\\Users\\Magda\\Desktop\\Magda nauka\\Informatyka\\Semestr 5\\Uczenie maszynowe\\extracted.mp4', fourcc, 50.0, (w, h), True)

bgSubstractor = cv2.createBackgroundSubtractorMOG2()
kernel_o = np.ones((6,6),np.uint8)
kernel_c = np.ones((10,10),np.uint8)

while (True):
    bul, klatka = film.read()
    if bul:
        height, width, layers = klatka.shape

        klatka_hsv = cv2.cvtColor(klatka, cv2.COLOR_BGR2HSV)
        low_red1 = np.array([169, 170, 20])
        high_red1 = np.array([179, 255, 255])
        red_mask1 = cv2.inRange(klatka_hsv, low_red1, high_red1)

        low_red2 = np.array([0, 170, 20])
        high_red2 = np.array([9, 255, 255])
        red_mask2 = cv2.inRange(klatka_hsv, low_red2, high_red2)

        red_mask = cv2.bitwise_or(red_mask1, red_mask2)

        low_blue = np.array([112, 170, 20])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(klatka_hsv, low_blue, high_blue)

        maska = blue_mask | red_mask1 | red_mask2
        fgmask = bgSubstractor.apply(klatka_hsv)

        klatka = cv2.bitwise_and(klatka, klatka, mask=maska&fgmask)

        oczyszczonaKlatka = cv2.morphologyEx(cv2.morphologyEx(klatka, cv2.MORPH_OPEN, kernel_o), cv2.MORPH_CLOSE, kernel_c)

        out.write(oczyszczonaKlatka)
        cv2.imshow('oczyszczonaKlatka', oczyszczonaKlatka)
        stopNumber = cv2.waitKey(5) & 0xFF
        if stopNumber == 27:
            break

    else:
        break

film.release()
out.release()
cv2.destroyAllWindows()