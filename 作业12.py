"""
作者:张杰
时间:2024年03月23日
"""
# 一、请思考以下两段代码的执行结果
# 1         2\n 3\n 2\n 1
# x=1
# def fuc1():
#     x=2
#     print(x)
#
#     def fuc2():
#         x=3
#         print(x)
#     fuc2()
#     print(x)
# fuc1()
# print(x)
# 2.     2\n 4\n 5\n 3\n 3\n
x=1
def fuc1():
    global x
    x=2
    print(x)
    x=3

    def fuc2():
        x=4
        print(x)
        def fuc3():
            nonlocal x
            x=5
        fuc3()
        print(x)

    fuc2()
    print(x)
fuc1()
print(x)
#  nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量