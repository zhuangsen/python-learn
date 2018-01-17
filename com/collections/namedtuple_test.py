#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import namedtuple

User = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple = ("madison", 26, 175)
# user_tuple = ("madison", 26, 175, "IT")
user_list = ["madison", 26, 175, "IT"]

user_dict = {
    "name": "madison",
    "age": 29,
    "height": 175,
    "edu": "master"
}
user = User(*user_tuple, edu="IT")
# user = User(*user_dict, edu="IT")
name, age, *other = user
user_info_dict = user._asdict()

# 灵活性不高
# user = User._make(user_tuple)
# user = User._make(user_list)
# user = User._make(user_list)
# user = User(name="madison", age=29, height=175, edu="IT")
# user.edu = "master"
print(user.name, user.age, user.height, user.edu)

# class Userprofile(models.Mode):
#     name = models.Cahrfiles()

# User 表的数据全部取出然后加一个列


# 函数参数
def ask(*args, **kwargs):
    pass

ask("madison", 12, 19)
