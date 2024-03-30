"""
作者:张杰
时间:2024年03月10日
"""
# 一
# 1.集合是可变类型还是不可变类型  可变
# 2.集合是不是序列 不是
# 3.集合里的元素可以重复吗 不可以
# 4.集合里的元素要满足什么条件
# 集合里的元素必须是不可变的类型，例如整数、浮点数、字符串、元组等，
# 不能包含可变类型的元素，例如列表、字典（集合后一节的内容）等。

# 二、set_a = {'chatgpt'，'爬虫'}，set_b = {'chatgpt'，'自动化办公'}
# 1.求这两个集合的交集（&），并集（|）
set_a = {'chatgpt', '爬虫'}
set_b = {'chatgpt', '自动化办公'}
print(set_a & set_b)
print(set_a | set_b)
# 2.在set_a中添加元素'python基础'（add），再删除元素'爬虫'（remove）

set_a.add("python基础")
print(set_a)
set_a.remove("爬虫")
print(set_a)
