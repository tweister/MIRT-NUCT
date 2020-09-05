import Init_MIRT
import Show_L
import MIRT_DSY
import MCMC
import time


def main():
    while True:
        print("""
        指令列表如下：
        1.查看不同题目作答组合的L曲线
        2.对题目作答进行DSY算法估计
        3.对题目作答进行MCMC算法估计
        4.导入xls类型的作答结果并对其进行分析和处理
        0.退出
        """)
        command = input('请输入需要执行的指令')
        a, b = Init_MIRT.Init_a_b()
        if command == '0':
            print('感谢您的使用')
            break
        elif command == '1':
            time_star=time.time()
            Show_L.m_show(a, b)
            time_end=time.time()
            print("程序运行时间：%.8s s" %(time_end-time_star))
        elif command == '2':
            time_star = time.time()
            MIRT_DSY.DSY(a, b)
            time_end = time.time()
            print("程序运行时间：%.8s s" % (time_end-time_star))
        elif command == '3':
            time_star = time.time()
            MCMC.MCMC(a,b)
            time_end = time.time()
            print("程序运行时间：%.8s s" % (time_end-time_star))
        elif command == '4':
            print("""
            请输入需要处理的文件位置         
            """)
            while True:
                URL=input()
                if URL=='':
                    print("请输入有效地址")
                else:
                    print('测试完成，本功能还在开发中')
                    break
        print('finish')
        KEY=input('继续执行请按1，停止执行请按0')
        if (KEY!='1'):
            break


if __name__ == "__main__":
    main()
