from matplotlib import pyplot as plt

import matplotlib

font = {'family': 'FangSong',
        'weight': 'bold',
        'size': '10'}

matplotlib.rc('font', **font)  # pass in the font dict as kwargs

y_10 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
        22, 23]

y_11 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]

print(len(y_10))
print(len(y_11))

plt.figure(figsize=(15, 8), dpi=80)

x_10 = range(1, 32)

x_11 = range(50, 81)

plt.scatter(x_10, y_10, label='十月份')
plt.scatter(x_11, y_11, label='十一月份')

plt.legend()

_x = list(x_10) + list(x_11)
_xticks_label = ["十月{}号".format(i) for i in x_10]
_xticks_label += ["十一月{}号".format(i-50) for i in x_11]

plt.xticks(_x[::3], _xticks_label[::3], rotation=45)

plt.xlabel("时间")
plt.ylabel("温度")
plt.title('十月十一月气温情况')

plt.grid()

plt.savefig('04-demo.png')

plt.show()
