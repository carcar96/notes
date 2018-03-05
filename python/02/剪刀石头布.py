# -*- coding:utf-8 -*-

#设定：
#   0：剪刀  1：石头  2：布

#1、电脑随机出一个姿势：

# 导入 random(随机数) 模块
import random
randomNum = random.randint(0,2)

#2、用户输入一个手势
userNum = input("请输入手势代号：(0：剪刀  1：石头  2：布)")

#3、校验输入
if isinstance(userNum,int) and abs(userNum)<3:
    # 4、判断输赢
    if userNum > randomNum:
        print("恭喜您赢了！")
    elif userNum == randomNum:
        print("平局！再来一次！")
    else:
        print("您输了！呜呜")
else:
    print("姿势不对！您输错啦")