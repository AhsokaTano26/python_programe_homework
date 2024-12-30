from openpyxl import load_workbook

workBook = load_workbook("ScoresSheet.xlsx")
workSheet = workBook.worksheets[0]
for idx,row in enumerate(workSheet.rows):
    if idx==0:
        continue 
    row[5].value = row[1].value * 0.3 + row[2].value * 0.1 \
        + row[3].value * 0.2 + row[4].value * 0.4

workBook.save("ScoresSheet2.xlsx")  