
# num = int(input('qingshuruzhengshu:'))
#
# if num % 2 == 0:
#     print('zhengshu', num)
# elif num % 2 == 1:
#     print('jishu', num)

# year = int(input('qingshurunianfen:'))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('runnian', year)
# else:
#     print('pingnian', year)

# age = float(input('qingshurunianling:'))
#
# like_person_age = 0
# if age > 0:
#     if age <= 2:
#         like_person_age = age * 10.5
#     else:
#         like_person_age = 2 * 10.5
#         like_person_age += (age - 2) * 4
#     print('like_person_age', like_person_age)
# else:
#     print('buhefa')


# score = float(input('qingshuruchengji(0-100):'))
#
# print('=' * 40)
#
# if 100 >= score >= 0:
#     if score == 100:
#         print('100')
#     elif score >= 80:
#         print('80-100')
#     elif score >= 60:
#         print('60-80')
#     else:
#         print('nothing')
# else:
#     print('buhefa')


height = float(input('请输入你的身高(厘米):'))
money = float(input('请输入你的财富(万):'))
face = float(input('请输入你的颜值(平方厘米):'))

if height > 180 and money > 1000 and face > 500:
    print('yi ding jia')
elif height > 180 or money > 1000 or face > 500:
    print('jia ba')
else:
    print('bu ba')


# 练习1：
#     编写一个程序，获取一个用户输入的整数。然后通过程序显示这个数是奇数还是偶数。
# 获取用户输入的整数
# num = int(input('请输入一个任意的整数：'))

# # 显示num是奇数还是偶数
# if num % 2 == 0 :
#     print(num , "是偶数")
# else :
#     print(num , '是奇数')


# 练习2：
#     编写一个程序，检查任意一个年份是否是闰年。
#     如果一个年份可以被4整除不能被100整除，或者可以被400整除，这个年份就是闰年
# year = int(input('请输入一个任意的年份:'))
# # 检查这个年份是否是闰年
# # year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print(year,'是闰年')
# else :
#     print(year,'是平年')

# 练习3：
#     我家的狗5岁了，5岁的狗相当于多大年龄的人呢？
#     其实非常简单，狗的前两年每一年相当于人类的10.5岁，然后每增加一年就增加四岁。
#     那么5岁的狗相等于人类的年龄就应该是10.5+10.5+4+4+4 = 33岁 

#     编写一个程序，获取用户输入的狗的年龄，然后通过程序显示其相当于人类的年龄。
#     如果用户输入负数，请显示一个提示信息

# dog_age = float(input('请输入狗的年龄：'))
# like_person_age = 0
# 检查用户输入的是否是负数
# if dog_age < 0 :
#     print('你的输入不合法！')
# # 如果狗的年龄在两岁以下（包含两岁）
# elif dog_age <= 2 :
#     # 直接将当前的年龄乘以10.5
#     like_person_age = dog_age * 10.5
# # 如果狗的年龄在两岁以上
# else :
#     # 计算前两岁相当于人类的年纪
#     like_person_age = 2 * 10.5
#     # 计算超过两岁的部分相对于人类的年纪，并进行相加
#     like_person_age += ( dog_age - 2 ) * 4

# if dog_age > 0 :
#     print(dog_age,'岁的狗，年纪相当于',like_person_age,'岁的人')
#     

# 在if也可以去嵌套if，代码块是可以嵌套的，每增加一个缩进的级别，代码块就低一级
# 检查用户的输入是否合法
# if dog_age > 0 :
#     # 如果狗的年龄在两岁以下（包含两岁）
#     if dog_age <= 2 :
#         # 直接将当前的年龄乘以10.5
#         like_person_age = dog_age * 10.5
#     # 如果狗的年龄在两岁以上
#     else :
#         # 计算前两岁相当于人类的年纪
#         like_person_age = 2 * 10.5
#         # 计算超过两岁的部分相对于人类的年纪，并进行相加
#         like_person_age += ( dog_age - 2 ) * 4

#     print(dog_age,'岁的狗，年纪相当于',like_person_age,'岁的人')
# else :
#     print('请输入一个合法的年龄！')


# 练习4：
#     从键盘输入小明的期末成绩:
#         当成绩为100时，'奖励一辆BMW'
#         当成绩为[80-99]时，'奖励一台iphone'
#         当成绩为[60-79]时，'奖励一本参考书'
#         其他时，什么奖励也没有

# 获取小明的成绩
# score = float(input('请输入你的期末成绩(0-100)：'))

# # 打印分割线
# print("="*40)

# # 检查用户的输入是否合法
# if 0 <= score <= 100 :
#     # 判断发给的奖励
#     if score == 100 :
#         print('宝马，拿去玩！')
#     elif score >= 80 :
#         print('苹果手机，拿去玩！')
#     elif score >= 60 :
#         print('参考书，拿去玩！')
#     else :
#         print('棍子一根！')
# else :
#     # 用户输入的不合法，弹出一个友好提示
#     print('你输入的内容不合法，拉出去毙了！')


# 练习5：
#     大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
#         高：180cm以上; 富:1000万以上; 帅:500以上;
#         如果这三个条件同时满足，则:'我一定要嫁给他'
#         如果三个条件有为真的情况，则:'嫁吧，比上不足，比下有余。'
#         如果三个条件都不满足，则:'不嫁！'

# 获取用户的三个数据，身高、财富、颜值
# height = float(input('请输入你的身高(厘米):'))
# money = float(input('请输入你的财富(万):'))
# face = float(input('请输入你的颜值(平方厘米):'))
#
# # 判断到底嫁不嫁
# # 如果这三个条件同时满足，则:'我一定要嫁给他'
# if height > 180 and money > 1000 and face > 500 :
#     print('我一定要嫁给他！')
# # 如果三个条件有为真的情况，则:'嫁吧，比上不足，比下有余。'
# elif height > 180 or money > 1000 or face > 500 :
#     print('嫁吧，比上不足，比下有余。')
# # 如果三个条件都不满足，则:'不嫁！'
# else :
#     print('不嫁！')

