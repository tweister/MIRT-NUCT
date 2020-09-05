import math
import numpy as np
import Init_MIRT
import random


def Cal_P_θ(a):                 #计算P（θ）：
    PI=math.pi
    P1=math.exp(-math.pow(a,2)/2)
    P2=math.sqrt(2*PI)
    P=P1/P2
    return P

def Judge_transfer(L0,L1,j0,j1):              #判断是否转移，如果转移则返回true，否则则为folse
    N0=Cal_P_θ(j0)
    N1=Cal_P_θ(j1)
    D1=(L1*N1)
    D0=(L0*N0)
    D=D1/D0
    a=min(D,1)
    #print(a)

    u=np.random.uniform(0,1)
    #u=1
    if a<=u:
        s=0
    else:
        s=1
    return s

def MCMC(a,b):  #MCMC迭代程序
    l = int(input('请输入题目个数'))
    print(a)
    print(b)
    N=Init_MIRT.transfer_DEX_to_bin(l)
    Theta=[]
    Save_THETA=[]
    Save_L_new=[]
    Save_L=[]
    Theta_Save_Each_Iterations=[]
    Iterations=[]
    Save_sub=[]
    Save_sub_original=[]
    for d in range(2**l):       #对16种情况进行大历遍循环
        t=N[d]
        L = 1
        step=20000
        K= 0.1                 #历遍初值为0.1
        L = Init_MIRT.Cal_L(a, b, K, t, l)  # 构造L初值
        len, L_each, Lmax, The = Init_MIRT.Show_L(a, b, t)  # 构造L变化图像

        for i in range(step):
            k1=Init_MIRT.random_normal(K)
            Save_THETA.append(k1)       #存储新构建的θ值

            L_New=Init_MIRT.Cal_L(a,b,k1,t,l)#构造新的L值
            print(L)
            Save_L_new.append(L_New)    #存储新构建的L值

            SUB = L_New - L
            Save_sub_original.append(SUB)


            Result=Judge_transfer(L,L_New,K,k1)


            if Result==1:                 #满足条件转移，更新L和θ
                L=L_New
                K=k1
            Save_L.append(L)
            Theta_Save_Each_Iterations.append(K)#存储每次迭代产生的θ
            Iterations.append(i)        #存储迭代次数


        TEHTA_END=K                     #迭代完成后的θ值

        avg = float(np.mean(Theta_Save_Each_Iterations[(step-1000):step]))#生成最终θ
        Theta.append(avg)
        L_END = Init_MIRT.Cal_L(a, b, K, t, l)  # 迭代完成后的L值

        Init_MIRT.Draw_scatter(Save_THETA, Save_L_new, L_END, d + 1, Iterations, Theta_Save_Each_Iterations,
                               Save_sub_original, len, L_each, Lmax, The)  # 绘制图像

        print('第%d种θ值估算已完成' % (d + 1) + ' θ= %f' % avg + ',共进行了%d次估计' % (i + 1))
        print(t)
        print('*********************************************')
        Save_L_new.clear()              #清除记录，准备新的迭代
        Save_THETA.clear()
        Theta_Save_Each_Iterations.clear()
        Iterations.clear()
        Save_sub.clear()
        Save_sub_original.clear()

        #print('本次迭代组合为'+N[d])
    print('全部迭代已完成,全部能力值结果为：')
    for num in range(2**l):
        a=Theta[num]
        print('%.4f'%a)

