"""
作者:张杰
时间:2024年03月19日
"""


# 一、思考以下代码的结果
# grades = [grade / 2 for grade in range(201)]
# print(grades)
# 二、定义一个函数，作用是：接收两个参数，打印这两个个参数的类型（type），并且返回两
# 者类型是否相等。然后调用这个函数，分别传入相同类型参数以及不同类型参数尝试
# 1.
grades = [grade / 2 for grade in range(201)]
print(grades)
# 结果:[0,0.5,1.0 ...,100.0]
# 2.


def type_test(x, y):
    print(type(x), type(y))


a = (1, 2)
b = {1, 2}
c = 1
d = {}
type_test(y=a, x=b)
type_test(c,d)