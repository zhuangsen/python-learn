#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import ChainMap

user_dic1 = {"a": "madison1", "b": "madison2"}
user_dic2 = {"b": "madison4", "d": "madison3"}

for key, value in user_dic1.items():
    print(key, value)

for key, value in user_dic2.items():
    print(key, value)


print("-------------")
user_dic = ChainMap(user_dic1, user_dic2)
# user_dic = user_dic.new_child({"aa": "aa", "bb": "bb"})
for key, value in user_dic.items():
    print(key, value)

print("--------------")
print(user_dic.maps)
user_dic.maps[0]["a"] = "madison"
for key, value in user_dic.items():
    print(key, value)