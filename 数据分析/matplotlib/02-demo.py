from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simhei.ttf", size=14)

# font = {'family': 'FangSong',
#         'weight': 'bold',
#         'size': '10'}
#
# matplotlib.rc('font', **font)  # pass in the font dict as kwargs

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(13, 10), dpi=80)

plt.plot(x, y)

# plt.xticks(x)

# _x = x[::10]
_x = x
print(_x)
_labels = ["十点{}分".format(i) for i in range(60)]
_labels += ["十一点{}分".format(i) for i in range(60)]

print(_labels)

# plt.xticks(_x[::3], _labels[::3], rotation=45)
plt.xticks(_x[::3], _labels[::3], rotation=45, fontProperties=font)

# plt.savefig('02-demo.png')

plt.xlabel("时间", fontproperties=font)
plt.ylabel("温度", fontproperties=font)
plt.title("10点到12点的温度变化趋势", fontproperties=font)

plt.show()
