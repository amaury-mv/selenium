from selenium import webdriver
#llamdo de teclado
from selenium.webdriver.common.keys import Keys
import time
import unittest

class Xpath(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_for_xpath(self):
        driver = self.driver
        driver.get("http://qa03.factocloud.com.mx/facto/")
        
        usuario = driver.find_element_by_id("j_idt12:userName")
        usuario.send_keys("maximolider")
        password = driver.find_element_by_name("j_idt12:password")
        password.send_keys("vb1596Mt5GqM")
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        xpath_element = driver.find_element_by_xpath("//*[@id='menuform:um_cfdi']")
        xpath_element.click()
        time.sleep(5)

    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()

