

from smallseg.smallseg import SEG
#from blue_py.blue_a import blue_a


seg = SEG()
#seg = blue_a("")
#seg.act()


def cuttest(text):
    wlist = seg.cut(text)
    wlist.reverse()
    tmp = " ".join(wlist)
    print(tmp) 

cuttest("这是一个伸手不见五指的黑夜我叫孙悟空ggg我爱北京爱Python和C++。")
