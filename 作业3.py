# 1. 6 -5
# 2
a = 1
b = 2.0
print(type(a), type(b))
a = str(a)
b = str(b)
print(type(a), type(b))
# 3.字符串切片
birthday = input("输入出生年月日（xxxx年xx月xx日）")
# birthday = "xxxx年xx月xx日"
# 方法一
print(f"生日:{birthday[5:]}")
# 方法二
birthday = birthday.split("年")
print(f"生日:{birthday[1]}")