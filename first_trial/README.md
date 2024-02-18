***
# First Trial
*** 

# 1. Text (No Calc)

In this folder, I attempt to write text from one Excel file into another already existing Excel file. There are no calculations.

## Taking from one file into another (using mock Excel files)

### Mock1: Student Names

The source Excel file (`mock1_StudentNames.xlsx`) contains the following data:

| Name       | Surname |
|------------|---------|
| Masixole   | Boya    |
| Jessica    | Mahasi  |
| Andrew     | Garfield|

### Mock2: Student Ages

The destination Excel file (`mock2_StudentAges.xlsx`) initially contains the following data:

| Age |
|-----|
| 21  |
| 25  |
| 28  |

## Process Overview

1. Load the source workbook (`mock1_StudentNames.xlsx`).
2. Load the destination workbook (`mock2_StudentAges.xlsx`).
3. Extract ages from the destination sheet in the destination workbook.
4. Update the age column in the source sheet in the source workbook.
5. Save the changes to the source workbook.

### Mock1 Updated: Student Names

The source Excel file (`mock1_StudentNames_updated.xlsx`) after the process contains the following data:

| Name       | Surname | Age |
|------------|---------|-----|
| Masixole   | Boya    | 21  |
| Jessica    | Mahasi  | 25  |
| Andrew     | Garfield| 28  |
