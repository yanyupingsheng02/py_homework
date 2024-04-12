"""
作者:张杰
时间:2024年04月12日
"""
# import os
# print(os.getcwd() )
# print(os.listdir(os.getcwd()))
# if os.path.exists("E:\学习资料\python\资料\HOMEWORK\pratice\\test"):
#     os.rmdir("E:\学习资料\python\资料\HOMEWORK\pratice\\test")
# else:
#     os.mkdir("test")
# if(os.path.exists("digui/test")):
#     os.removedirs("digui/test")
# else:
#     os.makedirs("digui/test")
# file = open(r"E:\学习资料\python\资料\HOMEWORK\课件\python基础\补充.txt","r")
# print(file.read())
# with open(r"E:\学习资料\python\资料\HOMEWORK\课件\python基础\补充.txt","r", encoding='UTF-8') as file:
#     print(file.read())
#
#     # 在with代码块中进行文件操作
#
# # 在with代码块外，文件资源已经被自动释放,不需要file.close(
try:
    with open(r"E:\学习资料\python\资料\HOMEWORK\课件\python基础\补充.txt" ,"r",encoding="UTF-8") as file:
        print(file.read())
except(BaseException):
    print("存在异常")
except(UnicodeDecodeError):
    print("解码方式有误")
except:
    print("未知错误")
else:
    print("没有错误")
finally:
    print("执行结束")
