from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class ReturnPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_return_forward_page(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.facebook.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()

if __name__ == "__main__":
    unittest.main()
