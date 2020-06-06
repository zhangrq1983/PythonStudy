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

temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]  # 去重后转换为列表['EMS', 'Traffic', 'Fire']
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))

df.set_index("timeStamp", inplace=True)

print(df.head(10))

plt.figure(figsize=(20, 8), dpi=80)

for group_name, group_data in df.groupby(by="cate"):

    count_by_month = group_data.resample("M").count()["title"]

    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()
