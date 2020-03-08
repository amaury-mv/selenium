import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#descargar pip install opencv-python capitulo 12
import cv2
import time


class Cv2(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_screenshot_open_cv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot('img2.png')
        time.sleep(3)

    def test_comparing_images(self):
        img1= cv2.imread('img1.png')
        img2 = cv2.imread('img2.png')

        diferencia = cv2.absdiff(img1,img2)
        image_gris = cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(image_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) >= 20:
                possicion_x,possicion_y,ancho,alto = cv2.boundingRect(c)
                cv2.rectangle(img1,(possicion_x,possicion_y),(possicion_x+ancho,possicion_y,alto),(0,0,255),2)