
# i = 0
# while i < 5:
#     j = 0
#     while j < 5:
#         print('* ', end='')
#         j += 1
#     i += 1
#     print()

i = 0
while i < 5:
    i += 1
    print('* ' * i, end='')
    print()

i = 0
while i < 5:
    j = 0
    while j < i + 1:
        print('* ', end='')
        j += 1
    print()
    i += 1



# 在控制台中打印如下图形
# *****
# *****
# *****
# *****
# *****
# 

# 创建一个循环来控制图形的高度
# 循环嵌套时，外层循环没执行一次，内存循环就要执行一圈
# i = 0
# while i < 5:
#     # 创建一个内层循环来控制图形的宽度
#     j = 0
#     while j < 5:
#         print("* ",end='')
#         j += 1
#     print()
#     i += 1

#
# *     j<1   i=0
# **    j<2   i=1   
# ***   j<3   i=2
# ****  j<4   i=3
# ***** j<5   i=4
# 
# *****
# ****
# ***
# **
# *
# i = 0
# while i < 5:
#     j = 0
#     while j < i + 1:
#         print("* ",end='')
#         j += 1
#     print()
#     i += 1

