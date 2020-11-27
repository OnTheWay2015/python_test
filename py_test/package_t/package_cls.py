#coding:utf-8
class package_cls_t:
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


def package_fun_act():
    print("package_cls package_fun_act!")