#-*-coding:latin1-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class InteracoesEntreUsuarios(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_interacoes_entre_usuarios(self):
        driver = self.driver
        driver.get(self.base_url + "/vindula/logged_out")
	print '-'*80
	print 'Logando no Vindula como Administrador'
	print '-'*80
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
	print '-'*80
	print 'Testando pensamentos'
	print '-'*80	
        driver.find_element_by_link_text("Meu Perfil").click()
        driver.find_element_by_link_text("Recados para Você").click()
        driver.find_element_by_link_text("Pensamentos").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("Teste pensamento")
        driver.find_element_by_css_selector("input.context.bt_comments").click()
        driver.find_element_by_css_selector("img").click()
	print '-'*80
	print 'Criando portlet para localizar usuarios'
	print '-'*80	
        driver.find_element_by_css_selector("#portletsLeft > div.managePortletsLink > a[title=\"Exibir a tela de gerenciamento dos portlets\"]").click()
        Select(driver.find_element_by_css_selector("#portletmanager-plone-rightcolumn > div.section > form > select[name=\":action\"]")).select_by_visible_text("Portlet busca de pessoas")
        driver.find_element_by_id("form.title_portlet").clear()
        driver.find_element_by_id("form.title_portlet").send_keys("Usuarios")
        driver.find_element_by_id("form.quantidade_portlet").clear()
        driver.find_element_by_id("form.quantidade_portlet").send_keys("5")
        driver.find_element_by_id("form.actions.save").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("teste1")
        driver.find_element_by_name("SearchSubmit").click()
	print '-'*80
	print 'Deixando recado para o usuario Teste1'
	print '-'*80	
        driver.find_element_by_css_selector("img[alt=\"teste1\"]").click()
        driver.find_element_by_link_text("Recados").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("Testando recado.")
        driver.find_element_by_name("submit").click()
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
        driver.find_element_by_name("name").clear()
	print '-'*80
	print 'Procurando usuario Teste1'
	print '-'*80	
        driver.find_element_by_name("name").send_keys("teste1")
        driver.find_element_by_name("SearchSubmit").click()
        driver.find_element_by_css_selector("img[alt=\"teste1\"]").click()
	print '-'*80
	print 'Deixando recado'
	print '-'*80	
        driver.find_element_by_link_text("Recados").click()
        driver.find_element_by_name("text").clear()
        driver.find_element_by_name("text").send_keys("Teste2 recados")
        driver.find_element_by_name("submit").click()
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
	print 'Verificando Recados'
	print '-'*80	
        driver.find_element_by_link_text("Meu Perfil").click()
        driver.find_element_by_link_text("Recados para Você").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("user-name").click()
        driver.find_element_by_link_text("Sair").click()
	print '-'*80
	print 'Logando no Vindula como Administrador'
	print '-'*80	
        driver.find_element_by_id("__ac_name").clear()
        driver.find_element_by_id("__ac_name").send_keys("administrador")
        driver.find_element_by_id("__ac_password").clear()
        driver.find_element_by_id("__ac_password").send_keys("vindula")
        driver.find_element_by_name("submit").click()
	print '-'*80
	print 'Excluindo Portlet localizador'
	print '-'*80	
        driver.find_element_by_css_selector("#portletsLeft > div.managePortletsLink > a[title=\"Exibir a tela de gerenciamento dos portlets\"]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'×')])[3]").click()
        driver.find_element_by_css_selector("#portletmanager-plone-rightcolumn > div.portletAssignments > form > div.formControls > input.context").click()
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
