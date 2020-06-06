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
cate_list = [i[0] for i in temp_list] # 去重后转换为列表['EMS', 'Traffic', 'Fire']

cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))

df["cate"] = cate_df

print(df.head(5))

print(df.groupby(by="cate").count()["title"])

