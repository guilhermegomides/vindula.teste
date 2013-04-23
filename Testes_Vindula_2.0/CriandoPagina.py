#-*-coding: latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CriandoPagina(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_criando_pagina(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
	print '-'*80
	print 'Logando no vindula com o usuario administrador'
	print '-'*80
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Pasta de Testes").click()
	print '-'*80
	print 'Criando conteudo pagina'
	print '-'*80	
        driver.find_element_by_css_selector("a[title=\"Adiciona novos itens dentro deste item\"] > span").click()
	driver.get(self.base_url + "/vindula/pasta-de-testes/portal_factory/VindulaNews/vindulanews.2013-04-11.7150949640/edit")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Testando Pagina")
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("Testando Pagina")
        driver.find_element_by_id("imageCaption").clear()
        driver.find_element_by_id("imageCaption").send_keys("Pagina")
        driver.find_element_by_name("form.button.save").click()
	print '-'*80
	print 'Alterando o estado da aplicacao de privado para publico'
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
	print 'Teste Finalizado \nTeste OK'
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
