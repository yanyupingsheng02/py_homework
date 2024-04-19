"""
作者:张杰
时间:2024年04月16日
"""
# 生成器 generator
# gen = (i for i in range(3))  # 生成器属于迭代器对象，也属于迭代对象
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# fib1=fib()
# for i in range(5):
#     print(next(fib1))
# fib1.send(5)
# print(next(fib1))
def my_generator():
    while True:
        val = yield     # 中间值接收
        if val is not None:
            print(f"Received value: {val}")
        else:
            print("No value received")

gen = my_generator()

next(gen)       # 启动生成器

gen.send(10)    # 向生成器发送值 10
gen.send("Hello")   # 向生成器发送字符串 "Hello"
gen.send(None)  # 向生成器发送空值