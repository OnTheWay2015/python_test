#coding:utf-8
"""
---------------------------------------
标准数据类型
    Python3 中有六个标准的数据类型：
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。



---------------------------------------
定义枚举
class Color(Enum):
    red = 1
    green = 2
    red = 3    # TypeError: Attempted to reuse key: 'red'
成员值允许相同，第二个成员的名称被视作第一个成员的别名


class Color(Enum):
    red   = 1
    green = 2
    blue  = 1

print(Color.red)              # Color.red
print(Color(1))               # Color.red  在通过值获取枚举成员时，只能获取到第一个成员

---------------------------------------
字典,元组,序列，集合

字典里不使用等号
obj_dict = { "a":1 } 
for, if ,while和方法定义语句后面有冒号

是否有键值
print obj_dict.has_key('name'); print key in obj_dict.keys();

ttt={"a":0, "b":1}
print( " res:%s" % ("a" in ttt) )
print( " res:%s  with keys()   " % ("a" in ttt.keys()) )


for i in range(5,3,-1):
range 5,3表示 [5,3) 的集合, -1 表示递增或减的值,当增序不对时，不生效
for i in range(5) 等价于 for i in range(0,5,1) 


array
	append

if :
	do somthing
else :
	do somthing
	
条件判断 
	非  if not ... : 
	或 if ... or ... :
	与 if ... and ...:




使用any判断一个对象是否为空
>>> eth = {"eth0″:"192.168.1.1″}
>>> any(eth)
True
>>> eth = {}
>>> any(eth)
False


判断list是否为空
传统的方式：
if len(mylist):
    # Do something with my list
else:
    # The list is empty

由于一个空 list 本身等同于 False，所以可以直接：
if mylist:
    # Do something with my list
else:
    # The list is empty

	
"""

import json
def f_test_type():
    obj_dict = {'ab':123, "abc":321}
    obj_dict["a"] =10
    print( "obj_dict -> %s %s"% (json.dumps(obj_dict), "test") )
    print( json.dumps({'ab':123, "abc":321}))
    print( obj_dict )
    print(obj_dict["ab"])


    str_obj = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    print(str_obj)


    obj_r_ary = (1,2,3,3)
    print(obj_r_ary)

    obj_ary = [6,5,4,4,3]
    print(obj_ary)

    obj_set=set(obj_r_ary)
    print(obj_set)

    obj_set=set(obj_ary)
    print(obj_set)

    """ 遍历  """
    print( dir(obj_dict) )
    for v in obj_dict.values():
        print( "obj_dict-> v[%s]" % (v) )
    for key in obj_dict.keys():
        print( "obj_dict-> key[%s]" % (key) )
    for key,val in obj_dict.items():
        print( "obj_dict-> key[%s] val[%d]" % (key,val) )
    print( dir(obj_r_ary) )
    for i in range(5,13,1):
        print( "x[%d] " % (i))
    for i in range(5):
        print( "i[%d] " % (i))
    for i in range(obj_ary.__len__()):
        print( "i[%d] v[%d]" % (i, obj_ary[i]))
    
    for val in obj_ary:	
        print( "v[%d]" % (val) )