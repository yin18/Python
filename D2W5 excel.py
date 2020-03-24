import xlsxwriter

data9 = xlsxwriter.Workbook("data9.xlsx")

worksheet = data9.add_worksheet("data9.xlsx")

#rows and columns are zero indexed
#first cell in worksheet A1 is (0,0), B1 is (0,1)
worksheet.write("A1", "data 9")
worksheet.write("A2", "Isabella")
worksheet.write("A3", "Shahrukh")
worksheet.write("A4", "Zoe")

row = 0
column = 1

info = ["Name", "Sassy", "CJ"]
for name in info:
    worksheet.write(row, column, name)
    row +=1
data9.close()

import openpyxl
path =
data9 = openpyxl.load_workbook()

