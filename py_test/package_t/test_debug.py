#coding:utf-8

import sys
import traceback

def func1():
    raise NameError("--traceback exception--")


def d_traceback():
    try:
        func1()
    except Exception as e:
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        traceback.print_exception(exc_type, exc_value,exc_traceback_obj)


def f_test_debug():
    print("%s---%s"%(1,2))
    d_traceback()




