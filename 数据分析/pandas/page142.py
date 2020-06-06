import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

file_path = "911.csv"

df = pd.read_csv(file_path)

temp_list = df["title"].str.split(": ").tolist()

cate_list = list(set([i[0] for i in temp_list]))  # 去重后转换为列表['EMS', 'Traffic', 'Fire']

print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)

for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1

# for i in range(df.shape[0]):
#     zeros_df.loc[i, temp_list[i][0]] = 1
#
print(zeros_df.head(10))

sum_ret = zeros_df.sum(axis=0)
print(sum_ret)
