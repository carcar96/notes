# -*- coding:utf-8 -*-
"""
比较（关系）运算符
    1/  ==
    2/  !=
    3/  <>  等价于!=
    4/  >
    5/  >=
    6/  <
    7/  <=
逻辑运算符
    1/  and（ 如果 a 为 false，a and b 返回 false，否则它返回 b 的计算值）
    2/  or（ 如果 a 是非 0，它返回 a 的值，否则它返回 b 的计算值）
    3/  not 不是某个值或某段范围，返回false或者true
"""
age = 18
print (age==18)
print (age==8)
print(not(age==18)) #false
print(not(age>18))  #true