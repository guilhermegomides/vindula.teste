#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestandoFormularioBasico(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_ando_formulario_basico(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
	print '-'*80
	print 'Logando no Vindula como Teste1'
	print '-'*80
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("teste1")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("teste")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
	print '-'*80
	print 'Acessando e respondendo formulario'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Teste Formulario')])[2]").click()
        driver.find_element_by_id("campo-de-texto").clear()
        driver.find_element_by_id("campo-de-texto").send_keys("Teste")
        driver.find_element_by_id("campo-texto-multiplas-linhas").clear()
        driver.find_element_by_id("campo-texto-multiplas-linhas").send_keys("teste\nteste\nteste\nteste\nteste")
        driver.find_element_by_id("verdadeiro-falso").click()
        Select(driver.find_element_by_name("campo-de-escolha")).select_by_visible_text("3")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").clear()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").send_keys("<p>TESTANDO</p>")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_id("datepicker-campo-data").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
        driver.find_element_by_link_text("11").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
	print '-'*80
	print 'Logando no Vindula como Teste2'
	print '-'*80	
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("teste2")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("teste")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Pasta de Testes").click()
	print '-'*80
	print 'Acessando e respondendo o formulario'
	print '-'*80	
        driver.find_element_by_xpath("(//a[contains(text(),'Teste Formulario')])[2]").click()
        driver.find_element_by_css_selector("div.formHelp").click()
        driver.find_element_by_id("campo-de-texto").clear()
        driver.find_element_by_id("campo-de-texto").send_keys("Teste")
        driver.find_element_by_id("campo-texto-multiplas-linhas").clear()
        driver.find_element_by_id("campo-texto-multiplas-linhas").send_keys("teste\nteste\nteste")
        driver.find_element_by_id("verdadeiro-falso").click()
        Select(driver.find_element_by_name("campo-de-escolha")).select_by_visible_text("5")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").clear()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").send_keys("<p>TESTE</p>")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_id("datepicker-campo-data").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-w").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-w").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-w").click()
        driver.find_element_by_link_text("15").click()
        driver.find_element_by_name("form.submited").click()
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
