import csv
import os
from dotenv import load_dotenv

from automation import Automation

load_dotenv()

user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

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
    
