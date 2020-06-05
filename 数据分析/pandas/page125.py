import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)


file_path = "IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)  # 读取csv数据
# 1. 统计Genre字段
temp_list = df["Genre"].str.split(",").tolist()

print(df["Genre"].head(3))

# [[],[],[]] 嵌套列表 [['Action', 'Adventure', 'Sci-Fi'], ['Adventure', 'Mystery', 'Sci-Fi']...]
genre_list = list(set([j for i in temp_list for j in i]))

# 类别过滤 如柱状图下边的单词 举个例子：若sb 这个单词出现过100次，只统计一次
# 2. 构造全为0的二维数组

zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)

# 3. 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1

# zeros_df.to_csv("zeros_df.csv")

# 4. 统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)

# 5. 将电影的数量和升序排序
genre_count = genre_count.sort_values()

# 6. 画图
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(20, 8), dpi=80)
# plt.bar(range(len(_x)), _y, width=0.4, color="orange")
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
