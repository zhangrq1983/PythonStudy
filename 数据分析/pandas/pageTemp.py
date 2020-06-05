import pandas as pd
import numpy as np

file_path = "911.csv"
df = pd.read_csv(file_path)
temp_list = df["title"].str.split(": ").tolist()
cate_list = list(set([i[0] for i in temp_list]))  # 去重后转换为列表['EMS', 'Traffic', 'Fire']
# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1
sum_ret = zeros_df.sum(axis=0)
print(sum_ret)
