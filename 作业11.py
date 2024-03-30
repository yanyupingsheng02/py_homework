"""
作者:张杰
时间:2024年03月21日
"""
# 一、定义函数，该函数能求出一个学生的总成绩，例：s1 = {'语文': 107, '数学': 113, '英语':
# 140, '理综': 264}，并测试其功能（可以查询字典课件）
# 二、定义函数，能求任意个数的数字的乘积（），例：当用户传了2, 3，就计算2乘以3，传了
# 3,4,5，就计算3乘4乘5
# values()不能直接相加，需强制转换
# 1.
# def sum_score(a):
#     s=sum(a.values())
#     return s
# a={'语文': 107, '数学': 113, '英语':140, '理综': 264}
# print(sum_score(a))
# 2.
# def mut(a):
#     s=1
#     for i in range(a,2*a):
#         s *= i
#     return s
# print(mut(1))
# print(mut(2))
# print(mut(3))
# print(mut(4))
def mutp(*args):
    result=1
    for i in args:
        result*=i
    print(result)
mutp(1,5,22)