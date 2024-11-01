from time import sleep


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


from utils.convert_format_date_to_datebr import convert_format_date_to_datebr


#Obs: 
# Para não dar erro na automação, busque por um item no site
# que aparece somente existe quando a tela estiver carregada.

class Automation:
    def __init__(self, driver):
        self.driver = driver
    def insert_items(self, items):
        try:
            sleep(1)
            todos_items_mes_button = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[1]/details[1]/ul/li[1]/a')
            todos_items_mes_button.click()
            
            sleep(2)
            adicionar_button = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/header/header/button')
            adicionar_button.click()
            
            sleep(1)
            data_insercao_input = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[1]/div/input')
            
            data_insercao_value = convert_format_date_to_datebr(items[0])
            
            data_insercao_input.send_keys(data_insercao_value)

            data_insercao_input.send_keys(Keys.TAB) 
            data_insercao_input.send_keys("15:30")
        
            sleep(1)
            elemento_select_find = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[2]/label/select')
            
            elemento_select = Select(elemento_select_find)
            elemento_select.select_by_visible_text(items[1])
            sleep(2)
            subelemento_select_find = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[3]/div/select')
            sleep(2)
            subelemento_select = Select(subelemento_select_find)
            subelemento_select.select_by_visible_text(items[2])
            sleep(2)    
            valor_input = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[8]/div/input')
            valor_input.send_keys(items[7])
            
            sleep(2)
            entrada_saida_input = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[2]/div[1]/div/input')
            entrada_saida_input.click()
            
            descricao_items = items[9]
            observacao_input = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[3]/div/div/input')
            observacao_input.send_keys(f"{descricao_items} by bot")
            
            salvar_button = self.driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[4]/button')
            salvar_button.click()
            sleep(3)
            
        except WebDriverException as e:
            print(f"Ocorreu um erro: {e}")
            self.driver.quit()

        
    
    
