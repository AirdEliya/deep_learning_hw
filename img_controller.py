from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np

class img_controller(object):
    def __init__(self,img1_path,img2_path):
        self.img_path1=img1_path
        self.img_path2= img2_path

    def set_path1(self, img1_path):
        self.img_path1 = img1_path

    def set_path2(self, img2_path):
        self.img_path2 = img2_path

    def color_seperation(self):
        img=cv2.imread(self.img_path1)
        (B,G,R)=cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype = "uint8")
        cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
        cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
        cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))


    def color_transformation(self):
        img=cv2.imread(self.img_path1)
        (B,G,R)=cv2.split(img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('OpenCV function',img_gray)
        cv2.waitKey(0)
        # #不要寫成(R+G+B)/3，會出現超過255從0計算的悲劇
        data=R/3+G/3+B/3
        data = data / data.max() #normalizes data in range 0 - 255
        data = 255 * data
        img_avg = data.astype(np.uint8)

        cv2.imshow("Average_weighted", img_avg)
        cv2.waitKey(0)


    def color_detection(self):
        img=cv2.imread(self.img_path1)
        hsv_img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_green=np.array([40,50,20])
        higher_green=np.array([80,255,255])
        green_mask=cv2.inRange(hsv_img,lower_green,higher_green)

        lower_white=np.array([0,0,200])
        higher_white=np.array([180,20,255])
        white_mask=cv2.inRange(hsv_img,lower_white,higher_white)

        # cv2.imshow('Green mask',green_mask)
        # cv2.imshow('White mask',white_mask)

        green_bit=cv2.bitwise_and(img,img,mask = green_mask)
        white_bit=cv2.bitwise_and(img,img,mask = white_mask)

        cv2.imshow('Green Detection',green_bit)
        cv2.imshow('White Detection',white_bit)


    def blending(self):
        img1=cv2.imread(self.img_path1)
        img2=cv2.imread(self.img_path2)
        alpha_slider_max = 255
        title_window = 'Blend'
        def on_trackbar(val):
            alpha = val / alpha_slider_max
            beta = ( 1.0 - alpha )
            dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
            cv2.imshow(title_window, dst)
        src2 = img1
        src1 = img2
        cv2.namedWindow(title_window)
        trackbar_name = 'Blend'
        cv2.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)

        # Show some stuff
        on_trackbar(0)
        # Wait until user press some key
        cv2.waitKey()

    def gaussian_filter(self):
        img=cv2.imread(self.img_path2)
        slider_max = 10
        title_window = 'Gaussian Blur'
        def on_trackbar(val):
            if val==0:
                dst=img
                cv2.imshow(title_window,dst)
            else:
                kernel=2*val+1
                dst=cv2.GaussianBlur(img,(kernel,kernel),0)
                cv2.imshow(title_window,dst)

        cv2.namedWindow(title_window)
        trackbar_name = 'Magnitude'
        cv2.createTrackbar(trackbar_name, title_window , 0, slider_max, on_trackbar)
        on_trackbar(0)
        cv2.waitKey()

    def bilateral_filter(self):
        img=cv2.imread(self.img_path2)
        slider_max=10
        title_window='Bilateral Blur'
        def on_trackbar(val):
            if val==0:
                dst=img
                cv2.imshow(title_window,dst)
            else:
                kernel=2*val+1
                dst=cv2.bilateralFilter(img,kernel,90,90)
                cv2.imshow(title_window,dst)

        cv2.namedWindow(title_window)
        trackbar_name='Magnitude'
        cv2.createTrackbar(trackbar_name,title_window,0,slider_max,on_trackbar)
        on_trackbar(0)
        cv2.waitKey()

    def median_filter(self):
        img=cv2.imread(self.img_path2)
        slider_max=10
        title_window='Median Filter'
        def on_trackbar(val):
            if val==0:
                dst=img
                cv2.imshow(title_window,dst)
            else:
                kernel=2*val+1
                dst=cv2.medianBlur(img, kernel)
                cv2.imshow(title_window,dst)

        cv2.namedWindow(title_window)
        trackbar_name='Magnitude'
        cv2.createTrackbar(trackbar_name,title_window,0,slider_max,on_trackbar)
        on_trackbar(0)
        cv2.waitKey()



