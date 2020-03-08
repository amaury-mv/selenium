import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class SelectOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/select")
        #find_elements_by_tag_name busca por la opcion del tag del navegador
        opcion = select.find_elements_by_tag_name("option")
        time.sleep(3)

        for option in opcion:
            #print("Los valores son : %s " % option.get_attibute("value"))
            option.click()
            time.sleep(3)
        
        selecionar = Select(driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/select"))
        selecionar.select_by_value("10")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()




