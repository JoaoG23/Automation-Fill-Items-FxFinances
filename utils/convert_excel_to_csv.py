import openpyxl
import csv
import os

current_dir = os.getcwd()
excel_file_path = os.path.join(current_dir, 'files', 'task.xlsx')

import openpyxl
import csv
import os

# Defina o caminho do arquivo Excel
current_dir = os.getcwd()
excel_file_path = os.path.join(current_dir, 'files', 'task.xlsx')

def convert_excel_to_csv():
    try:
        # Carrega a planilha Excel
        wb = openpyxl.load_workbook(excel_file_path)
        sheet = wb.active  # Obtém a planilha ativa

        csv_file_path = 'output.csv'

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            for row in sheet.iter_rows(values_only=True):
                if any(row):  # Só escreve a linha se houver algum valor
                    writer.writerow(row)

        print(f"Arquivo Excel {excel_file_path} foi convertido para CSV {csv_file_path}")

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")




        
