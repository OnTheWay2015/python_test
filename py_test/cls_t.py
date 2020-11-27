#coding:utf-8

class cls:
    name=""
    #类的私有属性 两个下横线开头
    __name_p=""
    #构造方法, 初始化属性时，不要忘了 self.
    def __init__(self,n,np):
        self.name = n
        self.__name_p=np
    def __del__(self):
        print("__del__")
    def fun(self):
        self.__fun_s()
        print("fun act!")
    #类的私有方法 两个下横线开头
    def __fun_s(self):
        print("__fun_s act!")


def fun_act():
    print("fun_act!")


import sys
import traceback

def func1():
    raise NameError("--traceback exception--")


def d_traceback():
    print("d_traceback")
    #try:
    #  1/0
    #except Exception, e:
    #  #traceback.print_exc()
    #  exc_type, exc_value, exc_traceback_obj = sys.exc_info()
    #  #traceback.print_tb(exc_traceback_obj)
    #  print(exc_traceback_obj)
    #try:
    #    func1()
    #except Exception as e:
    #    exc_type, exc_value, exc_traceback_obj = sys.exc_info()
    #    traceback.print_exception(exc_type, exc_value,exc_traceback_obj)


def f_test_debug():
    print("cls_t f_test_debug act!")




