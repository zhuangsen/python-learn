#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

users = ["madison1", "madison2", "madison3", "madison1"]
user_counter = Counter(users)
user_counter = Counter("asdfasdaaaa")
user_counter.update("sdgas")

print(user_counter.most_common(2))
print(user_counter)

