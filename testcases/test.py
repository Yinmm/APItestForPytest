# import openpyxl as op
# wb = op.load_workbook(r"C:\Users\Administrator\Desktop\PetDoc\Config\Excel\LogicConfig\lua_GlobalConfig.xlsx")
# active_sheet = wb.active
# dict = {}
# row_num = active_sheet.max_row
# for row in range(1,row_num+1):
#     key = active_sheet.cell(row, 1).value
#     value = active_sheet.cell(row, 5).value
#     if type(value) is str:
#         value = value.strip(',')
#     dict[key]=value
#     print(value)
# wb.close()

hunger=1
mood =1
clean = 1


if hunger == 0 and mood == 0 and clean == 0:
    print("都是0")
elif (hunger == 0 and mood == 0) or (hunger == 0 and clean == 0) or (mood == 0 and clean == 0):
    print("其中两个是0")
elif hunger == 0 or mood == 0 or clean == 0:
    print("有一个是0")
elif hunger != 0 and mood != 0 and clean != 0:
    print("都不是0")
else:
    print("出错")