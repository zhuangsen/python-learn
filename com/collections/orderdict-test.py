#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import OrderedDict
user_dict = OrderedDict()
user_dict["b"] = "madison1"
user_dict["a"] = "madison2"
user_dict["c"] = "madison3"

# print(user_dict.popitem())
print(user_dict.move_to_end("b"))
print(user_dict)
