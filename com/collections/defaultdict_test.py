#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import defaultdict

user_dict = {}
users = ["madison1", "madison2", "madison3", "madison1", "madison1", "madison2"]
user_dict = defaultdict(int)
for user in users:
    # user_dict.setdefault(user, 0)
    # if user not in user_dict:
    #     user_dict[user] = 1
    # else:
    user_dict[user] += 1


print(user_dict)

# default_dict = defaultdict(int)


def gen_default():
    return {
        "name": "",
        "nums": 0
    }

group_dict = {
    "group1": {
        "name": "",
        "nums": 0
    }
}
default_dict = defaultdict(gen_default)
default_dict["group1"]

# default_dict["madison"]
pass
