"""
作者:张杰
时间:2024年03月30日
"""
# 一、 1.定义一个人类People
# 2.重写类的init构造方法，能够传入参数初始化人的名字name和年龄age属性，并且打印下面这句话:调用父类构造方法
# 3.定义一个Chinese类继承人类
# 4.用Chinese类,在里面定义一个方法say，作用为打印'我是中国人'，并创建一个中国人对象
# 5.(附加题).重写Chinese类的init构造方法，能够传入参数初始化人的名字和年龄属性，并且打
# 印下面这句话:调用子类构造方法, 然后重新运行代码，说说为什么输出改变
# 提示：重写构造方法即为在类里写一个init方法，创建对象报错？没有传入参数，因为父类的
# init方法需要传两个参数
# 二、理解课堂代码（私有成员部分了解即可）


class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("调用父类构造方法")


class Chinese(People):
    @classmethod
    def say(cls):
        print("我是中国人")


zhangsan = Chinese("张三",3)
zhangsan.say()
print("姓名"+zhangsan.name,"年龄：",zhangsan.age)

# 附加5


class Chinese2(People):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("调用子类构造方法")

    @classmethod
    def say(cls):
        print("我是中国人")


lisi = Chinese2("李四", 4)
lisi.say()
print("姓名"+lisi.name,"年龄：", lisi.age)
# 输出改变原因：重写了init方法，父类people的init方法被覆盖了
    