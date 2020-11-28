# Author: hcm Time: 2020/11/18

# chapter11 测试代码


# 11.1 测试函数

# import unittest                                                   模块unittest提供了代码测试工具
# from city_functions import sites                                  单元测试用于核实函数的某个方面没有问题（一个单元即一个def）
#                                                                   测试用例是一组单元测试
# class CaseTest(unittest.TestCase):                                首先导入模块unittest和要测试的函数
#     """测试city_functions.py"""                                    接着定义一个测试子类，必须继承unittest.TestCase类
#
#     def test_city_country(self):                                  test_打头的方法将自动运行
#         """测试"""
#         site = sites('santiago', 'chile')
#         self.assertEqual(site, "Santiago, Chile - population ")   断言方法：核实得到的结果是否与期望的结果一致
#
#     def test_city_country_population(self):
#         """测试"""
#         site = sites('santiago', 'chile', 5000)
#         self.assertEqual(site, "Santiago, Chile - population 5000")
#
# if __name__ == '__main__':                                        运行程序时会设置变量__name__，如果程序作为主程序执行，其值将为__main__
#     unittest.main()                                               调用unittest.main()来运行测试用例

# 11.2 测试类

# import unittest
#                                               六种断言方法：
#                                                       assertEqual(a, b)           核实a == b
# class AnonymousSurvey:                                assertNotEqual(a, b)        核实a != b
#     """收集匿名调查问卷的答案"""                          assertTrue(x)               核实x为True
#                                                       assertFalse(x)              核实x为False
#     def __init__(self, question):                     assertIn(item, list)        核实item在list中
#         """存储一个问题，并为存储答案做准备"""              assertNotIn(item, list)     核实item不在list中
#         self.question = question
#         self.responses = []
#
#     def show_question(self):
#         """显示调查问卷"""
#         print(self.question)
#
#     def store_response(self, new_response):
#         """存储单份调查答卷"""
#         self.responses.append(new_response)
#
#     def show_results(self):
#         """显示收集到的所有答卷"""
#         print("Survey results:")
#         for response in self.responses:
#             print('- ' + response)
#
#
# class TestAnonymousSurvey(unittest.TestCase):
#     """针对AnonymousSurvey类的测试"""
#
#     def setUp(self):                              方法setUp()可创建一系列实例和属性，并且在不同的测试单元中会被重置，所有可供所有测试单元使用
#         """                                           Python将先运行setUp()方法，再运行各个以test_打头的方法
#         创建一个调查对象和一组答案，供使用的测试方法使用
#         """
#         question = "What language did you first learn to speak?"
#
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']  # 存储这两样东西的变量名包含前缀self，因此可在这个类的任何地方使用
#
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)
#         print(self.my_survey.responses)
#
#     def test_store_three_responses(self):
#         """测试三个答案会被妥善地存储"""
#         print(self.my_survey.responses)
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response, self.my_survey.responses)
#         print(self.my_survey.responses)
# if __name__ == '__init__'
#     unittest.main()

# 11-3
# import unittest
#
#
# class Employee:
#
#     def __init__(self, first, last, money):
#         self.first = first
#         self.last = last
#         self.money = money
#
#     def give_raise(self, lift=5000):
#         self.money += lift
#
#
# class Testem(unittest.TestCase):
#
#     def setUp(self):
#         self.exam = Employee('cm', 'h', 10000)
#
#     def test_give_default_raise(self):
#         self.exam.give_raise()
#         money = 15000
#         self.assertEqual(self.exam.money, money)
#
#     def test_give_custom_raise(self):
#         self.exam.give_raise(20000)
#         money = 30000
#         self.assertEqual(self.exam.money, money)
#
#
# if __name__ == '__init__':
#     unittest.main()
