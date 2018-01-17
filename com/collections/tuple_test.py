#!/usr/bin/python
# -*- coding: UTF-8 -*-

name_tuple = ("madison1", "madison2")
# name_tuple[0] = "madison3"

user_tuple = ("madison", 29, 175)
name, age, height = user_tuple
name, *other = user_tuple

print(name, age, height)
print(name, other)


name_tuple = ("madison", [29, 175])
name_tuple[1].append(22)
print(name_tuple)


name_list = ['madison1', 'madison2']
for name in name_list:
    print(name)


user_info_dict = {}
user_info_dict[user_tuple] = "madison"
print(user_info_dict)





class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User(name="madison", age=29)
print(user.name, user.age)

pass
