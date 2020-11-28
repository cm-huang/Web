# Author: hcm Time: 2020/11/7

# chapter7 用户输入和while循环

# 7.1 函数input()的工作原理

# message = input("Tell me something, and I will repeat it to you:\n")
# print(message)                                                函数input()工作原理：先让程序暂停运行
# print(isinstance(message, str))                               然后打印括号内的参数（要向用户显示的提示或说明）
#                                                               然后等待用户输入一些文本，获取用户输入后，再赋给一个变量
# prompt = "If you tell us who you are, "                       使用函数input()时，Python将用户输入解读为字符串
# prompt += "I can give you 10 yuan."
# message = input(prompt)                                       提示过长时，可将提示赋给一个变量
# print(message)                                                += 表示 prompt = prompt + "I can give you 10 yuan."

# number = input("Enter a number.\n")
# number = int(number)
# if number % 2 == 0:                                           使用函数int()将字符串（数字型）转换为数值
#     print("It's even.")                                       求模运算符 % ：将两数相除并返回余数
# else:
#     print("It's odd.")

# 7.2 while循环简介

# prompt = "Tell me something, I will repeat it. "
# prompt += "Enter 'quit' to end the program.\n"
# message = ""                                                  for循环用于针对集合中的每个元素都执行一个代码块
# while message != 'quit':                                      而while循环则不断运行，直到指定的条件不满足为止
#     message = input(prompt)                                   定义退出值时，应先设置一个初始值以供while检查
#     if message != 'quit':
#         print(message)

# active = True
# while active:
#     message = input(prompt)                                   在要求很多条件都满足时才继续运行的程序中，可使用变量标志
#     if message == 'quit':                                     标志值为Ture时，程序继续运行，为False时，程序停止运行
#         active = False
#     else:
#         print(message)

# while True:
#     message = input(prompt)
#     if message == 'quit':                                     使用break语句退出循环（任何Python循环）
#         break                                                 与上述两种相比，无需定义初始值
#     else:
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1                                       continue语句：忽略代码块中剩余代码，返回循环开头，继续运行循环代码
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# 7.3 使用while循环处理列表和字典

# unconfirmed_users = ['hcm', 'hsm', 'xwt']
# confirmed_users = []
# while unconfirmed_users:                                      在遍历列表的同时对其进行修改，可使用while循环
#     current_user = unconfirmed_users.pop()                    for循环是一种遍历列表的有效方式，但不应在for循环中修改列表
#     print(f"Verifying user: {current_user.title()}")          否则会导致Python难以跟踪其中的元素
#     confirmed_users.append(current_user)
# print(f"\nHave been confirmed users: ")                       在列表之间移动元素
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['cat', 'dog', 'tiger', 'cat']
# while 'cat' in pets:                                          删除为特定值的所有列表元素：在while中使用方法remove()
#     pets.remove('cat')
# print(pets)

# responses = {}
# active = True
# while active:
#     name = input("\nWhat's your name?\n")
#     response = input("What's your answer?\n")                 使用用户输入来填充字典
#     responses[name] = response
#     repeat = input("Any other?(Yes/No)\n")
#     if repeat == 'No':
#         active = False
# print("\n--- Poll Results ---\n")
# for name, response in responses.items():
#     print(f"{name.title()}'s answer is {response}.")

# 练习 7-9

# sandwich_orders = ['chicken', 'pastrami', 'beef', 'pastrami', 'fish', 'pastrami']
# finished_sandwiches = []
# print("Pastrami sold out.")
# while sandwich_orders:
#     sandwich_orders.remove('pastrami')
#     if 'pastrami' not in sandwich_orders:
#         break
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(sandwich)
# for sandwich in finished_sandwiches:
#     print(sandwich)

# 练习 7-10

# people_travel = {}
# while True:
#     people = input("\nWhat's your name?\n")
#     travel = input("Where do you want to go?\n")
#     people_travel[people] = travel
#     repeat = input("Any other?(Yes/No)\n")
#     if repeat == "No":
#         break
# print("\n--- Results ---\n")
# for people, travel in people_travel.items():
#     print(f"{people}: {travel}")
