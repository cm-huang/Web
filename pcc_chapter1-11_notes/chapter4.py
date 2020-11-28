# Author: hcm Time: 2020/11/4

# chapter4 操作列表(for循环)


# 4.1 遍历整个列表                                            for a in b:   b必须是列表或字典或range()等能包含多个值的形式

# magicians = ['hcm', 'hsm', 'yyf']
#     print("Thank you, everyone!")                         python中一行代码中的第一个命令不能有空白，否则会报错，这点与matlab不同
# for magician in magicians:                                for循环中，有缩进的代码为循环内代码，当列表内所有元素执行完毕后
#     print(magician.title() + ", that's a great trick!")   自动结束循环，无需end。循环结束后继续执行未缩进代码
#     print("I can't wait to see your next trick.")
# print("Thank you, everyone!")

# 4.3创建数字列表

# numbers = list(range(1, 10))
# print(numbers)
# squares = []                                              函数range()用于生成一系列数字,达到最后的值时不会输出
# for value in range(1, 11):                                range(123) = range(0, 123)
#     square = value ** 2                                   生成数字列表方法有三：
#     squares.append(square)                                1. 使用函数list()；
# print(squares)                                            2. 使用for循环（先创建一个空列表，再往内添加元素）
# print(min(squares))                                       3. 列表解析方法（只需一行代码）
# print(max(squares))                                       Python还提供了函数min()、max()、sum()求最小值、最大值、总和
# print(sum(squares))
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# 4.4 使用列表的一部分

# players = ['hcm', 'hsm', 'yyf', 'zy']
# print(players[0:3])                                       切片：列表的部分元素组成的列表
# print(players[:4])                                        索引从0开始
# print(players[1:])
# print(players[-3:])

# print("Players on my team:")
# for player in players[:3]:                                for循环遍历列表
#     print(player.title())

# my_foods = ['apple', 'banana', 'peach']                   使用切片复制列表，my_foods和friend_foods为两个不同的列表
# friend_foods = my_foods[:]                                如果直接赋值，相当于把新变量friend_foods关联到包含在my_foods中的列表
# friend_foods = my_foods                                   这时两个变量为同一个列表

# 4.5 元组

# dimensions = (100, 60)                                    元组：不能修改元素值的列表，用()标识，访问元素时与列表一致
# print(dimensions[0])
# dimensions[0] = 250

# for dimension in dimensions:                              遍历元组
#     print(dimension)

# dimensions = (200,50)
# print("\nmodified dimensions:")                           虽然不能修改元组内元素的值，但可以重新定义整个元组变量
# print(dimensions)
