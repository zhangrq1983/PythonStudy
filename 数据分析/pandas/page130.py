import pandas as pd

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

# ?统计美国和中国的星巴克数量groupby

groups = df.groupby(by="Country")

print(groups)

for i in groups:
    print(i[0])
    print(type(i[1]))
    break
country_count = groups["Brand"].count()
print(country_count["US"])
print(country_count["CN"])

# 统计中国每个省份数量
china_data = df[df["Country"] == "CN"]
groups = china_data.groupby(by="State/Province").count()["Brand"]
print(groups)

# dataframegroupby有很多方法
# count（分组中非NA值的数量）
# sum（非NA的和）
# mean（非NA平均数）
# median(非NA的算术中位数)
# std、var无便（分母n-1）标准差和方差
# min、max（非NA最大和最小）

# 按多个条件进行分组
groups = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
type(groups)
