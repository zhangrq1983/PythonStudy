import numpy as np
import pandas as pd

# 打开文件，仅读取第7至第10列
FileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(FileNameStr, encoding='utf-8', usecols=[1, 2, 6, 7, 8, 9])

# 新建平均值列，并将平均值写入
# 其中，iloc[:, 2:6]指第3到第6列，mean(axis=1)为求行平均值
df['PM_ave'] = df.iloc[:, 2:6].mean(axis=1)
# 保存到文件，其中以'year'和'month'分组，计算'PM_ave'列的平均值。
df.groupby(['year', 'month'])['PM_ave'].mean().to_csv("solution2.csv")
# 为方便，再打印一份
print(df.groupby(['year', 'month'])['PM_ave'].mean())
