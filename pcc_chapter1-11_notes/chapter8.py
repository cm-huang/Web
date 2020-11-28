# Author: hcm Time: 2020/11/8

# chapter8 函数


# 8.1 定义函数

# def greet_user(username):
#     """显示简单的问候语。"""                                   函数定义与调用的基本格式
#     print(f"Hello, {user.title()}.")                          括号内的相当于定义一个名为username的变量
#                                                               username为形参，即只有名字没有赋值的变量
#                                                               调用时输入的'hcm'为实参，即传递给函数的信息
# greet_user('hcm')                                             在第二行使用文档字符串对函数进行注释

# 8.2 传递实参

# def discribe_pet(animal_type, pet_name):
#     """显示宠物信息。"""
#     print(f"\nI have a {animal_type}.")                       传递实参方式：位置实参；关键字实参
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# discribe_pet('dog', 'penny')                                  位置实参：实参顺序与形参对应
# discribe_pet(pet_name='peky', animal_type='cat')              关键字实参：顺序无关紧要，注意等号两边无空格
# discribe_pet(animal_type='cat', pet_name='peky')              混用时，位置实参必须与形参位置对应

# def discribe_pet(pet_name, animal_type='dog'):
#     """显示宠物信息。"""
#     print(f"\nI have a {animal_type}.")                       给形参指定默认值，可简化函数用法
#     print(f"My {animal_type}'s name is {pet_name.title()}.")  如果没有给animal_type指定实参，则Python就将其设为默认值'dog'
# discribe_pet('penny')                                         注意使用默认值时，必须现在形参列表中列出没有默认值的形参
# discribe_pet(pet_name='penny')                                再列出有默认值的实参，以便Python正确地解读位置实参
# discribe_pet('cat', 'peky')
# discribe_pet(animal_type='cat', pet_name='peky')

# 8.3 返回值

# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名。"""                                       返回值：在函数中使用return语句将值返回到调用函数的代码行
#     full_name = f"{first_name} {last_name}"                   函数可返回任何类型的值，包括列表、字典等
#     return full_name                                          调用函数时，需要提供一个变量，以便将返回的值赋给它
# player = get_formatted_name('h', 'cm')
# print(player)

# def get_formatted_name(first_name, last_name, middle_name=None):
#     """返回整洁的姓名。"""
#     if middle_name:                                           让实参变成可选的：使用默认值，将对应形参设置为None，注意移至末尾
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:                                                     if条件中，Python将非空字符串/列表/字典解读为Ture
#         full_name = f"{first_name} {last_name}"
#     return full_name
# player = get_formatted_name('h', middle_name='x', last_name='cm')
# print(player)

# def build_person(first_name, last_name, age=None):
#     """返回一个字典，其中包含有关一个人的信息。"""
#     person = {'first': first_name, 'last': last_name}         返回字典
#     if age:
#         person['age'] = age
#     return person
# while True:
#     print("\nPlease tell me your name:")
#     print("(Enter 'q' at any time to quit.)")
#     f_name = input("First name: ")                            结合使用函数和while循环
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     full_name = build_person(f_name, l_name)
#     print(f"\nHello, {full_name}!")

# 8.4 传递列表

# def greet_users(names):
#     """问候"""
#     for name in names:                                        向函数传递列表
#         print(f"Hello, {name}!")
# usernames = ['hcm', 'hsm', 'xwt']
# greet_users(usernames)

# def zuofan(yidian, yizuo):
#     """zuofan"""
#     while yidian:
#         zaizuo = yidian.pop()
#         print(f"zaizuozhong: {zaizuo}")                       在函数中修改列表
#         yizuo.append(zaizuo)
# def xianshi(yizuo):                                           如果想保留原列表，可使用其副本进行操作
#     """xainshi"""                                             即将列表的副本传递给函数
#     print("\nyi jin zuo hao de:")                             如：zuofan(yidian[:], yizuo)
#     for cai in yizuo:
#         print(cai)
# yidian = ['chicken', 'fish', 'beef']
# yizuo = []
# zuofan(yidian, yizuo)
# xianshi(yizuo)

# 8.5 传递任意数量的实参

# def make_pizza(size, *toppings):
#     """概述披萨"""
#     print("Making a pizza with the follow toppings:")         传递任意数量的实参：使用星号*
#     for topping in toppings:                                  形参名*toppings中的星号*让Python创建一个名为toppings的空元组
#         print(f"- {topping}")                                 并将收到的所有值都封装到这个元组中
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'extra cheese')                    如果要让函数接受不同类型的实参，必须在函数定义中将任意数量形参放在最后
#                                                            Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中

# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     user_info['first_name'] = first                           **toppings让Python创建一个名为toppings的空字典
#     user_info['last_name'] = last                             并将收到的所有名称值对都放在这个字典中
#     return user_info
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',            使用任意数量的关键字实参，相当于在字典中创建一个键值对，无需分号
#                              field='physics')
# print(user_profile)

#  8.6 将函数存储在模块中                                         模块：只包含函数代码的.py文件

# import module_name                                            导入整个模块
#                                                               调用被导入模块中的函数：模块名.函数名
# module_name.function_name()

# from module_name import function_name                         导入特定的函数
# from module_name import function_0, function_1, function_2    导入多个函数
# function_name()                                               调用函数：直接函数名

# from pizza import make_pizza as mp                            使用关键字as给函数指定别名
# mp()                                                          调用函数：使用别名

# import module_name as mn                                      使用关键字as给模块指定别名

# from module_name import *                                     使用星号（*）运算符导入模块中的所有函数
#                                                               但最佳做法是只导入需要的函数，或者导入整个模块并使用句点表示法
