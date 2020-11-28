# Author: hcm Time: 2020/11/4

# chapter3 列表简介


# 3.1 列表是什么

# bicycles = ['trek','redline',4]               列表变量由一系列按特定顺序排列的元素组成，类似于matlab中的元胞数组/单元数组
# print(bicycles[-2].title())                   元素索引从0开始，也可用负数索引，如-1表示最后一个元素
# message = "My bicycle is a " + "bicycles(0)"
# print(message)

# 3.2 修改、添加和删除元素

# motorcycles = ['honda','yamaha','suzuki']
# motorcycles[0] = 'ducati'                     修改列表中的元素
# print(motorcycles)

# motorcycles.append('honda')
# print(motorcycles)                            方法append()从末尾添加一个元素
# motorcycles.insert(0,'honda')                 方法insert()从任意位置添加一个元素
# print(motorcycles)

# del motorcycles[1]                            del语句删除任意位置的一个列表元素
# print(motorcycles)

# popped_motorcycles = motorcycles.pop()
# print(motorcycles)                            方法pop()可弹出一个列表元素，弹出的值仍可使用
# print(popped_motorcycles)                     ()为空时弹出末尾元素，指定索引可弹出任意位置元素
# first_owned = motorcycles.pop(0)
# print('The first is ' + first_owned.title())

# too_expensive = 'honda'
# motorcycles.remove(too_expensive)             方法remove()根据给定值删除一个元素，但是只删除第一个指定的值，若出现多次需使用循环
# print(motorcycles)                            使用remove()方法时也可使用被删除的元素，将其存储在某个变量内即可
# print("\nA " + too_expensive + " is too expensive")

# 3.3 组织列表

# cars = ['bmw','audi','auto','1','a']
# cars.sort()                                   方法sort()对列表元素进行永久排序，默认为从小到大
# print(cars)                                   向方法sort()传递参数reverse=Ture,可反向排序
# cars.sort(reverse=True)
# print(cars)

# print("The original list:")
# print(cars)
# print("\nThe sorted list:")                   函数sorted()对列表进行临时排序
# print(sorted(cars,reverse=True))
# print("\nThe original list again:")
# print(cars)

# cars.reverse()                                方法reverse()永久反转列表元素的排列顺序
# print(cars)

# len(cars)                                     函数len()计算列表长度，即元素个数
# print(len(cars))

