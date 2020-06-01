from matplotlib import pyplot as plt
import random

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.plot(x, y)

# plt.xticks(x)

_x = x[::10]
print(_x)
plt.xticks(_x)

plt.savefig('02-demo.png')

plt.show()
