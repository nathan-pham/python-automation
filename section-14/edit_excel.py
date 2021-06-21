import openpyxl as xl

workbook = xl.Workbook()
sheet_name = workbook.sheetnames[0]
sheet = workbook[sheet_name]

sheet['A1'].value = "Hello"
sheet['A2'].value = "World"

workbook.save("files/section-14/edit_excel.xlsx")