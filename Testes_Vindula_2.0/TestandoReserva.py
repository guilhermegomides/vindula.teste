#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestandoReserva(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_ando_reserva(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
	print '-'*80
	print 'Logando no Vindula como administrador'
	print '-'*80
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_link_text("Pasta de Testes").click()
	print '-'*80
	print 'Adicionando Item Reserva dentro da Aplicacao Reserva'
	print '-'*80	
        driver.find_element_by_link_text("Teste Reserva").click()
        driver.find_element_by_css_selector("a[title=\"Adiciona novos itens dentro deste item\"] > span").click()
        driver.get("http://localhost:8080/vindula/pasta-de-testes/teste-reserva/++add++vindula.reservacorporativa.content.reserve")
        driver.find_element_by_id("form-widgets-IBasic-title").clear()
        driver.find_element_by_id("form-widgets-IBasic-title").send_keys("Teste1")
        driver.find_element_by_id("form-widgets-IBasic-description").clear()
        driver.find_element_by_id("form-widgets-IBasic-description").send_keys("Teste\nTeste")
        Select(driver.find_element_by_id("form-widgets-frequency")).select_by_visible_text("quinzenal")
        driver.find_element_by_id("form-widgets-local").clear()
        driver.find_element_by_id("form-widgets-local").send_keys("1 andar")
        driver.find_element_by_id("form-widgets-duration").clear()
        driver.find_element_by_id("form-widgets-duration").send_keys("02:00")
        driver.find_element_by_id("form-widgets-contact").clear()
        driver.find_element_by_id("form-widgets-contact").send_keys("guilhermepereira@liberiun.com")
        driver.find_element_by_id("form-widgets-replic_semana-0").click()
        driver.find_element_by_id("form-widgets-replic_start").clear()
        driver.find_element_by_id("form-widgets-replic_start").send_keys("12:00")
        driver.find_element_by_id("form-widgets-replic_end").clear()
        driver.find_element_by_id("form-widgets-replic_end").send_keys("14:00")
        driver.find_element_by_id("form-buttons-save").click()
        driver.find_element_by_css_selector("a[title=\"Altera o estado deste item\"]").click()
        driver.find_element_by_css_selector("span.subMenuTitle").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
	print '-'*80
	print 'Logando no Vindula como Teste1'
	print '-'*80	
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("teste1")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("teste")
        driver.find_element_by_name("submit").click()
	print '-'*80
	print 'Acessando e testando Reserva'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_link_text("Teste Reserva").click()
        driver.find_element_by_css_selector("a.external-link > p").click()
        driver.find_element_by_xpath("(//div[@id='day']/span)[3]").click()
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
	print '-'*80
	print 'Acessando e testando Reserva'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_link_text("Teste Reserva").click()
        driver.find_element_by_css_selector("a.external-link > p").click()
        driver.find_element_by_xpath("(//div[@id='day']/span)[8]").click()
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
