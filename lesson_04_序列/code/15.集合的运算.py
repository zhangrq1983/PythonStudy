
a = {1, 2, 3, 4, 5}
a2 = {3, 4, 5, 6, 7}

print(a, a2)

result = a & a2

result = a | a2

result = a - a2







print('result =',result)






# # 在对集合做运算时，不会影响原来的集合，而是返回一个运算结果
# # 创建两个集合
# s = {1,2,3,4,5}
# s2 = {3,4,5,6,7}
#
# # & 交集运算
# result = s & s2 # {3, 4, 5}
#
# # | 并集运算
# result = s | s2 # {1,2,3,4,5,6,7}
#
# # - 差集
# result = s - s2 # {1, 2}
#
# # ^ 异或集 获取只在一个集合中出现的元素
# result = s ^ s2 # {1, 2, 6, 7}
#
# # <= 检查一个集合是否是另一个集合的子集
# # 如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合是a集合超集
# a = {1,2,3}
# b = {1,2,3,4,5}
#
# result = a <= b # True
# result = {1,2,3} <= {1,2,3} # True
# result = {1,2,3,4,5} <= {1,2,3} # False
#
# # < 检查一个集合是否是另一个集合的真子集
# # 如果超集b中含有子集a中所有元素，并且b中还有a中没有的元素，则b就是a的真超集，a是b的真子集
# result = {1,2,3} < {1,2,3} # False
# result = {1,2,3} < {1,2,3,4,5} # True
#
# # >= 检查一个集合是否是另一个的超集
# # > 检查一个集合是否是另一个的真超集
# print('result =',result)