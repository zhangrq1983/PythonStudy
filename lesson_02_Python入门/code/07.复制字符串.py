
name = 'sunwukong'

print('huanying ' + name + ' guanglin!')

print('huanying ', name,' guanglin!')

print('huanying %s guanglin!' %name)

print(f'huanying {name} guanglin!')

a = 'abc'

a = a * 20

print(a)


# 创建一个变量来保存你的名字
name = '孙悟空'

# 使用四种方式来输出，欢迎 xxx 光临
# 拼串
print('欢迎 '+name+' 光临！')
# 多个参数
print('欢迎',name,'光临！')
# 占位符
print('欢迎 %s 光临！'%name)
# 格式化字符串
print(f'欢迎 {name} 光临！')

# 字符串的复制（将字符串和数字相乘）
a = 'abc'
# * 在语言中表示乘法
# 如果将字符串和数字相乘，则解释器会将字符串重复指定的次数并返回
a = a * 20

print(a)