from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

plt.figure(figsize=(25, 15), dpi=80)

plt.plot(x, y)

_x = [i / 2 for i in range(4, 49)]
# plt.xticks(x)
plt.xticks(_x)

plt.yticks(range(min(y), max(y) + 1))

plt.savefig('./01-demo.png')

plt.show()
