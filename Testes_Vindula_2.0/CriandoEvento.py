#-*-coding: latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CriandoEvento(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_criando_evento(self):
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
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_css_selector("a[title=\"Adiciona novos itens dentro deste item\"] > span").click()
	print '-'*80
	print 'Criando conteudo evento'
	print '-'*80	
        driver.get(self.base_url + "/vindula/pasta-de-testes/portal_factory/Event/event.2013-04-11.2750040282/edit")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Evento")
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("Evento")
        driver.find_element_by_id("location").clear()
        driver.find_element_by_id("location").send_keys("1 andar")
        Select(driver.find_element_by_id("edit_form_startDate_0_day")).select_by_visible_text("21")
        Select(driver.find_element_by_id("edit_form_startDate_0_month")).select_by_visible_text("novembro")
        Select(driver.find_element_by_id("edit_form_startDate_0_year")).select_by_visible_text("2018")
        Select(driver.find_element_by_id("edit_form_startDate_0_hour")).select_by_visible_text("07")
        Select(driver.find_element_by_id("edit_form_startDate_0_minute")).select_by_visible_text("55")
        Select(driver.find_element_by_id("edit_form_endDate_1_day")).select_by_visible_text("12")
        Select(driver.find_element_by_id("edit_form_endDate_1_month")).select_by_visible_text("outubro")
        Select(driver.find_element_by_id("edit_form_endDate_1_year")).select_by_visible_text("2007")
        Select(driver.find_element_by_id("edit_form_endDate_1_hour")).select_by_visible_text("19")
        Select(driver.find_element_by_id("edit_form_endDate_1_minute")).select_by_visible_text("10")
        Select(driver.find_element_by_id("edit_form_startDate_0_year")).select_by_visible_text("2001")
        driver.find_element_by_id("attendees").clear()
        driver.find_element_by_id("attendees").send_keys("Todo Mundo")
        driver.find_element_by_id("contactName").clear()
        driver.find_element_by_id("contactName").send_keys("Teste")
        driver.find_element_by_id("contactEmail").clear()
        driver.find_element_by_id("contactEmail").send_keys("teste")
        driver.find_element_by_id("contactPhone").clear()
        driver.find_element_by_id("contactPhone").send_keys("teste")
        driver.find_element_by_id("cmfeditions_version_comment").clear()
        driver.find_element_by_id("cmfeditions_version_comment").send_keys("teste")
        driver.find_element_by_name("form.button.save").click()
        driver.find_element_by_id("contactEmail").clear()
        driver.find_element_by_id("contactEmail").send_keys("teste@email.com")
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
