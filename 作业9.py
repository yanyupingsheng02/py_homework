"""
作者:张杰
时间:2024年03月16日
"""
# 一、用for循环计算一个任意列表里奇数元素的和
# 提示:判断是否为奇数例子：if num % 2 == 1:
# 二、（附加题）模拟输入密码场景，用户总共有三次机会，每一次密码输入之后如果正确就可
# 以打开门，(提示：==可以判断内容是否相等)就停止继续输入密码。如果输入错误进行提示还
# 有几次输入的机会，继续输入，直到三次机会用完，结束程序，如果成功打开门最后再打印字
# 符串'欢迎光临'(else)
# 1.
list1 = [1, 2, 3, 4, 5]
sum1 = 0
sum2 = 0
for i in range(len(list1)):
    if list1[i] % 2 == 1:
        sum1 += list1[i]
print(sum1)
# for j in list1:
#     if j % 2 == 1:
#         sum2 += j
# print(sum2)
# 2.
Password = "a123456"
for i in range(1, 4):
    password = input("请输入密码：")
    if password == Password:
        print("欢迎光临")
        break
    else:
        print(f"密码错误还有{3-i}次机会")