#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
#   	支付宝手机号枚举工具
#	 	By：FengPeiYu
print("支付宝手机号枚举工具\nMy Github Url:https://github.com/FengPeiYu")
while True:
    tou3 = str(input("请你输入前面3位号码:"))
    wei2 = str(input("请你输入末尾2位号码:"))
    if len(tou3) ==3 and len(wei2) ==2:
        f = open("PhoneNumber.txt", "w+")
        time1= time.strftime('%Y-%m-%d %H:%M:%S')
        start_time = time.time()
        for i in range(0,10):# 1
            for j in range(0, 10): # 2
                for k in range(0, 10):# 3
                    for l in range(0, 10):# 4
                        for m in range(0, 10):# 5
                            for n in range(0, 10):# 6
                                number = ("{}{}{}{}{}{}{}{}".format(tou3,i, j, k, l,m,n,wei2))
                                # print("正在生成:"+number)   #这个注释掉可以加快生成输入，更具你自己的喜好来决定
                                f.write(number + '\n')
        f.close()
        time2 =time.strftime('%Y-%m-%d %H:%M:%S')
        print("     已全部生成完毕请在脚本目录下查看PhoneNumber.txt文件\n"+"开始时间:",time1,"结束时间:",time2,"共耗时:%5.2f Second"% (time.time() - start_time))
        break
    else:
        print("=======================你的输入有误请在下方重新输入")