# -- coding: utf-8 --
# @Time : 2023-02-10 15:01
# @Author : zhangwen
# @File : test.py

# class Person:
#
#
#     def __init__(self,name,gender,age):
#         self.name = name      #实例变量
#         self.gender = gender  #实例变量
#         age = age  #局部变量
#
#     def get_name(self):   #实例方法，必须要实例化
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# xiaoli = Person("小李","Male",18)
#
# print(xiaoli.get_name())   #用实例对象来调用实例方法
#
def test(a,b,c,main,secondary):
    if (a>=2.1) +(b>=2.1) +(c>=2.1)>=2:
        n = 0
        list = []
        for i in (a,b,c):
            n=n+1
            if i>2:
                list.append(n)
        if main in list and secondary in list:
            print(main, secondary)
        else:
            print("不能选择主推次推")

test(1,3,3,3,2)






