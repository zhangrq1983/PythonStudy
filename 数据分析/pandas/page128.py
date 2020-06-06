import pandas as pd

print("*" * 25 + "数据合并操作" + "*" * 25)
# merge按行索引操作，join按列索引操作

import numpy as np

df1 = pd.DataFrame(np.ones((2, 4)), index=["A", "B"], columns=list("abcd"))
df2 = pd.DataFrame(np.zeros((3, 3)), index=["A", "B", "C"], columns=list("xyz"))

print(df1)

print(df2)
print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df1.join(df2)")
print(df1.join(df2))

print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df2.join(df1)")
print(df2.join(df1))

df3 = pd.DataFrame(np.zeros((3, 3)), columns=list("fax"))
print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df1.merge(df3, on=\"a\")# 默认并集所以为空")
print(df1.merge(df3, on="a"))  # 默认并集所以为空

print("*" * 25 + "数据分组聚合" + "*" * 25)
df3.loc[1, "a"] = 1
print("df1.merge(df3, on=\"a\")")
print(df1.merge(df3, on="a"))

df3 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=list("fax"))
print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df1.merge(df3, on=\"a\")")
print(df1.merge(df3, on="a"))

print("*" * 25 + "数据分组聚合" + "*" * 25)
df1.loc["A", "a"] = 100
print("df1.merge(df3, on=\"a\")")
print(df1.merge(df3, on="a"))

print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df1.merge(df3, on=\"a\", how=\"outer\") # 外连接，NaN补全")
print(df1.merge(df3, on="a", how="outer"))

print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df1.merge(df3, on=\"a\", how=\"left\")# 左链接，以df1为准")
print(df1.merge(df3, on="a", how="left"))  # 左链接，以df1为准

print("*" * 25 + "数据分组聚合" + "*" * 25)
print("df1.merge(df3, on=\"a\", how=\"right\")# 右连接，以df3为准")
print(df1.merge(df3, on="a", how="right"))  # 右连接，以df3为准

print("*" * 25 + "数据分组聚合" + "*" * 25)


