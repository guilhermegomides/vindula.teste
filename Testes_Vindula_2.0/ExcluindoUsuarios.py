#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ExcluindoUsuarios(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_excluindo_usuarios(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
	print '-'*80
	print 'Logando no Vindula'
	print '-'*80	
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
	print '-'*80
	print 'Excluindo Usuarios (Teste1, Teste2, Teste3)'
	print '-'*80	
        driver.find_element_by_link_text("Painel de Controle").click()
        driver.find_element_by_xpath("(//div[@id='topic'])[2]").click()
        driver.find_element_by_link_text("Usuários e Grupos").click()
        driver.find_element_by_xpath("(//input[@name='delete:list'])[12]").click()
        driver.find_element_by_xpath("(//input[@name='delete:list'])[13]").click()
        driver.find_element_by_xpath("(//input[@name='delete:list'])[14]").click()
        driver.find_element_by_name("form.button.Modify").click()
        driver.find_element_by_css_selector("img").click()
	print '-'*80
	print 'Saindo do Vindula'
	print '-'*80	
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
	print '-'*80
	print 'Teste finalizado \nTeste OK'
	print '-'*80	
    
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
