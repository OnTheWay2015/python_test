
#------------- 
import numpy as np
import matplotlib.pyplot as plt


#------------- 
def test_numpy():
    #numpy.zeros(shape, dtype = float, order = 'C')
    #numpy.ones(shape, dtype = None, order = 'C')  #创建指定形状的数组，数组元素以 1 来填充
    #-----------------------------------------------
    # 设置类型为整数
    y = np.zeros((5,), dtype = np.int)  #一维数组
    print(y)
    # 自定义类型
    z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4'),('a','i4')])  
    print(z)
    #-----------------------------------------------
    #从已有的数组创建数组
    #numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个。
    a = [2,4,6] 
    np.asarray(a, dtype = None, order = None)
    print(a)
    #-----------------------------------------------
    #从数值范围创建数组
    #numpy.arange(start, stop, step, dtype) #创建数值范围并返回 ndarray 对象
    #numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) #函数用于创建一个一维数组，数组是一个等差数列构成的
    
    #-----------------------------------------------

def test_line():
    x = np.arange(1,11)
    print(x) 
    y =  2  * x +  5 
    print(y) 
    plt.title("Matplotlib demo") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    plt.plot(x,y) 
    plt.show()

def test_sin():
    x = np.linspace(0, 2*np.pi)
    print(x)
    y_sin = np.sin(x)
    print(y_sin)
    #y_cos = np.cos(x)
    plt.plot(x, y_sin)
    plt.show()

def test_sin_cos():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X,C)
    plt.plot(X,S)

    plt.show()
    
    """ 
    Matplotlib is currently using agg, which is a non-GUI backend, 
    so cannot show the figure.意思是：“Matplotlib 现在用的是 agg，这是一个非图形界面的后端（backend），因此不能显示图形”
    安装 python时,要选中带gui
    """ 

def test_def():
    #1.1 Figure 在任何绘图之前，我们需要一个Figure对象，可以理解成我们需要一张画板才能开始绘图。
    fig = plt.figure() #画板

    #1.2 Axes 在拥有Figure对象之后，在作画前我们还需要轴，没有轴的话就没有绘图基准，所以需要添加Axes。也可以理解成为真正可以作画的纸。
    ax1 = fig.add_subplot(111)  #画板划成1*1,1份.在画板的第1行第1列的第一个位置生成一个Axes对象来准备作画
    #ax = fig.add_subplot(1,1,1) #参数等价上面 (111)
    ax2 = fig.add_subplot(221)  #画板划成2*2,4份.在画板的第2行第2列的第一个位置生成一个Axes对象来准备作画
    
    ax1.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
           ylabel='Y-Axis', xlabel='X-Axis') #设置坐标系参数

    ax2.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
           ylabel='Y-Axis', xlabel='X-Axis') #设置坐标系参数

    x = np.linspace(0, 4, 30) #创建显示数据
    print(x)
    print(x.__len__())
    y = x
    
    ax1.plot(x,y) #设置显示数据 x轴,y轴
    ax2.plot(x,y) #设置显示数据 x轴,y轴
    plt.show()


def test_def_mul():
    #1.3 Multiple Axes 可以发现我们上面添加 Axes 似乎有点弱鸡，所以提供了下面的方式一次性生成所有 Axes
    fig, axes = plt.subplots(nrows=2, ncols=2)
    axes[0,0].set(title='Upper Left')
    axes[0,1].set(title='Upper Right')
    axes[1,0].set(title='Lower Left')
    axes[1,1].set(title='Lower Right')

    x = np.linspace(0, 4, 30) #创建显示数据
    print(x)
    print(x.__len__())
    y = x
    
    axes[0,0].plot(x,y) #设置显示数据 x轴,y轴
    plt.show() 

def f_matplot_main():
    print("f_matplot_main act!")
    test_def_mul()
    #test_def()
    #test_numpy()
    #test_line()
    #test_sin()
