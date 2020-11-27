#coding:utf-8

# --------- from 
#from cls_t import cls,fun_act,d_traceback #引入同目录下的文件，from 后面跟文件名
#from package_t import test_debug  #引入 package_t 目录的 test_debuy 文件
#from package_t.test_debug import f_test_debug #引入 package_t 目录 test_debuy 文件 的 f_test_debug 方法


# --------- import 
import cls_t #引入同目录下的文件 可直接 import 文件名，此时文件名就是 module 名. cls_t.cls
import package_t #引入目录名



#def ttt():
#    d_traceback()

def main():
    print("main act!")
    #--------------------- import
    #fun_act() 
    #test_debug.f_test_debug()
    #f_test_debug()
    #--------------------- from
    cls_t.f_test_debug()
    package_t.package_cls.package_fun_act() 
    package_t.test_debug.f_test_debug()
    package_t.f_test_type()
    #---------------------

    #xx = cls("1l","22")
    #xx.fun()
    #fun_act()
    #ttt() 

if __name__ == "__main__":
    print("1----")
    main()
else:
    print("2----")


