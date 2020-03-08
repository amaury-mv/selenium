import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ImplicitWait(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)#segundos
        driver.get("http://qa03.factocloud.com.mx/facto/")
        dynamicElement = driver.find_element_by_name("j_idt12:userName")


if __name__ == "__main__":
    unittest.main()
