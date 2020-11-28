# Author: hcm Time: 2020/11/17

# chapter10 文件和异常


# 10.1 从文件中读取数据

# with  open('F:/DeepLearning/matlab_code/example.txt') as file_object:     # open()函数打开文件，返回一个表示文件的对象，并使用as将其赋给file_object
#     contents = file_object.read()     # 关键字with在不需要访问文件后将其自动关闭，open()返回的文件对象只在with代码块内可用，路径应使用斜杆而不是反斜杠
# print(contents)     # 方法read()读取文件的所有内容，并以 一个字符串 形式赋给变量contents

# filename = 'F:/DeepLearning/matlab_code/example.txt'
# with open(filename) as file_object:
#     for x in file_object:       # 直接使用for循环逐行读取，相当于把文件内容按行看作一个列表
#         print(x)      # 输出的每行之间有两个换行符，一个来自文件，一个来自函数print()

# filename = 'F:/DeepLearning/matlab_code/example.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()     # 使用方法readlines()将文件各行存储在一个列表中
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)      # 读取文本文件时，Python将其中所有的文本都解读为字符串
# print(len(pi_string))

# 10-1
# with open('learning_python.txt') as example:
#     lines = example.readlines()
# print(lines)

# 10-2
# with open('learning_python.txt') as example:
#     for line in example:
#         line = line.replace('Python', 'C')
#         print(line.rstrip())

# 10.1 写入文件

# 10-3
# filename = 'guest.txt'
# contents = input("Input your name:\n")
# with open(filename, 'w') as file_object:      open()函数第二个实参:'r'只读、'w'写入、'a'附加、'r+'读写，其中写入模式会清空原文件内容
#     file_object.write(f"{contents}")      Python只能将字符串写入文本文件，要将数值数据存储到文本文件中，必须先使用函数str()将其转化为字符串格式

# 10-4
# filename = 'guest_book.txt'
# with open(filename,'w') as fileid:
#     while True:
#         names = input("(Enter q to quit)Input your name:\n")
#         if names != 'q':
#             print(f"Hello {names}!")
#             records = f"{names} has come.\n"      write()不会在写入的文本末尾添加换行符，因此一般在要存入的数据尾部加入换行符
#             fileid.write(records)
#         else:
#             break

# 10-5
# with open('reason.txt', 'a') as file:     附加模式会将写入文件的行添加到文件末尾
#     while True:
#         reason = input("Why do you like programming?(Enter q to quit)\n")
#         if reason != 'q':
#             file.write(f"{reason}\n")
#         else:
#             break

# 10.3 异常

# 10-6
# print("Enter two numbers, q to quit.")
# while True:
#
#     num1 = input("First number:")
#     if num1 == 'q':
#         break
#     num2 = input("Second number:")
#     if num2 == 'q':
#         break
#     try:                              使用try-except-else代码块来处理异常
#         num = int(num1) + int(num2)       将可能导致错误的代码放在try代码块中，如果没有问题，Python将跳过except代码块继续运行
#     except ValueError:                    如果出现异常，Python会执行except代码块
#         print("Please enter number.")     依赖try代码块执行成功的代码应放在else代码块中，否则运行完except代码块后也会运行else代码块
#     else:
#         print(num)

# 10-8
# try:
#     with open('cats.txt') as cats:
#         mao = cats.read()
# except FileNotFoundError:
#     pass                              pass语句表示静默，即出现异常后什么也不做
# else:
#     print(mao)
# try:
#     with open('dogs.txt') as dogs:
#         gou = dogs.read()
# except FileNotFoundError:
#     pass
# else:
#     print(gou)

# 10-10
# filename = "guest_book.txt"
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     pass
# else:
#     words = contents.split()          方法split()以空格(包括换行符、制表符和空格)将字符串拆分成多个部分，并存储到一个列表中
#     num = len(words)
#     print(f"This file has {num} words.")
#     print(words)
#     print(contents.count('xwt'))      方法count()计算特定单词或短语在字符串中出现多少次

# 10.4 存储数据

# 10-12
# import json
#
# filename = 'numbers.json'
# try:
#     with open(filename) as f:
#         numbers = json.load(f)
# except FileNotFoundError:
#     numbers = input("Please enter a number:\n")
#     with open(filename,'w') as f:
#         json.dump(numbers, f)
# else:
#     print(numbers)

# 10-13
# import json                           使用模块json存储数据，保留了原有数据格式，并且可供其他编程语言使用
#
# def get_stored_username():
#     """如果存储了用户名，就获取它。"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def get_new_username():
#     """提示用户输入用户名。"""
#     username = input("What's your name?\n")
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username                   重构：将代码划分为一系统完成具体工作的函数，使代码更清晰、更易于理解、更容易扩展
#
# def greet_user():
#     """问候用户，并指出其名字。"""
#     username = get_stored_username()
#     if username:
#         again = input("Please enter your name to confirm:\n")
#         if again == username:
#             print(f"Welcome back, {username}!")
#         else:
#             get_new_username()
#     else:
#         username = get_new_username()
#         print(f"We'll remember you when you come back, {username}!")
#
# greet_user()
