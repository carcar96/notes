# -*- coding:utf-8 -*-
# age = input("您的年龄为：")
age = int(raw_input("您的年龄为："))
if age>0 and age<18:
    print("少年")
elif age>=18 and age<=35:
    print("青年")
elif age>35 and age<=65:
    print("中年")
elif age>65 and age<=150:
    print("老年")
else:
    print("输入范围：1-150")