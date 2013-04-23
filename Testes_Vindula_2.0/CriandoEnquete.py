# -*- coding: latin1 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CriandoEnquete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_criando_enquete(self):
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
        driver.find_element_by_link_text("Pasta de Testes").click()
	print '-'*80
	print 'Adicionando aplicacao Enquete'
	print '-'*80
        driver.find_element_by_css_selector("a[title=\"Adiciona novos itens dentro deste item\"] > span").click()
        driver.get(self.base_url + "/vindula/pasta-de-testes/portal_factory/PlonePopoll/plonepopoll.2013-04-12.5149592040/edit")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Teste Enquete")
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("Teste")
        driver.find_element_by_id("question").clear()
        driver.find_element_by_id("question").send_keys("I ai?")
        driver.find_element_by_id("choices").clear()
        driver.find_element_by_id("choices").send_keys("Otimo\nPerfeito\nBom\nRuim\nPessimo")
        driver.find_element_by_name("form.button.save").click()
        print '-'*80
	print 'Alterando estado de privado para Publico'
	print '-'*80		
        driver.find_element_by_css_selector("span.state-private").click()
        driver.find_element_by_css_selector("span.subMenuTitle").click()
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
