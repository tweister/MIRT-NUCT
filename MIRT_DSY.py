import Init_MIRT

def DSY(a,b):  #DSY迭代程序
    l=int(input('请输入题目个数'))
    print(a)
    print(b)
    N=Init_MIRT.transfer_DEX_to_bin(l)
    Theta=[]
    Save_THETA=[]
    Save_L_new=[]
    Theta_Save_Each_Iterations=[]
    Iterations=[]
    Save_sub_original=[]

    for d in range(2**l):       #对16种情况进行大历遍循环
        t=N[d]
        K= 0.1                 #历遍初值为0.1

        L=Init_MIRT.Cal_L(a,b,K,t,l)#构造L初值
        len, L_each, Lmax, The=Init_MIRT.Show_L(a,b,t)#构造L变化图像

        for i in range(500):
            k1=Init_MIRT.random_normal(K)
            Save_THETA.append(k1)       #存储新构建的θ值

            L_New=Init_MIRT.Cal_L(a,b,k1,t,l)#构造新的L值

            Save_L_new.append(L_New)    #存储新构建的L值
            SUB = L_New - L

            Save_sub_original.append(SUB)
            if L_New>L:                 #满足条件转移，更新L和θ
                L=L_New
                K=k1
            Theta_Save_Each_Iterations.append(K)#存储每次迭代产生的θ
            Iterations.append(i)        #存储迭代次数
            # if abs(SUB)<0.001:
            #      print('误差满足，停止迭代')
            #      break

        L_END=L                          #迭代完成后的L值
        TEHTA_END=K                     #迭代完成后的θ值
        Theta.append(K)                 #装载最终的结果
        #Init_MIRT.Draw_scatter(Save_THETA,Save_L_new,L_END,d+1,Iterations,Theta_Save_Each_Iterations,Save_sub_original,len, L_each, Lmax, The)#绘制图像
        print('第%d种θ值估算已完成'%(d+1)+' θ= %f'%K+',共进行了%d次估计'%(i+1))
        print(t)
        print('*********************************************')
        Save_L_new.clear()              #清除记录，准备新的迭代
        Save_THETA.clear()
        Theta_Save_Each_Iterations.clear()
        Iterations.clear()

        Save_sub_original.clear()

        #print('本次迭代组合为'+N[d])
    print('全部迭代已完成,全部能力值结果为：')
    for num in range(2**l):
        a=Theta[num]
        print('%.4f'%a)


