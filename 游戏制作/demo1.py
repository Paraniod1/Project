'''
print('{0},{1}'.format("xiao", 1122))   # 若无顺序要求默认依次填充  序号可以控制后面输出的顺序
print('{name},{age}'.format(name="xiao", age=90)) # 这里没有顺序要求

print('{:>8}'.format('fei'))   # 右对齐 8位数据  空格填充
print('{:0>8}'.format('fei'))  # 右对齐 8位数据  0填充

print ('{:.2f}' .format(3.141592))  # 保留2位小数print('{:>8}'.format('fei'))   # 右对齐 8位数据  空格填充
print('{:0>8}'.format('fei'))  # 右对齐 8位数据  0填充
'''
# print('My name is %s' % "mingfei")     #与c语言类似
# print('My name is %s, and I am %d years old.' % ("mingfei", 60)) # 多个控制位输出采用元组类型

# ls1 = [122, 'balbal', 98]
# ls2 = ls1          # 用“=”进行复制时，只是会给现存的对象添加一个新的引用，并不会在内存中生成新的对象 两个变量指向了同一个值
# ls3 = ls1[:]   # 分片[:]复制 会创建一个新的对象 地址是不同的 copy()函数和分片相同
# ls1[0] = 25
# print(ls1)
# print(ls2)
#print(ls3)


#  # 一个异常信息
# try:
#     print(a)
# except NameError as result:
#     print(result)
#
# # 捕获多个异常信息
# try:
#     open("test.txt")
# except (NameError,IOError) as result:
#     print("哈哈，捕获到异常")
#     print("异常的基本信息：%s" % result)
#
# # 捕获所以的异常
# try:
#     open("test.txt")
# except Exception as result:
#     print("捕获到异常")
#     print(result)
#

# import pickle
#
# def unserialize():
#     f = open('test1.pkl', 'rb')
#     test = pickle.load(f)
#     print(test)
#
#
# if __name__ == "__main__":
#     unserialize()
#    serialize()

# import pickle
#
# def unserialize():
#     result = b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x03jan\x94\x8c\x03tom\x94\x8c\x04kang\x94e.'
#     ls = pickle.loads(result)
#     print(ls)
#
# if __name__  == "__main__":
#     unserialize()

# class Student(object):
#     # __下划线表示类私有的
#     def __init__(self, name, sex, height):
#         self.name = name
#         self.sex = sex
#         self.height = height
#         print("my name is {},sex is {},height is {}".format(name, sex, height))
#     def Gostudy(self):
#         print("go to school")
#
# stu1 = Student("tom", "男", 1.80 )
#
# stu1.Gostudy()

# class Person(object):
#     def __init__(self, name):
#         self._name = name  # 类的私有属于
#
#     def getName(self):
#         return self._name
#
#     def setName(self, name):
#         self._name = name
#
# tom = Person("tom")
# print(tom.getName())   # 获取类私有数据的属性

# class Father(object):
#     def eat(self):
#         print("苹果")
#
# class Mother(object):
#     def eat(self):
#         print("草莓")
#
# class Child(Father, Mother):
#     def test(self):
#         return self.eat()
#
# tom = Child()
#
# tom.eat()

# class Animal(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Person(Animal):
#     def __init__(self, name, age, emtion):
#         super(). __init__(name, age) # 继承父类，并定义新的属性
#         self.emtion = emtion
#
#     def test(self):
#         print("name:{},age:{},emtion:{}".format(self.name, self.age, self.emtion))
#
# tom = Person("tom", 18, "单身狗")
# tom.test()   # name:tom,age:18,emtion:单身狗

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, name, age):
#         if age > 0 and age <150:
#             return super().__new__(cls)  # object.__new__(cls) 必须调用父类的方法返回
#         else:
#             None
#
#     def str(self):
#         print("name:{}，age:{}".format(self.name, self.age))
#
# stu1 = Person('Tom', 120)
# stu1.str()
# print("...................")
# stu2 = Person('Tom', 500)
# stu2.str()


# class A:
#     pass
#
#
# class B(A):
#     def __new__(cls):
#         print("__new__方法被执行")
#         return A.__new__(cls)
#
#     def __init__(self):
#         print("__init__方法被执行")
#
#
# b = B()
# class Str1(str):
#     def __new__(cls, string):
#         self_in_init = super().__new__(cls, string)  # 创建一个实例化对象
#         print(id(self_in_init))
#         return self_in_init
#
#     def __init__(self, string):
#         print(id(self))
#
#
# a = Str1("I love China!")
# print(id(a))

# class Str2(str):  #str是一个不可修改的父类
#     def __new__(cls, stringValue):
#         string = str(stringValue).upper()  #new必须返回一个实例对象
#         return super().__new__(cls,string)  # 返回str构造后的实例对象 → 一个大写的字符串
#
# a = Str2('i love China')
# print(a)   # a此时是一个大写的字符串（实例对象）

# class FileObject(object):
#     def __init(self, filename = "a.txt"):
#         self.f= open(filename, "w+")
#
#     def __del(self):
#         self.f = close()
#         del f
# a=FileObject()

# class Nint(int):
#     def __new__(cls, arg=0):
#         if isinstance(arg, str):
#             total = 0
#             for i in arg:
#                 total+=ord(i)
#             arg = total
#         return int.__new__(cls, arg)
#
#
# if __name__ == '__main__':
#     print(Nint(123))
#     print(Nint('a'))
#     # help(ord)
#     # dict(ord())
# class Countlist():
#     def __init__(self, *args):
#         self.values = [x for x in args]
#         self.count = {}.fromkeys(range(len(self.values)))
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem(self, key):
#         self.count[key] += 1
#         return self.values[key]
#
# c1 = Countlist(9, 2, 3, 4, 5)
# c2 = Countlist(8, 2, 3, 4, 5)
#
# print(c1[1])

# x = int('12')  # 创建一个int的对象
# y = int('3')
# print(x+y)    # 相当于对象相加
#
# class New_int(int):
#     def __add__(self, other):
#         return int.__sub__(self, other)
#
#     def __sun__(self, other):
#         return int.__add__(self, other)
#
# a =New_int(4)    # 创建对象
# b =New_int(7)
# print(a+b)
#
# class Rint(int):
#     def __radd__(self, other):
#         return int.__sub__(self, other)
# a = Rint(5)
# b = Rint(6)
#
# print(a+b)   # self=a,other=b a,b都是Rint的对象 可以找到--add__()
# print(1+b)   # 找不到1对象的加法 调用b的反运算 self=b,other=1
# print(b+1)   #self=b ,other=1 可以找到b对象的加法

# # 列表的迭代
# list = [12, 35, 67, 89]
# for i in list:
#     print(i, end=' ')
# print("\n")
# #字典的迭代
# dict1 ={"lmf": "1", "cym": "2", "czh": "3"}
# for i in dict1:         # 迭代的是键
#     print(i, dict1[i])
# str = "wlytlj"
# a = iter(str)    # iter获取迭代器对象返回给 a
# while True:
#     try:
#         i = next(a)
#     except StopIteration:  # 没有next以后抛出stopIteration异常 捕捉异常 结束死循环
#         break
#     print(i)

# class Fib():
#     def __init__(self, n= 10):
#         self.a = 0
#         self.b = 1
#         self.n = n
#
#     def __iter__(self):
#         print("iter...")
#         return self
#     def __next__(self):
#         print("next...", end=" ")
#         self.a, self.b = self.b, self.a+self.b
#         if self.a >self.n:
#             raise StopIteration    # 抛出异常
#
#         return self.a
#
# fib = Fib()
# for i in fib:
#    print(i)

# class Gen():
#     print("生产器被执行")
#     yield 1  # 和return 类似但是在这里仅仅是暂停，返回参数后继续执行
#     yield 2
#
# my = Gen()
# print(next(my))

#列表推导式  40以内 可以被2 整除，不能被3整除的数字
list = [i for i in range(100) if not(i % 2) and (i % 3)]
print(list)

#字典推导式 10以内被2 整除的情况
dic = {i : (i %2) == 0 for i in range(10)}
print(dic)

#集合推导式 找出一个列表里可以被2整除的数字，组成一个集合
myset = {i for i in [1,3,2,1,2,6,5,3,4,1,2,3] if (i % 2) == 0}

#元组 生成器推导式
tup = (i for i in range(10) if i%2)
print(tup)
print('\n', sum(i for i in range(10) if i % 2))   #将生成器对象作为函数参数
#读取生成器
for i in tup:
    print(i, end=' ')


