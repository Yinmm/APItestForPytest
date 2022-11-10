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
