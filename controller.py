#opencv用的function
import os
import cv2
import numpy as np


#pyqt5用的function
from PyQt5 import QtWidgets
from Ui_Hwgui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from img_controller import img_controller


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        
    def setup_control(self):

        #避免修改功能的程式過於冗，將其寫到另外一個檔案並將其命名把東西繼承過來
        path1=''
        path2=''
        self.img_controller=img_controller(path1,path2)

                                    

        self.ui.Load_image1.clicked.connect(self.open_file1)
        self.ui.Load_image2.clicked.connect(self.open_file2)        
        self.ui.One1_button.clicked.connect(self.img_controller.color_seperation)
        self.ui.One2_button.clicked.connect(self.img_controller.color_transformation)
        self.ui.One3_button.clicked.connect(self.img_controller.color_detection)
        self.ui.One4_button.clicked.connect(self.img_controller.blending)
        self.ui.Two1_button.clicked.connect(self.img_controller.gaussian_filter)
        self.ui.Two2_button.clicked.connect(self.img_controller.bilateral_filter)
        self.ui.Two3_button.clicked.connect(self.img_controller.median_filter)

    def open_file1(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./") # start path  
        original=cv2.imread(filename)      
        cv2.imshow('Original_image1',original)
        self.ui.image1_name.setText('Picture is loaded')
        self.img_controller.set_path1(filename)
        cv2.waitKey(0)

    
    def open_file2(self):
        filename,filetype=QFileDialog.getOpenFileName(self, "Open file", "./") # start path 
        original=cv2.imread(filename) 
        cv2.imshow('Original_image2',original)
        self.ui.image_name2.setText('Picture is loaded')
        self.img_controller.set_path2(filename)
        cv2.waitKey(0)



    



    
#啟動檔案把GUI頁面打開
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())