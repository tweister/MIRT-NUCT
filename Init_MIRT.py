import math
import matplotlib.pyplot as plt
import numpy as np
import xlrd

def open_excel(file):
    data = xlrd.open_workbook(file)
    print(file + '文件读取成功')
    return data

def Init_bytes(i,num):
    result=[]
    if i!=1:
        s=int(i)-1
        tansf = int(num)
        while s>0:
            t=2**s
            p=tansf//t
            if p==1:
                result.append('1')
                tansf=tansf-t
            else:
                result.append('0')
            s=s-1
            if s==0:
                result.append(str(tansf))
    else:
        result.append('0')
        result.append('1')
    return result

def Init_a_b():
    a = [0.6364, 0.3636, 0.6818, 0.5909, 0.3265, 0.1245, 0.2564]
    b = [0.3133, 0.1566, 0.3012, 0.2289, 0.5546, 0.7112, 0.8456]
    return a,b

def Init_P(a,b,k): #构造函数Pi
    P = 1 / (1 + math.exp(-1.7*a*(k - b)))
    return P

def transfer_DEX_to_bin(i):
    result=[]
    n=int(i)
    for num in range(2**int(n)):
        #print(num)
        trans=Init_bytes(n,num)
        result.append(trans)
    print("%d个题目的转换结果为"%n)
    print(result)
    return result

def random_normal(K):
    K1=np.random.normal(K, 0.2, 1)
    return K1

def Cal_L(a,b,k,t,l):
    L=1
    for n in range(l):  # 构造L初值
        if t[n] == '0':
            P = Init_P(a[n], b[n], k)
            Q = 1 - P
            L = L * Q
        elif t[n] == '1':
            L = L * Init_P(a[n], b[n], k)
    return L

def plt_ax1(fig,n,x,y,y_end):
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_title('The %dth plot L_Last' % n)  # 设置标题名称
    ax1.set_xlabel('θ')         # 设置横坐标名称
    ax1.set_ylabel('L_New')     # 设置纵坐标名称
    ax1.grid(True)              # 显示网格线

    x_line = np.random.uniform(-10, 10, 4000)  # 横坐标x2
    y_line = np.array([y_end] * 4000)  # 纵坐标y2

    ax1.plot(x_line, y_line, c='b', ls='--')
    ax1.scatter(x, y, s=1,c='g',marker=',')

    ax1.text(-3, y_end + 0.01 * y_end, "tehta=%.4f" % x[len(x)-1] + "L_max=%.4f" % y_end,
             fontdict={'size': '8', 'color': 'b'})

def plt_ax2(fig,n,x2,y2):
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_title('The %dth plot θ' % n)  # 设置标题名称
    ax2.set_xlabel('n')     # 设置横坐标名称
    ax2.set_ylabel('θ')     # 设置纵坐标名称
    ax2.grid(True)          # 显示网格线

    ax2.scatter(x2[:100], y2[:100], s=1, c='b', marker=',')

def plt_ax3(fig,n,y,x,y_max,theta):
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_title('The %dth plot Theta'%n)  # 设置标题名称
    ax3.set_xlabel('θ')     # 设置横坐标名称
    ax3.set_ylabel('L')     # 设置纵坐标名称
    ax3.grid(True)          # 显示网格线

    x_line = np.random.uniform(-10, 10, 1000)  # 横坐标x2
    y_line = np.array([y_max] * 1000)  # 纵坐标y2

    ax3.scatter(x, y, s=1, c='g', marker=',')
    ax3.plot(x_line, y_line, c='b', ls='--')
    ax3.text(-3, y_max + 0.01 * y_max, "tehta=%.4f" % theta + "L_max=%.4f" % y_max,
             fontdict={'size': '8', 'color': 'b'})

def plt_ax4(fig,n,x2,SUB):
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.set_title('The %dth plot SUB(ariginal)' % n)  # 设置标题名称
    ax4.set_xlabel('n')  # 设置横坐标名称
    ax4.set_ylabel('SUB')  # 设置纵坐标名称

    ax4.scatter(x2[:300], SUB[:300], s=1, c='r', marker=',')

def Draw_scatter(x,y,y_end,type,iteration,y2,SUB,len,L,Lmax,The,):#绘制散点图
    fig = plt.figure(num=type)
    plt_ax1(fig,type,x,y,y_end)         #ax1绘制L随θ变化图
    plt_ax2(fig,type,iteration,y2)      #ax2绘制θ的变化图
    plt_ax3(fig,type,len,L,Lmax,The)    #ax3绘制L关于θ自身的变化
    plt_ax4(fig,type,iteration, SUB)    #ax4绘制误差变化
    #plt.xlim(xmax=10, xmin=-10)
    plt.show()

def Show_L(a,b,num):
    t=num
    l=len(num)
    s=-10
    d=-s
    step=0.01
    Save_L=[]
    Save_Theta=[]
    while 1:
        s=s+step
        if s>d:
            break
        else:
            L=Cal_L(a,b,s,t,l)
            Save_L.append(L)
            Save_Theta.append(s)
            L_MAX=max(Save_L)
    L_num=Save_L.index(L_MAX)
    Theta=Save_Theta[L_num]
    return Save_L,Save_Theta,L_MAX,Theta

