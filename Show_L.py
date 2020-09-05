import matplotlib.pyplot as plt
import numpy as np
import Init_MIRT

def show(x,y,t,y_max,theta):
    fig = plt.figure(1)
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_title('The '+t+' plot Theta' )  # 设置标题名称
    ax1.set_xlabel('θ')  # 设置横坐标名称
    ax1.set_ylabel('L')  # 设置纵坐标名称
    plt.grid(True)  # 显示网格线

    x_line = np.random.uniform(-10, 10, 1000)  # 横坐标x2
    y_line = np.array([y_max] * 1000)  # 纵坐标y2

    ax1.scatter(x, y, s=1, c='g', marker=',')
    ax1.plot(x_line, y_line, c='b', ls='--')
    plt.text(-3, y_max+0.01*y_max, "tehta=%.4f"%theta+"L_max=%.4f"%y_max, fontdict={'size': '16', 'color': 'b'})
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
            L=Init_MIRT.Cal_L(a,b,s,t,l)
            Save_L.append(L)
            Save_Theta.append(s)
            L_MAX=max(Save_L)
    L_num=Save_L.index(L_MAX)
    Theta=Save_Theta[L_num]
    show(Save_Theta,Save_L,t,L_MAX,Theta)
    Save_L.clear()
    Save_Theta.clear()
    print('绘制完成')

def m_show(a,b):
    while 1:
        num=input("""
        请输入想要查看的组合型号，输入s退出:
        
        """)
        plt.close('all')
        if num=='s':
            break
        else:
            Show_L(a,b,num)
            print('绘制完成')

