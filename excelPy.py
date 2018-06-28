import openpyxl
import crawling

def getname_from_excels(filename, sheetnum):
    retName = list()
    wb = openpyxl.load_workbook(filename)
    wsList = wb.get_sheet_names()
    ws = wb[wsList[sheetnum]]
    for i in ws.iter_rows(min_row = 2, max_col = 2):
        name = i[1].value
        retName.append(name)
    return retName

def write_to_excel(filename, sheetnum, datalist):
    wb = openpyxl.load_workbook(filename)
    wsList = wb.get_sheet_names()
    ws = wb[wsList[sheetnum]]
    for row in datalist:
        ws.append(row)
    wb.save(filename)

write_to_excel('KBO_타자.xlsx', 0, crawling.get_datalist('a'))
