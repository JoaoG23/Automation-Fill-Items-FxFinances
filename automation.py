from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from utils.convert_format_date_to_datebr import convert_format_date_to_datebr


service = Service(ChromeDriverManager().install())

#Obs: 
# Para não dar erro na automação, busque por um item no site
# que aparece somente existe quando a tela estiver carregada.

class Automation:
        
    def insert_items(self, items):
        driver = webdriver.Chrome(service=service)
        try:
            driver.get("http://localhost:81")
            sleep(2)
            
            login = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/main/div/form/div[1]/input')
            login.send_keys("admin")
            
            password = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/main/div/form/div[2]/input')
            password.send_keys("admin")
       
            submit = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/main/div/form/button')
            submit.click()
            sleep(3)
            
            ## Cadastro de tarefas
            fluxo_caixa_button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[1]/details[1]/summary')
            fluxo_caixa_button.click()
            
            sleep(1)
            todos_items_mes_button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[1]/details[1]/ul/li[1]/a')
            todos_items_mes_button.click()
            
            sleep(2)
            adicionar_button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/header/header/button')
            adicionar_button.click()
            
            sleep(1)
            data_insercao_input = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[1]/div/input')
            
            data_insercao_value = convert_format_date_to_datebr(items[0])
            
            data_insercao_input.send_keys(data_insercao_value)

            data_insercao_input.send_keys(Keys.TAB)  # Tab to the time input, or send the T directly
            data_insercao_input.send_keys("15:30")
        
            sleep(1)
            elemento_select_find = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[2]/label/select')
            
            elemento_select = Select(elemento_select_find)
            elemento_select.select_by_visible_text(items[1])
            sleep(1)
            subelemento_select_find = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[3]/div/select')
            
            subelemento_select = Select(subelemento_select_find)
            subelemento_select.select_by_visible_text(items[2])
                
            valor_input = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[1]/main/div[8]/div/input')
            valor_input.send_keys(items[7])
            
            
            entrada_saida_input = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[2]/div[1]/div/input')
            entrada_saida_input.click()
            
            observacao_input = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[3]/div/div/input')
            observacao_input.send_keys("Criado por automacao python")
            
            salvar_button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[4]/main/form/section/section[4]/button')
            salvar_button.click()
            
                    
            sleep(2)
        except WebDriverException as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            driver.quit()

        
    
    
