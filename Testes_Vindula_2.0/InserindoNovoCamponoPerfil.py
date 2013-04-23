#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class InserindoNovoCamponoPerfil(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_inserindo_novo_campono_perfil(self):
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
        driver.find_element_by_id("user-name").click()
        print '-'*80
	print 'Inserindo novo campo no Perfil'
	print '-'*80	
        driver.find_element_by_link_text("Painel de Controle").click()
        driver.find_element_by_xpath("(//div[@id='topic'])[2]").click()
        driver.find_element_by_css_selector("span[name=\" http://localhost:8080/vindula/myvindulaconfgs\"]").click()
        driver.find_element_by_link_text("Cadastrar novo campo").click()
        driver.find_element_by_id("fields").clear()
        driver.find_element_by_id("fields").send_keys("Testando novo campo")
        driver.find_element_by_id("ativo_edit").click()
        driver.find_element_by_id("ativo_view").click()
        driver.find_element_by_id("label").clear()
        driver.find_element_by_id("label").send_keys("Novo Campo")
        driver.find_element_by_id("decription").clear()
        driver.find_element_by_id("decription").send_keys("Campo")
        driver.find_element_by_id("required").click()
        Select(driver.find_element_by_name("type")).select_by_visible_text("Campo Texto Múltiplas Linhas")
        Select(driver.find_element_by_name("area_de_view")).select_by_visible_text("Outros")
        driver.find_element_by_name("form.submited").click()
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
        driver.find_element_by_id("user-name").click()
        print '-'*80
	print 'Editando novo campo no perfil'
	print '-'*80	
        driver.find_element_by_link_text("Meu Perfil").click()
        driver.find_element_by_link_text("Editar Perfil").click()
        driver.find_element_by_id("testando-novo-campo").clear()
        driver.find_element_by_id("testando-novo-campo").send_keys("Teste Novo Campo")
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
        driver.find_element_by_id("user-name").click()
        print '-'*80
	print 'Editando novo campo no perfil'
	print '-'*80	
        driver.find_element_by_link_text("Meu Perfil").click()
        driver.find_element_by_link_text("Editar Perfil").click()
        driver.find_element_by_id("testando-novo-campo").clear()
        driver.find_element_by_id("testando-novo-campo").send_keys("Teste Novo Campo")
        driver.find_element_by_name("form.submited").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
        driver.find_element_by_id("__ac_name").clear()
        print '-'*80
	print 'Logando no Vindula como administrador'
	print '-'*80	
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_id("user-name").click()
        print '-'*80
	print 'Excluindo campo criado'
	print '-'*80	
        driver.find_element_by_link_text("Painel de Controle").click()
        driver.find_element_by_xpath("(//div[@id='topic'])[2]").click()
        driver.find_element_by_css_selector("span[name=\" http://localhost:8080/vindula/myvindulaconfgs\"]").click()
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
