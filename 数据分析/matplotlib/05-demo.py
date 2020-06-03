from matplotlib import pyplot as plt

from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simhei.ttf", size=12)

x = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5", "最后的骑士", "摔跤吧!\n爸爸", "加勒比海盗5:\n死无对证", "金刚:\n骷髅岛",
     "极限特工:\n终极回归", "生化危机6:\n终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3", "蜘蛛侠", "孙悟空",
     "银河护卫队", "情圣", "新木乃衣"]

y = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23, 5.23]

plt.figure(figsize=(15, 8), dpi=80)

plt.bar(range(len(x)), y, width=0.5)

plt.xticks(range(len(x)), x, FontProperties=font, rotation=45)

plt.xlabel("时间", FontProperties=font)
plt.ylabel("温度", FontProperties=font)
plt.title('十月十一月气温情况', FontProperties=font)

plt.show()
