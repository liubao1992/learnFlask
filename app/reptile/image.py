import pandas as pd
print(pd.__version__ ) # 查看版本

data = pd.read_excel(r'D:\python\learnFlask\file\user.xls', sheet_name = 1)

data.head()
print(data.head())