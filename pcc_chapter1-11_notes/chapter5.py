# Author: hcm Time: 2020/11/6

# chapter5 if语句


# 5.2 条件测试

# cars = ['audi', 'bmw', 'benz', 'ferrari']
# for car in cars:
#     if car == 'bmw' and car != 'audi':            if语句基本格式，条件测试：即条件表达式，正确则返回值Ture，错误则返回值False
#         print(car.upper())                        Ture时执行代码块后退出if语句，False时则继续判断下一个条件表达式
#     else:                                         使用and（与）和or（或）来检查多个条件
#         print(car.title())

#     if 'bmw' in cars:                             使用关键字in和not in来检查特定值是否包含在列表中
#     if 'bmw' not in cars:

# game_active = True
# if game_active:                                   布尔表达式，将Ture或False赋给某个条件
#     print("The game is active.")

# 5.3 if语句

# age = 22
# if age > 18:                                      简单if语句
#     print("You are old.")

# if age > 18:                                      if-else
#     print("You are old.")
# else:
#     print("You are young.")

# if age < 4:
#     price = 0                                     if-elif-else
# elif age < 18:                                    只执行一个代码块，因此此处age<18等价于4=<age<18
#     price = 25                                    可以多个elif,也可以省略else
# else:                                             仅适用于一个条件满足的情况（遇到通过了的测试，会跳过其余测试）
#     price = 40                                    因此测试多个条件时可使用多个简单if语句
# print(f"Your cost is {price}.")

# 5.4 使用if语句处理列表(for循环与if语句联动)

# fruits = []
# if fruits:
#     for fruit in fruits:
#         print(f"I like {fruit}.")                 if语句中将列表名用作条件表达式时，列表为空时返回False，非空时返回Ture
#     print("\nI like fruits.")
# else:
#     print("The list is empty.")
