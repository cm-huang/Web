# Author: hcm Time: 2020/11/6

# chapter6 字典


# 6.2 使用字典

# point1 = [5, 23]
# # alien_0 = {'color': 'green', 'point': point1}           字典是一系列键值对，每个键与一个值相关联
# print(alien_0['point'])                                   与键相关联的值可以是任何Python对象
# color1 = alien_0['color']                                 获取值时如果指定的键不存在会出错
# print(color1)

# point_value = alien_0.get('point', 'no point')            方法get()访问值
# print(point_value)                                        指定的键不存在时会返回第二个参数的值，若未指定则返回None

# alien_0 = {}
# alien_0['x_position'] = 0                                 添加键值对:用中括号[]直接创建键和值即可。列表不可这样操作
# alien_0['y_position'] = 25                                元素排列顺序与添加顺序相同
# print(alien_0)

# alien_0['x_position'] = 1                                 修改字典中的值的方式与列表相同

# del alien_0['x_position']                                 使用del语句删除键值对

# favorite_languages = {
#     'hcm': 'python',
#     'hsm': 'c',                                           也可使用字典存储众多对象的同一种信息
#     'yyf': 'java',                                        将一个较大的字典放在了多行，列表也可这么操作
# }
# print(favorite_languages['hcm'].title())

# 6.3 遍历字典

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'enrico',
# }
# for key, value in user_0.items():                         遍历所有键值对：方法items(),其中两个变量key和value名称随意
#     print(f"\nKey: {key}")                                user_0.items()返回一个包含所有键值对的列表
#     print(f"Value: {value}")

# for name in user_0.keys():
#     print(name.title())                                   遍历字典中的所有键：方法keys()
# if 'second' not in user_0.keys():                         user_0.keys()返回一个包含所有键的列表
#     print("No second.")                                   若直接for name in user_0,则默认遍历键

# for x in user_0.values():                                 遍历字典中的所有值：方法values()，该方法没有考虑重复
#     print(f"x= {x}")                                      user_0.values()返回一个包含所有值的列表

# for x in set(user_0.values()):                            为剔除重复项，可使用集合
#     print(f"\nx= {x}")                                    对包含重复元素的列表调用set()，可找出列表中独一无二的元素，并创建集合

# languages = {'python', 'c', 'ruby', 'python'}             使用一对花括号直接创建集合
# print(languages)                                          不同于列表和字典，集合不会以特定的顺序存储元素，每次打印元素排列顺序都不同

# 6.4 嵌套

# aliens = []
# for number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     alien['color'] = 'yellow'                             在列表中存储字典
#     alien['points'] = 10
#     alien['speed'] = 'medium'
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"\nTotal number of aliens is: {len(aliens)}.")

# favorite_languages = {
#     'hsm': ['python', 'c'],
#     'hcm': ['python'],
#     'yyf': ['java', 'c++'],
# }                                                         在字典中存储列表
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print(f"\n{name.title()}'s favorite language is:"
#               "\n\t{languages[0].title()}.")
#     else:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"\t{language.title()}.")

# users = {
#     'hcm': {
#         'first': 'h',
#         'last': 'cm',
#         'location': 'xian',
#     },
#     'hsm': {
#         'first': 'h',
#         'last': 'sm',
#         'location': 'nc',                                 在字典中存储字典
#     },
# }
# for user_name, user_info in users.items():
#     print(f"\nUsername: {user_name.title()}.")
#     fullname = f"{user_info['first'].title()}{user_info['last']}"
#     location = f"{user_info['location'].title()}."
#     print(f"\tFullname: {fullname}.")
#     print(f"\tLocation: {location}")

# 练习 6-11

# cities = {
#     'shanghai': {
#         'country': 'china',
#         'population': 1000_0000,
#         'fact': 'beautiful',
#     },
#     'beijing': {
#         'country': 'china',
#         'population': 1500_0000,
#         'fact': 'important',
#     },
#     'xian': {
#         'country': 'china',
#         'population': 500_0000,
#         'fact': 'history',
#     },
# }
# for city, info in cities.items():
#     print(f"\n{city.title()}:")
#     for key, value in info.items():
#         print(f"\t{key.title()}:")
#         if isinstance(value, str):
#             print(f"\t\t{value.title()}")
#         else:
#             print(f"\t\t{value}")
