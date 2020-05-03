
class A:
    def __init__(self):
        self.name = 'A类'

    def __del__(self):
        print('A()对象被删除了~~~', self)

a = A()
print(a.name)

# b = a

# a = None
# b = None
# del a
# del b

input('hui che jian tuichu....')

print(a.name)


# # 就像我们生活中会产生垃圾一样，程序在运行过程当中也会产生垃圾
# # 程序运行过程中产生的垃圾会影响到程序的运行的运行性能，所以这些垃圾必须被及时清理
# # 没用的东西就是垃圾
# # 在程序中没有被引用的对象就是垃圾，这种垃圾对象过多以后会影响到程序的运行的性能
# #   所以我们必须进行及时的垃圾回收，所谓的垃圾回收就是讲垃圾对象从内存中删除
# # 在Python中有自动的垃圾回收机制，它会自动将这些没有被引用的对象删除，
# #   所以我们不用手动处理垃圾回收
#
# class A:
#     def __init__(self):
#         self.name = 'A类'
#
#     # del是一个特殊方法，它会在对象被垃圾回收前调用
#     def __del__(self):
#         print('A()对象被删除了~~~',self)
#
# a = A()
# b = a # 又使用一个变量b，来引用a对应的对象
#
# print(a.name)
#
# # a = None # 将a设置为了None，此时没有任何的变量对A()对象进行引用，它就是变成了垃圾
# # b = None
# # del a
# # del b
# input('回车键退出...')
