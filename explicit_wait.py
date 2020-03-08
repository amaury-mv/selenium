from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import unittest


class ExplicitWait(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_expected_wait(self):
        driver = self.driver    
        driver.get("http://qa03.factocloud.com.mx/facto/")
        #intentos 
        try:
            #intenta cargar durante 10 veces hasta que encuentre el elemento q, si no lo encuentar madna timeout
            element = WebDriverWait(driver,10).until(
            ec.presence_of_element_located((By.NAME,"j_idt12:userName"))
            )
        
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()







