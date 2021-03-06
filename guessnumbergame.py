#！/usr/bin/env python
# -*-coding:utf-8 -*-

# 【项目二】高级猜数字
# 制作交互性强、容错率高的猜数字游戏程序。
# 要求：
# 为猜数字游戏增加记录玩家成绩的功能，包括玩家用户名、玩的次数和平均猜中的轮数、历史的最好成绩等；
# 如果记录里没有玩家输入的用户名，就新建一条记录，否则在原有记录上更新数据；
# 对玩家输入做检测，判定输入的有效性，并保证程序不会因异常输入而出错；
# 将游戏打包为 exe 文件。（可选）
#思路：
#文件记录三个变量：玩家姓名，玩的总次数，玩的总轮数，平均猜中的轮数,历史最好成绩
# #打开文件，如果玩家存在，读取玩家原先的游戏次数，总轮数
#           如果玩家不存在，创建玩家姓名
#           开始游戏
#           游戏结束，保存玩家游戏次数（原游戏次数+本次游戏次数），总轮数（原轮数+本次轮数），历史最好成绩
# 关闭文件
#用到的知识点：输入输出，循环（循环内添加变量），条件判断
#盲点:如何对输入有效性做检测，打包exe文件
#盲点:如何进行文件处理，记录数据，更新数据

import os
if os.path.exists("gameplayer record.txt"):
    pass
else:
    with open("gameplayer record.txt",mode="w",encoding="utf-8") as f:
        f.write("name,0,0,0,0")
        f.close()
name=input("请输入你的玩家ID吧：")
f=open("gameplayer record.txt","r+")
lines=f.readlines()
scores={}
f.close()
print(scores)
for l in lines:
    s=l.split()
    scores[s[0]]=s[1:]
score=scores.get(name)
print(score)
if score==None:
    score=[0,0,0,0]
else:
    score = scores.get(name)
import random
total_times=int(score[0])
times=float(score[1])
best_times=float(score[3])
if best_times!=0:
    average_times = times / total_times
    print("%s,你好，你已经玩了%d次，平均%.2f轮猜中一次,最快%.2f轮猜中" % (name, total_times, average_times,best_times))
else:
    average_times=0
    print("%s,你好，这是你首次玩本游戏"%(name))
while True:
    times2 = 0
    choice = input("1:开始游戏 2：退出游戏\n")
    if choice=="1":
        print("%s,下面请你猜一个1-10之间的数字"%(name))
        real_number = random.randint(1, 10)
        while True:
            number = input("猜猜我是几")
            b=number.isdigit()
            if  b==True:
                number=int(number)
                times=times+1
                times2=times2+1
                if number<real_number:
                    print("你猜的太小了")
                elif number>real_number:
                    print("你猜的太大了")
                else:
                    print("你猜对了")
                    break
            else:
                print("你的输入有错误，请输入数字")
        total_times=total_times+1
        average_times=float(times/total_times)
        if best_times==0 or best_times>=times2:
            best_times=times2
            print("%s,你一共玩了%d次，平均%.2f轮猜中一次,最快%.2f轮猜中"%(name,total_times,average_times,best_times))
        else:
            print("%s,你一共玩了%d次，平均%.2f轮猜中一次,最快%.2f轮猜中" % (name, total_times, average_times, best_times))
    else:
        print("%s,我们下回见"%(name))
        break
scores[name]=[str(total_times),str(times),str(average_times),str(best_times)]
result=""
for n in scores:
    lines=n+" "+" ".join(scores[n])+"\n"
    result+=lines
print(result)
f=open("gameplayer record.txt","w+")
f.write(result)
f.close()
