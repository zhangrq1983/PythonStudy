from matplotlib import pyplot as plt

from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simhei.ttf", size=12)

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 2, 3, 1, 1, 1, 1, 1, 2, 1, 1, 2, 3, 2, 2]

x_1 = range(11, 31)
x_2 = range(11, 31)

plt.figure(figsize=(13, 9), dpi=80)

plt.plot(x_1, y_1, label='自己', color='r', linewidth=5)
plt.plot(x_2, y_2, label='同桌', linestyle=':')
# plt.legend(prop=font, loc='upper right')
plt.legend(prop=font, loc='lower right')

_x = x_1
_xticks_label = ["{}岁".format(i) for i in _x]

plt.xticks(_x, _xticks_label, rotation=45, fontProperties=font)

plt.xlabel("岁数", fontproperties=font)
plt.ylabel("个数", fontproperties=font)
plt.title("11到31岁的男女朋友数量", fontproperties=font)

plt.grid(alpha=0.3)


plt.show()
