
my_list = []
print(my_list, type(my_list))

my_list = [10]

my_list = [10, 20, 30, 40, 50]

my_list = [10, '20', True, None, 1.2, print, [1, 2, 3]]

my_list = [10, 20, 30, 40, 50]

print(my_list)

print(my_list[0], type(my_list[0]))

# print(my_list[5], type(my_list[5]))

print(len(my_list))

# # 创建列表，通过[]来创建列表
# my_list = [] # 创建了一个空列表
# # print(my_list , type(my_list))
#
# # 列表存储的数据，我们称为元素
# # 一个列表中可以存储多个元素，也可以在创建列表时，来指定列表中的元素
# my_list = [10] # 创建一个只包含一个元素的列表
#
# # 当向列表中添加多个元素时，多个元素之间使用,隔开
# my_list = [10,20,30,40,50] # 创建了一个保护有5个元素的列表
#
# # 列表中可以保存任意的对象
# my_list = [10,'hello',True,None,[1,2,3],print]
#
# # 列表中的对象都会按照插入的顺序存储到列表中，
# #   第一个插入的对象保存到第一个位置，第二个保存到第二个位置
# # 我们可以通过索引（index）来获取列表中的元素
# #   索引是元素在列表中的位置，列表中的每一个元素都有一个索引
# #   索引是从0开始的整数，列表第一个位置索引为0，第二个位置索引为1，第三个位置索引为2，以此类推
# my_list = [10,20,30,40,50]
#
# # 通过索引获取列表中的元素
# # 语法：my_list[索引] my_list[0]
# # print(my_list[4])
# # 如果使用的索引超过了最大的范围，会抛出异常
# # print(my_list[5]) IndexError: list index out of range
#
# # 获取列表的长度，列表中元素的个数
# # len()函数，通过该函数可以获取列表的长度
# # 获取到的长度的值，是列表的最大索引 + 1
# print(len(my_list)) # 5