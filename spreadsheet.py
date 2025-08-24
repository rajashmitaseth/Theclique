import openpyxl

state = 'Bihar'
district = 'Buxar'
location = 'Chausa' 

def findMatch(state,district,location):
    path = "book1.xlsx"
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for i in range(1, 16976):
        reqLoc=[]
        s = sheet.cell(row=i, column=2)
        d = sheet.cell(row=i, column=3)
        l = sheet.cell(row=i, column=4)
        if (s.value == state) and (d.value == district) and (l.value == location):
            for j in range(1, 24):
                cell = sheet.cell(row=i,column=j)
                reqLoc.append(cell)
                print(cell.value)
    return reqLoc

findMatch(state,district,location)