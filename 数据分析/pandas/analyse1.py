import numpy as np
import pandas as pd

# 打开文件
FileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(FileNameStr, encoding='utf-8')

# 禁止省略列信息
pd.set_option('display.max_columns', None)
# 打印信息
print("--------------head--------------")
print(df.head())
print("------------describe------------")
print(df.describe())
print("--------------info--------------")
print(df.info())
print("================================")