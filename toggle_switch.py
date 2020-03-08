import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ToggleSwitch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_toggle(self):
        driver = self.driver        
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        toggle = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/label[3]/div")
        toggle.click()
        time.sleep(3)
        toggle.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
