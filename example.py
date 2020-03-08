from selenium import webdriver
#llamdo de teclado
from selenium.webdriver.common.keys import Keys
import time



#selenium version = 3.141.0

#driver = webdriver.Firefox(execuatable_path=r"/home/amaury/Documentos/Selenium/geckodriver")
#in linux dejar geckodriver in /usr/bin
driver = webdriver.Firefox()
driver.get("http://qa03.factocloud.com.mx/facto/")

usuario = driver.find_element_by_id("j_idt12:userName")
usuario.send_keys("maximolider")


password = driver.find_element_by_name("j_idt12:password")
password.send_keys("vb1596Mt5GqM")
password.send_keys(Keys.ENTER)






