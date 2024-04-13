"""
作者:张杰
时间:2024年04月13日
"""
# 定义一个装饰器my_decorator，并将其应用到函数say_hello

# def my_decorator(func):
#     def wrapper():
#         print("执行函数前...")
#         func()
#         print("执行函数后...")
#     return wrapper()
#
# # @my_decorator
# def say_hello():
#     print("Hello, world!")
#
# my_decorator(say_hello)
#
# @my_decorator
# def say_goodbye():
#     print("Goodbye, world!")
# say_goodbye

#@my_decorator相当于 say_hello = my_decorator(say_hello)
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}执行时间：{end_time - start_time:.2f}s")
        return result
    return wrapper

@timer
def test_func(n):
    return sum(range(n))

test_func(100000000)

# 定义了一个装饰器timer，它可以记录函数调用的执行时间，并在输出结果前后显示相关信息。在函数test_func上添加装饰器之后，即可得到带有计时功能的新函数对象