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



# 2. Text_2_(No_Calculations)


In this folder, I attempt to write text from one Excel file into another already existing Excel file. There are no calculations.

## Taking from one file into another (using mock Excel files)

### Mock1: Sales

The source Excel file (`mock2_SourceData.xlsx`) contains the following data:

| Customer          | Amount | Price |
|-------------------|--------|-------|
| ABC Corporation   | 50     | 500   |
| XYZ Ltd           | 30     | 300   |
| Acme Industries   | 20     | 200   |
| Global Solutions  | 40     | 400   |

### Mock2: Profit Margin

The destination Excel file (`mock2_DestinationData_Simplified.xlsx`) initially looks like this:

| Customer          | Amount | Price | Total Revenue | Profit Margin |
|-------------------|--------|-------|---------------|----------------|
| ABC Corp          |        |       |               |                |
| XYZ Limited       |        |       |               |                |
| Acme Inc.         |        |       |               |                |
| Global Solutions  |        |       |               |                |

## Process Overview

1. Load the source workbook (`mock2_SourceData.xlsx`).
2. Load the destination workbook (`mock2_DestinationData_Simplified.xlsx`).
3. Extract data from the source sheet in the source workbook.
4. Update the corresponding columns in the destination sheet in the destination workbook.
5. Calculate the `Total Revenue` using the formula: `Amount * Price`.
6. Calculate the `Profit Margin` using the formula: `(Total Revenue - TotalCost) / Total Revenue * 100`.
7. Save the changes to the destination workbook.

### Mock2 Updated: Profit Margin

After the process, the destination Excel file (`mock2_DestinationData_Simplified.xlsx`) will look like this:

| Customer          | Amount | Price | Total Revenue | Profit Margin |
|-------------------|--------|-------|---------------|----------------|
| ABC Corp          | 50     | 500   | 25000         | 40%            |
| XYZ Limited       | 30     | 300   | 9000          | 0%             |
| Acme Inc.         | 20     | 200   | 4000          | -100%          |
| Global Solutions  | 40     | 400   | 16000         | 0%             |


