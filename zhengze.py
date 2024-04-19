"""
作者:张杰
时间:2024年04月19日
"""

import re
#
# # 定义正则表达式  '\d+'，它可以匹配一个或多个数字字符
# pattern = r'\d+?'
#
# # 定义字符串
# string = '10 2The price of the apple is 26 dollars, and the price of the orange is 1 dollar.'
#
# # 使用 findall() 函数查找数字
# result = re.findall(pattern, string)
# # 使用 match() 函数查找数字
# print(result)
# result1 = re.match(pattern, string)
# if result1 :
#     print("匹配成功",result1.group(0))
# else:
#     print("匹配失败")
# # 输出结果
# 匹配邮箱
# pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
# pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(com)$'
# emails = ['example@mail.com','a@a886', 'test.email123@mail.co.uk', 'user.name@example.com', 'invalid_email.com']
#
# for email in emails:
#     if re.match(pattern, email): print(f'{email} 是一个有效的邮箱地址')
#     else: print(f'{email} 不是一个有效的邮箱地址')
# 定义 Unicode 字符串
unicode_str = u'Hello, 你好！'

# 定义 ASCII 字符串
ascii_str = 'Hello, world!'

# 定义正则表达式
pattern = r'\w+'

# 使用 re.U 修饰符进行匹配
match_result1 = re.findall(pattern, unicode_str, re.U)
print("使用 re.U 修饰符的匹配结果：", match_result1)

# 不使用 re.U 修饰符进行匹配
match_result2 = re.findall(pattern, unicode_str)
print("不使用 re.U 修饰符的匹配结果：", match_result2)