#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class IniciandoTestes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_iniciando_testes(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//localhost%3A8080/vindula")
	print '-'*80
	print 'Logando no Vindula'
	print '-'*80
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
	print '-'*80
	print 'Excluindo Portlets Padroes do Vindula'
	print '-'*80	
        driver.find_element_by_link_text("Gerenciar portlets").click()
        driver.find_element_by_link_text("×").click()
        driver.find_element_by_css_selector("input.context").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_link_text("Gerenciar portlets").click()
        driver.find_element_by_link_text("×").click()
        driver.find_element_by_css_selector("input.context").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_css_selector("#portletsLeft > div.managePortletsLink > a[title=\"Exibir a tela de gerenciamento dos portlets\"]").click()
        driver.find_element_by_link_text("×").click()
        driver.find_element_by_css_selector("#portletmanager-plone-rightcolumn > div.portletAssignments > form > div.formControls > input.context").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_css_selector("#portletsLeft > div.managePortletsLink > a[title=\"Exibir a tela de gerenciamento dos portlets\"]").click()
        driver.find_element_by_link_text("×").click()
        driver.find_element_by_css_selector("#portletmanager-plone-rightcolumn > div.portletAssignments > form > div.formControls > input.context").click()
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
