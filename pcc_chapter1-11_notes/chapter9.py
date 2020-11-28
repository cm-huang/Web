# Author: hcm Time: 2020/11/14

# chapter9 类


# 9.1 创建和使用类

# class Dog:                                                    类的首字母大写
#     """一次模拟小狗的简单尝试。"""
#
#     def __init__(self, name, age):
#         """初始化属性name和age。"""
#         self.name = name                                      类： 定义一大类对象都有的属性或通用行为
#         self.age = age                                            基于类创建对象时，每个对象都自动具有这种属性或通用行为
#
#     def sit(self):                                            方法_init_()是一个特殊方法，根据类创建实例时会自动运行
#         """模拟小狗收到命令时蹲下。"""                                 因此在Dog()中需要输入对应的实参，作用为初始化属性
#         print(f"{self.name} is now sitting.")
#                                                               self指实例名，创建类时会自动传入，以self为前缀的变量可供类中所有
#     def roll_over(self):                                          方法使用，可通过类的任何实例来访问，称为属性
#         """模拟小狗收到命令时打滚。"""
#         print(f"{self.name} rolled over!")
#
# my_dog = Dog('yyf', 22)                                       采用句点调用属性和函数
# your_dog = Dog('wxc', 22)
# print(f"My dog's name is {my_dog.name}.")
# your_dog.sit()

# 9.2 使用类和实例

# class Car:
#     """一次模拟汽车的简单尝试。"""
#
#     def __init__(self, make, model, year, odometer_reading=0):
#         """初始化描述汽车的属性。"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0                             给属性指定默认值：可在__init__()方法内指定，也可在括号内指定
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息。"""
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息。"""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):                       修改属性的值有三种方法：
#         """                                                       直接修改属性的值 my_new_car.odometer_reading = 30
#         将里程表读书设置为指定的值。                                    通过方法修改 update_odometer(self, mileage):
#         禁止将里程表读数往回调                                         通过方法对属性的值进行递增 increment_odometer(self, miles):
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的值。"""
#         self.odometer_reading += miles
# #
# # my_new_car = Car('audi', 'a4', 2019)
# # print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 30
# # my_new_car.update_odometer(20)
# # my_new_car.increment_odometer(10)
# # my_new_car.read_odometer()
#
# 9.3 继承
#
# class Battery:
#     """一次模拟电动汽车电瓶的简单尝试。"""
#
#     def __init__(self, battery_size=75):
#         """初始化电瓶的属性。"""
#         self.battery_size = battery_size
#
#     def discribe_battery(self):
#         """打印一条描述电瓶容量的消息。"""
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
# class ElectricCar(Car):                                           创建子类时，父类必须包含在当前文件中，且位于子类前面
#     """电动汽车的独到之处。"""
#
#     def __init__(self, make, model, year):                        方法__init__()接受创建Car实例所需的信息
#         """
#         初始化父类的属性。
#         再初始化电动汽车特有的属性。
#         """                                                       super()是一个特殊函数，调用父类方法__init__()
#         super().__init__(make, model, year)                           让ElectricCar实例能够调用父类的属性和方法
#         self.battery_size = 75
#         self.battery = Battery()                                  可将实例用作属性
#
#     def describe_battery(self):                                   可给子类定义属性和方法
#         """打印一条描述电瓶容量的消息。"""
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def fill_gas_tank(self):                                      可重写父类方法：定义一个与父类方法同名的方法
#         """电动汽车没有油箱。"""
#         print("This car doesn't need a tank!")
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.battery.discribe_battery()

# 9.4 导入类

# from car import Car                                               导入单个类
#
# from car import Car, ElectricCar                                  从一个模块中导入多个类
#
# import car                                                        导入整个模块
#
# from car import *                                                 导入模块中的所有类
#
# from car import Car                                               在一个模块中导入另一个模块
# class ElectricCar
#
# from electric_car import ElectricCar as EC                        使用别名

# 9.5 Python标准库

# from random import randint                                        Python标准库是一组模块，安装的Python都包含它
# randint(1, 6)
# from random import choice                                         也可从其他地方下载外部模块
# plays = ['charles', 'hcm', 'hsm']
# first_up = choice(plays)
