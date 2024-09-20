# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as BraveService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# # Set the path to the Brave browser executable
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with the actual path to your Brave browser executable

# options = Options()
# options.binary_location = brave_path

# service = BraveService(ChromeDriverManager().install())

# browser = webdriver.Chrome(service=service, options=options)

# # Open the Instagram login page
# browser.get("https://www.instagram.com/")

# try:
#     # Wait until the username input field is visible
#     user_input = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
#     )
#     # Wait until the password input field is visible
#     password_input = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
#     )
#     # Wait until the login button is clickable
#     login_btn = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]'))
#     )
#     browser.implicitly_wait(10)
#     user_input.send_keys("joao")
#     browser.implicitly_wait(10)
#     password_input.send_keys("teste")
#     browser.implicitly_wait(10)
#     login_btn.click()

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # Close the browser
#     browser.quit()

from automation import Automation
import csv

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
source_excel_file_path = os.path.join(base_dir, 'files', 'task.xlsx')
success_excel_file_path = os.path.join(base_dir, 'files', 'read', 'task.xlsx')
error_excel_file_path = os.path.join(base_dir, 'files', 'errors', 'task.xlsx')

from utils.move_to_file import move_to_file
from utils.convert_excel_to_csv import convert_excel_to_csv

if __name__ == '__main__':
    try:
        automation = Automation()
        
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
    
