# -*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CriandoPortletGerenciadorOcorrencias(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_criando_portlet_gerenciador_ocorrencias(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
	print '-'*80
	print 'Logando no vindula'
	print '-'*80
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
	print '-'*80
	print 'Criando Portlet para gerenciador de ocorrencias'
	print '-'*80
        driver.find_element_by_link_text("Gerenciar portlets").click()
        Select(driver.find_element_by_name(":action")).select_by_visible_text("Portlet Gerenciar Ocorrências")
        driver.find_element_by_id("form.title_portlet").click()
        driver.find_element_by_id("form.title_portlet").clear()
        driver.find_element_by_id("form.title_portlet").send_keys("Help Desk")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").clear()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").send_keys("<p>Testando Porlet Help Desk</p>")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_id("form.poi_tracker").clear()
        driver.find_element_by_id("form.poi_tracker").send_keys("teste")
        driver.find_element_by_name("form.poi_tracker.search").click()
        driver.find_element_by_name("form.poi_tracker").click()
        driver.find_element_by_name("form.poi_tracker.update").click()
        driver.find_element_by_id("form.actions.save").click()
        driver.find_element_by_css_selector("input.context").click()
	print '-'*80
	print 'Saindo do Vindula'
	print '-'*80
        driver.find_element_by_css_selector("img").click()
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
