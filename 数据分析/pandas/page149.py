import pandas as pd
from matplotlib import pyplot as plt

# 打开文件
file_path = 'BeijingPM20100101_20151231.csv'

df = pd.read_csv(file_path)

period = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")
df["datetime"] = period

# print(df.head(10))

# 把datetime设置为索引
df.set_index("datetime", inplace=True)

df = df.resample('7D').mean()

# print(df.shape)

print(df["PM_Dongsi"].tail(20))
print('*'*100)
print(df["PM_US_Post"].tail(20))

data = df["PM_US_Post"]
data_china = df["PM_Dongsi"]

print(df)

print(data)

_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_china = [i.strftime("%Y%m%d") for i in data_china.index]

print(len(_x),len(_x_china))

_y = data.values
_y_china = data_china.values

plt.figure(figsize=(13, 9), dpi=80)

plt.plot(range(len(_x)), _y, label="US_POST")
plt.plot(range(len(_x)), _y_china, label="CN_POST")

plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)

plt.legend(loc="best")

plt.show()


