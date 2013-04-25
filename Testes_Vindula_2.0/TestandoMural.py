#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestandoMural(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_ando_mural(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_link_text("Mural").click()
        driver.find_element_by_name("new-howareu").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("Administrador > Comentario Mural")
        driver.find_element_by_css_selector("input.context.bt_comments").click()
        driver.get(self.base_url + "/vindula")
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
        driver.get(self.base_url + "/vindula/logged_out")
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("teste1")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("teste")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_link_text("Mural").click()
        driver.find_element_by_name("new-howareu").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("Teste1 > Comentario Mural")
        driver.find_element_by_css_selector("input.context.bt_comments").click()
        driver.get(self.base_url + "/vindula")
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
        driver.get(self.base_url + "/vindula/logged_out")
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("teste2")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("teste")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_link_text("Mural").click()
        driver.find_element_by_name("new-howareu").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("Teste2 > Comentario Mural")
        driver.find_element_by_css_selector("input.context.bt_comments").click()
        driver.get(self.base_url + "/vindula")
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_link_text("Mural").click()
        driver.find_element_by_xpath("//input[@id='1']").click()
        driver.find_element_by_id("text").clear()
        driver.find_element_by_id("text").send_keys("Administrador > Comentario > Comentario")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
