import xlwings as xw
from prices import *

wb = xw.Book('info.xlsx')
ws1 = wb.sheets['Sheet1']

rownum = ws1.range('A1').current_region.last_cell.row
print("Rows total: " + str(rownum))

i = 0
while i <= rownum:
    print('Current row: ' + str(i), end='\r')
    try:
        id_tmp = str(ws1.range('C' + str(i)).value)[:-2]

        if ws1.range('D'+str(i)).value == None:
            ws1.range('D'+str(i)).value = gamePrice(id_tmp)

        if ws1.range('E'+str(i)).value == None and ws1.range('D'+str(i)).value != None:
            badge_tmp = badgePrice(id_tmp)
            if badge_tmp != 0:
                ws1.range('E'+str(i)).value = badge_tmp
            else:
                continue
    except:
        pass
    i += 1
print('All done!')
