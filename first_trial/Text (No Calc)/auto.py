from openpyxl import Workbook, load_workbook
import os

current_path = os.getcwd()

print(f"CURRENT working directory: {current_path}")
# importing the worksheets

wb_student_names = load_workbook('first_trial/Text (No Calc)/mock1_StudentNames.xlsx')
wb_student_ages = load_workbook('first_trial/Text (No Calc)/mock2_StudentAges.xlsx')

print(wb_student_ages.active)