#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TestandoMemorando(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_ando_memorando(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//localhost%3A8080/vindula")
        print '-'*80
	print 'Logando no Vindula como Administrador'
	print '-'*80
	driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        print '-'*80
	print 'Adicionando item Memorando dentro da aplicacao'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Teste Memorandos')])[2]").click()
        driver.find_element_by_css_selector("a[title=\"Adiciona novos itens dentro deste item\"] > span").click()
        driver.find_element_by_id("memorando").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Testando")
        driver.find_element_by_id("number").clear()
        driver.find_element_by_id("number").send_keys("78965487")
        Select(driver.find_element_by_id("edit_form_date_0_day")).select_by_visible_text("5")
        Select(driver.find_element_by_id("edit_form_date_0_month")).select_by_visible_text("novembro")
        Select(driver.find_element_by_id("edit_form_date_0_year")).select_by_visible_text("2001")
        Select(driver.find_element_by_id("edit_form_date_0_hour")).select_by_visible_text("17")
        Select(driver.find_element_by_id("edit_form_date_0_minute")).select_by_visible_text("40")
        driver.find_element_by_id("email_to").clear()
        driver.find_element_by_id("email_to").send_keys("guilhermepereira@liberiun.com")
        driver.find_element_by_id("email_from").clear()
        driver.find_element_by_id("email_from").send_keys("")
        driver.find_element_by_id("email_from").clear()
        driver.find_element_by_id("email_from").send_keys("guilhermepereira@liberiun.com")
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").clear()
        driver.find_element_by_css_selector("textarea.cke_source.cke_enable_context_menu").send_keys("<p>TESTANDO</p>")
        driver.find_element_by_id("portal-columns").click()
        driver.find_element_by_id("cke_8_label").click()
        driver.find_element_by_name("form.button.save").click()
        driver.find_element_by_css_selector("span.state-private").click()
        driver.find_element_by_css_selector("span.subMenuTitle").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
        print '-'*80
	print 'Logando no Vindula com usuario Teste1'
	print '-'*80	
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("teste1")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("teste")
        driver.find_element_by_name("submit").click()
        print '-'*80
	print 'Verificando Memorando'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Teste Memorandos')])[2]").click()
        driver.find_element_by_css_selector("h2").click()
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
