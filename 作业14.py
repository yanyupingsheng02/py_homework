"""
作者:张杰
时间:2024年03月28日
"""


# # 作业：1.定义一个类,类里面包含一个属性，一个对象方法（类里面直接定义的函数就是对象方法）
# 2.通过这个类创建一个对象，调用对象方法，打印类属性
# 3.给类添加初始化（构造）方法（__init__），并传入参数来创建对象，打印对象属性
# 1.

# import this

class class1(object):
    x = 11

    # @staticmethod
    def fun(self, a, b):
        return a + b + self.x

    def __init__(self, c):
        self.y = c

    @classmethod
    def fuc(cls):
        print("调用类方法")

    def object_method(self):
        print(self.x)

cla = class1(4)
print(cla.x)
print(cla.fun(1, 2))
print(cla.y)
class1.fuc()
cla.object_method()

