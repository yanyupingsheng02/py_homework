"""
作者:张杰
时间:2024年04月16日
"""
# 迭代器
# 迭代器是一个定义了__iter__()和__next__()方法的对象。在Python中，很多内置对象都是可以被迭代的，
# 例如列表、元组、字典、集合、字符串等。iterable（可迭代的）
# 优势相较于for循环更加高效灵活
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
#
# while True:
#     try:
#         value = next(my_iterator)
#         print(value)
#     except StopIteration:
#         break
# # 等同于
# for i in my_list:
#     print(i)
# 迭代器实现方法---重写__iter__()和__next__()
# 作用：记住当前当前遍历的位置，通过next方法获取下一个元素，并且可以用for循环遍历
# class MyIterator:
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.string):
#             raise StopIteration
#         result = self.string[self.index]
#         self.index += 1
#         return result
#
#
# my_iterator = MyIterator("Hello, world!")
#
# for char in my_iterator:
#     print(char)
# map(function, iterable)：将一个函数应用于可迭代对象的每个元素，并返回一个新的迭代器对象，其中包含了应用后的结果；
# my_list = [1, 2, 3, 4, 5]
# # new_list = list(map(lambda x: x ** 2, my_list))
# # print(new_list)
# my_tuple = ("apple", "banana", "cherry")
# my_dict = {"name": "John", "age": 36, "country": "Norway"}
# for item in zip(my_list, my_tuple, my_dict):
#     print(item)
# for char in reversed("Hello, world!"):
#     print(char)
gen = (i for i in range(3))  # 生成器属于迭代器对象，也属于迭代对象
print(next(gen))
print(next(gen))
print(next(gen))
