# -*- coding: latin1 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CriandoFormularioBasico(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_criando_formulario_basico(self):
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
	print 'Adicionando aplicacao Formulario Basico'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_css_selector("a[title=\"Adiciona novos itens dentro deste item\"] > span").click()
        driver.get(self.base_url + "/vindula/pasta-de-testes/++add++vindula.contentcore.formulariobasico")
        driver.find_element_by_id("form-widgets-IBasic-title").clear()
        driver.find_element_by_id("form-widgets-IBasic-title").send_keys("Teste Formulario")
        driver.find_element_by_id("form-widgets-IBasic-description").clear()
        driver.find_element_by_id("form-widgets-IBasic-description").send_keys("Teste")
        driver.find_element_by_id("form-widgets-acao_saida-0").click()
        driver.find_element_by_id("form-widgets-list_email").clear()
        driver.find_element_by_id("form-widgets-list_email").send_keys("guilhermepereira@liberiun.com")
        driver.find_element_by_id("form-widgets-mensagem").clear()
        driver.find_element_by_id("form-widgets-mensagem").send_keys("Obrigado")
        driver.find_element_by_id("form-buttons-save").click()
        print '-'*80
	print 'Alterando o estado de privado para Publico'
	print '-'*80	
        driver.find_element_by_css_selector("span.state-private").click()
        driver.find_element_by_id("workflow-transition-publish_internally").click()
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
