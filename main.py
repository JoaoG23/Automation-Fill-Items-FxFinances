import csv
import os
from dotenv import load_dotenv
load_dotenv()

from automation import Automation

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

base_dir = os.path.dirname(os.path.abspath(__file__))
source_excel_file_path = os.path.join(base_dir, 'files', 'task.xlsx')
success_excel_file_path = os.path.join(base_dir, 'files', 'read', 'task.xlsx')
error_excel_file_path = os.path.join(base_dir, 'files', 'errors', 'task.xlsx')

from utils.move_to_file import move_to_file
from utils.convert_excel_to_csv import convert_excel_to_csv

service = Service(ChromeDriverManager().install())

if __name__ == '__main__':
    try:
        
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.delete_all_cookies()
        
        driver.get("http://localhost:81")
        sleep(4)
            
        login_input = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/main/div/form/div[1]/input')
        sleep(1)
        login_input.send_keys(username)
        
        sleep(2)
        password_input = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/main/div/form/div[2]/input')
        password_input.send_keys(password)
        
        sleep(2)
        submit_button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/main/div/form/button')
        submit_button.click()
        
        sleep(2)
        fluxo_caixa_button = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div[1]/details[1]/summary')
        fluxo_caixa_button.click()
        
        automation = Automation(driver)
        
        
        convert_excel_to_csv()
        
        with open('output.csv', 'r') as file:
            file_read = csv.reader(file)
            list_file_read = list(file_read)
            
            ## Remove header
            list_file_read.pop(0)
            
            for i, line in enumerate(list_file_read):
                automation.insert_items(line)
        # Move to file for dir (read)
        move_to_file(source_excel_file_path, success_excel_file_path)
        
    
    except Exception as e:
        # Move file with dir(erros)
        move_to_file(source_excel_file_path, error_excel_file_path)
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    
