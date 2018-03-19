# -*- coding:utf-8 -*-
str = "woshiasddscv"
#获取字符串的第几个
print(str[0])

#获取字符串的最后一个
print(str[-1])
print(str[len(str)-1])

#获取字符串长度
print(len(str))

#字符串切片：获取字符串中的第a个到第b个，但不包括第b个，c是步长（默认1）   str[a:b:c]
print str[2:4]  #sh
print str[2:-1] #shiasddsc
print str[2:]   #shiasddscv
print str[2:-1:2] #sisdc

#字符串倒序
print str[-1::-1]   #vcsddsaihsow
print str[::-1]     #vcsddsaihsow

#查找字符串,返回查找到的第一个目标下标，找不到返回-1
print str.find("s") #2
print str.find("gg") #-1

#统计字符串中，某字符出现的次数
print str.count("s") #3
print str.count("gg") #0

#字符串替换
print str.replace("s","S")  #woShiaSddScv
print str   #不变
print str.replace("s","S",1)  #woShiasddscv
print str.replace("s","S",2)  #woShiaSddscv

#字符串分割
print str.split("s")    #['wo', 'hia', 'dd', 'cv']

#字符串第一个字符大写
print str.capitalize()  #Woshiasddscv

#每个单词首字母大写
str1 = "hah hsauh"
print str1.title()  #Hah Hsauh

#以xx结尾，文件后缀名判断
file = "ancd.txt"
print file.endswith(".txt") #True
print file.endswith(".pdf") #False

#以xx开头
print file.startswith("ancd")   #True
print file.startswith("ancds")  #False

#字符串小写
str2 = "HhnuhHUJHfgt"
print str2.lower()  #hhnuhhujhfgt

#字符串大写
print str2.upper()  #HHNUHHUJHFGT