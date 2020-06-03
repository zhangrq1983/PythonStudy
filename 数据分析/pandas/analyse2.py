import numpy as np
import pandas as pd

# 打开文件，仅读取第7至第10列
FileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(FileNameStr, encoding='utf-8', usecols=[6, 7, 8, 9])

# 打印信息

# 总行数
print("Total of rows: {}".format(len(df.index)))

# 显示某列缺失值个数
# print("The number of missing data in PM_Dongsi: {}".format(len(df.index) - len(df['PM_Dongsi'].dropna())))
# 为了书写简便，使用循环，遍历所有列，获得每列缺失值个数
for col in df:
    #dropna()会去除缺省值的数据，遂得到每列的缺失数据数
    print("The number of missing data in {}: {}".format(col, len(df.index) - len(df[col].dropna())))

# 获取所有列均为缺失值的行的个数，how='all'是限定所有列均为缺省值
print("The number of missing data in BOTH: ", len(df.index) - len(df.dropna(how='all')))