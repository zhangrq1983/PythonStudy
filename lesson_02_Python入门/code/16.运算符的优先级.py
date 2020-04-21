
a = 40
b = 50
c = 30

max = a if a > b else b
max = max if max > c else c

max = a if (a > b and a > c) else (b if b > c else c)

print(max)

a = 1 + 2 * 3

a = 1 or 2 and 3

a = (1 or 2) and 3

a = 1 < 2 < 3

a = 10 < 20 < 15

print(a)

a = 40
b = 50
c = 30

# 通过条件运算符获取三个值中的最大值
# max = a if a > b else b
# max = max if max > c else c

max = a if (a > b and a > c) else (b if b > c else c) # 不推荐这么使用
# max = a if (b < a > c) else (b if b > c else c)

# print(max)

# 运算符的优先级
# 和数学中一样，在Python运算也有优先级，比如先乘除 后加减
# 运算符的优先级可以根据优先级的表格来查询，
#   在表格中位置越靠下的运算符优先级越高，优先级越高的越优先计算
#   如果优先级一样则自左向右计算
#  关于优先级的表格，你知道有这么一个东西就够了，千万不要去记
#  在开发中如果遇到优先级不清楚的,则可以通过小括号来改变运算顺序
a = 1 + 2 * 3

# 一样 and高 or高
# 如果or的优先级高，或者两个运算符的优先级一样高
#   则需要先进行或运算，则运算结果是3
# 如果and的优先级高，则应该先计算与运算
#   则运算结果是1
a = 1 or 2 and 3

# print(a)

# 逻辑运算符（补充）
# 逻辑运算符可以连着使用
result = 1 < 2 < 3 # 相当于 1 < 2 and 2 < 3
result = 10 < 20 > 15

print(result)