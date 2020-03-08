from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class TabNavigation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_change_tab(self):
        driver = self.driver
        #las pestañas se cuentan desde la ventana 0 
        driver.get("http://qa03.factocloud.com.mx/facto/")
        time.sleep(2)
        driver.execute_script("window.open('');")
        time.sleep(2)
        #cambio a la ventana 2
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://www.google.com")
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[0])        

if __name__ == "__main__":
    unittest.main()
