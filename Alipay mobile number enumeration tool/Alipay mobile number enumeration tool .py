#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time

#支付宝手机号枚举工具
#	By FengPeiYu
# 	phonenumber= 186******17
f = open("PhpNumber.txt", "w+")
time1= time.strftime('%Y-%m-%d %H:%M:%S')
start_time = time.time()
for i in range(0,10):# 1
    for j in range(0, 10): # 2
        for k in range(0, 10):# 3
            for l in range(0, 10):# 4
                for m in range(0, 10):# 5
                    for n in range(0, 10):# 6
                        number = ("186{}{}{}{}{}{}17".format(i, j, k, l,m,n))
                        f.write(number + '\n')
f.close()
time2 =time.strftime('%Y-%m-%d %H:%M:%S')
print("Starting time:\n",time1,"\nEnd Time:\n",time2,"\nTime consuming:\n%5.2f Second"% (time.time() - start_time))