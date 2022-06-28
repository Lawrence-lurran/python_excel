import re
import pandas as pd
import numpy as np
import xlwt

data=pd.read_excel("biaoge.xlsx")
data_array=np.array(data)
length=len(data_array)
res=[]
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('病理')  # 将工作表worksheet命名为‘Python’
for i in range(length):
    m = re.findall('[A-Z][0-9]..[0-9]*',data_array[i][0])
    nums=list(set(m))
    len1=len(nums)
    res.append(len1)
    worksheet.write(i,0,len1)  # write(行,列,写入的内容)
print(res)
print(len(res))
 # 导入xlwt模块
# 1 新建工作簿
# 2 新建工作表并重命名
# 3 写入内容
# 4 保存
workbook.save('工作簿.xlsx')