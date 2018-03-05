# -*- coding:utf-8 -*-

# 导入 random(随机数) 模块
import random

#   1.random.randint(a,b)
#       返回指定范围的一个随机整数，包含上限a和下限b
print random.randint(0,2)

#   2.random.seed(int)
#       给随机数对象一个种子值，用于产生随机序列。
#       对于同一个种子值的输入，之后产生的随机数序列也一样。
#       通常是把时间秒数等变化值作为种子值，达到每次运行产生的随机系列都不一样
#       seed() 省略参数，意味着使用当前系统时间生成随机数
# random.seed(1)#0.134364244112
# random.seed(2)#0.956034271889
# random.seed(3)#0.237964627092
# random.seed(4)#0.236048089737
# random.seed(5)#0.62290169489
print random.random() #0.717435442568
# random.seed(10)
# print random.random()   #0.57140259469  同一个种子值，产生的随机数相同
# print random.random()   #0.428889054675
#   3. random.uniform(u,sigma)
#       随机正态浮点数
print random.uniform(1,5) #3.21561360405

#   4.random.randrange(start,stop,step)
#       按步长随机在上下限范围内取一个随机数
print random.randrange(20,100,5)

#   5. random.random()
#       随机浮点数
print random.random()#0.821716538852

#   6.random.shuffle()
#       对list列表随机打乱顺序，也就是洗牌
#       shuffle只作用于list，对str会报错比如‘abcdfed’,而['1','2','3','5','6','7']可以
item = ['1','2','3','5','6','7']
print item  #['1', '2', '3', '5', '6', '7']
random.shuffle(item)
print item  #['1', '2', '6', '7', '5', '3']

#   7. 随机选择字符
#   (1)random.choice(str)
#        随机选择一位字符,以字符串形式返回 'h'
#   (2)random.sample(str,n)
#        随机选择几位字符,以数组形式返回 ['b', 'o', 'a']

str = "abcn bosdh"
print random.choice(str)    #'c'
print random.sample(str,3)  #['h', 'b', 'c']

#将获取到的随机字符串数组拼接成新字符串
tarArr = random.sample(str,4)
print "".join(tarArr)   #"ds o"
print "".join(tarArr).replace(" ","")   #replace在这里用于去掉空格   "dso"