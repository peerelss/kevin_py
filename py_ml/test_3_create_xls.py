import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8') #print(workbook) %结果%<xlwt.Workbook.Workbook object at 0x005F4630>
# 创建一个worksheet
worksheet = workbook.add_sheet('小马过河')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1,0, label = '第二行第一列')

# 保存
workbook.save('学习笔记.xls')