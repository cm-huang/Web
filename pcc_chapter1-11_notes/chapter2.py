# Author: hcm Time: 2020/11/3

# chapter2 变量和简单数据类型


# 2.2 变量

# message = "Hello Python world!"
# print(message)                                    变量是可以赋给值的标签
# message = "Hello Python Crash Course world!"      python始终纪录变量的最新值
# print(message)

# 2.3 字符串

# name = "ade Love"
# print(name.title())                               name.title()中"."表示让python对变量name执行方法title()指定的操作
# print(name.upper())                               每个方法后面都跟着一对括号，因为方法通常需要额外的信息来完成其工作
# print(name.lower())                               函数title()不需要额外信息，所以括号为空。 方法是python可对数据执行的操作

# first_name = "ade"
# last_name = "Love"
# full_name = first_name + " " + last_name          python使用加号"+"来合并字符串；""代表0*0的字符串，" "代表1*1的字符串空格
# print(full_name)                                  python执行命令会自动跳过符号与变量/函数间的空格
# print("Hello, " +   full_name.title() + "!")
# a = 23
# full_name = f"{a}  {last_name}123456"             在字符串中使用变量——f字符串，将花括号内的变量替换为其值
# print(full_name)

# print("\tPython\tWorld")
# print("\nPython\nWorld")                          制表符(Tab)"\t",换行符"\n"
# print("\t\nPython\n\tWorld")

# method = " Python "
# print(method)
# print(method.rstrip())
# print(method.lstrip())                            删除空白,空白泛指任何非打印字符,如空格、制表符和换行符
# print(method.strip())
# method = method.strip()
# print(method)

# 2.4 数字

# print(2.1 + 3 ** 3)                               浮点数即小数
# print("Happy " + str(22) + "nd Birthday!")        str()函数，将非字符串值表示为字符串

# print(4/2)                                        任意两个数相除，结果总是浮点数

# universe_age = 14_000_000_000                     Python中，书写很大的数时可使用下划线将数字分组，1000、1_000、10_00没什么区别
# print(universe_age)

# x, y, z = 1, 2, 3
# name = "hcm"                                      同时给多个变量赋值方法
# print(x, y, z, name)

# MAX = 1000                                        Python中无常量类型，程序员规范全大写为常量
