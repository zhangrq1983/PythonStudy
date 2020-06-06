import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

file_path = "911.csv"

df = pd.read_csv(file_path)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])

df.set_index("timeStamp", inplace=True)

count_by_month = df.resample("M").count()["title"]

print(count_by_month)

# 6. 画图
_x = count_by_month.index
_y = count_by_month.values

# for i in _x:
#     print(dir(i))
#     break

print(_x)
_x = [i.strftime("%Y%m%d") for i in _x]

print(_x)
print(_y)

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x, rotation=45)

plt.show()
