# -*- coding:utf-8 -*-

#1.使用input获取信息
name = raw_input("请输入您的名字：")
sex = raw_input("请输入您的性别：")
moblie = input("请输入您的手机号码：")
qq = input("请输入您的qq号：")
job = raw_input("请输入您的职业：")

#2.使用print打印名片
    #在print后面添加一个 逗号，即可不换行输出
    # print("=================================")
    # print("名字：%s"%name),
    # print("性别：%s"%sex),
    # print("手机号码：%d"%moblie),
    # print("qq号：%s"%qq),
    # print("职业：%s"%job)
    # print("=================================")

print("=================================")
print("名字："+name)
print("性别："+sex)
print("手机号码：%d"%moblie)
print("qq号：%d"%qq)
print("职业："+job)
print("=================================")