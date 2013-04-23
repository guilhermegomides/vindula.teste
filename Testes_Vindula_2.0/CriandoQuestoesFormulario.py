#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CriandoQuestoesFormulario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_criando_questoes_formulario(self):
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
        print '-'*80
	print 'Adicionando novos campos ao formulario'
	print '-'*80	
        driver.find_element_by_link_text("Pasta de Testes").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Teste Formulario')])[2]").click()
        driver.find_element_by_link_text("Editar Campos").click()
        driver.find_element_by_name("form.submited").click()
        Select(driver.find_element_by_name("type_fields")).select_by_visible_text("Campo de Texto")
        driver.find_element_by_id("name_field").clear()
        driver.find_element_by_id("name_field").send_keys("Campo de texto")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Compo Texto")
        driver.find_element_by_id("description_fields").clear()
        driver.find_element_by_id("description_fields").send_keys("Teste")
        driver.find_element_by_id("required").click()
        driver.find_element_by_id("flag_ativo").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_name("form.submited").click()
        Select(driver.find_element_by_name("type_fields")).select_by_visible_text("Campo Texto Multiplas Linhas")
        driver.find_element_by_id("name_field").clear()
        driver.find_element_by_id("name_field").send_keys("Campo texto multiplas linhas")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Campo texto multiplas linhas")
        driver.find_element_by_id("required").click()
        driver.find_element_by_id("flag_ativo").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_name("form.submited").click()
        Select(driver.find_element_by_name("type_fields")).select_by_visible_text("Campo Verdadeiro/Falso")
        driver.find_element_by_id("name_field").clear()
        driver.find_element_by_id("name_field").send_keys("Verdadeiro/Falso")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Verdadeiro/falso")
        driver.find_element_by_id("required").click()
        driver.find_element_by_id("flag_ativo").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_name("form.submited").click()
        Select(driver.find_element_by_name("type_fields")).select_by_visible_text("Campo de Escolha")
        driver.find_element_by_id("name_field").clear()
        driver.find_element_by_id("name_field").send_keys("Campo de escolha")
        driver.find_element_by_id("list_values").clear()
        driver.find_element_by_id("list_values").send_keys("1\n2\n3\n4\n5")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Campo de escolha")
        driver.find_element_by_id("required").click()
        driver.find_element_by_id("flag_ativo").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_name("form.submited").click()
        Select(driver.find_element_by_name("type_fields")).select_by_visible_text("Campo de Texto Rico")
        driver.find_element_by_id("name_field").clear()
        driver.find_element_by_id("name_field").send_keys("Campo de texto rico")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Campo texto rico")
        driver.find_element_by_id("required").click()
        driver.find_element_by_id("flag_ativo").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_id("name_field").clear()
        driver.find_element_by_id("name_field").send_keys("Campo data")
        Select(driver.find_element_by_name("type_fields")).select_by_visible_text("Campo de Data")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Campo Data")
        driver.find_element_by_id("required").click()
        driver.find_element_by_id("flag_ativo").click()
        driver.find_element_by_name("form.submited").click()
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
