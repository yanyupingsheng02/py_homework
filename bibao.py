"""
作者:张杰
时间:2024年04月13日
"""
# 闭包
# 1
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c()) # 输出 1
print(c()) # 输出 2
print(c()) # 输出 3
# 2
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter
print(c()())
print(c()())
print(c()())
# 3
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()()#每次调用c都要重新执行一次counter()
print(c)
print(c)
print(c)
# 4
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment()

c = counter()#c直接被赋值为一个常量1
print(c)#1
print(c)#1
print(c)#1