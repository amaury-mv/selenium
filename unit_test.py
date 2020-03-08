from selenium import webdriver
#llamdo de teclado
from selenium.webdriver.common.keys import Keys
import time
import unittest


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://qa03.factocloud.com.mx/facto/")
        self.assertIn("Facto", driver.title)
        usuario = driver.find_element_by_id("j_idt12:userName")
        usuario.send_keys("maximolider")
        password = driver.find_element_by_name("j_idt12:password")
        password.send_keys("vb1596Mt5GqM")
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No se encontro el elemento " not in driver.page_source
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()