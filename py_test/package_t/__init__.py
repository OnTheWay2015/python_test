
#coding:utf-8
#from package_cls import cls #引入同目录下的文件，from 后面跟文件名,  import 后面是当前包,可导出的声明,或当前文件可使用的声明
#from test_debug import f_test_debug,d_traceback; 
#from test_type import f_test_type; 

#from package_cls import package_fun_act 

print("act packate_t __init__.py!")

import package_t.package_cls  #导入对应文件名,注意前面要带上完整路径
import package_t.test_debug
import package_t.test_type
from package_t.test_type import f_test_type   #导入单个声明

