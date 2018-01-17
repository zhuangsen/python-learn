#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import deque


user_list = ["madison", "madison1"]
user_name = user_list.pop()
print(user_name, user_list)


user_list = deque(["madison", "madison2"])
print(user_list)


user_list = deque({
    "madison": 27,
    "madison2": 22
})
print(user_list)

# 最好保持相同类型的数据，保持良好的编程习惯
user_list = deque(["madison", 22, 175])
user_tuple = ("madison1", 22, 175)
user_list.append(user_tuple)
print(user_list)


# deque GIL是线程安全的，List不是线程安全的

# user_deque = deque(["madison1", ["madison2", "madison3"], "madison3"])
user_deque = deque(["madison1", "madison2", "madison3"])
# user_deque.append("madison4")
# user_deque.appendleft("madison5")
# user_deque.clear()
# 浅拷贝
# user_deque2 = user_deque.copy()
# user_deque2[1] = "madison4"
# user_deque2[1].append("madison4")

# 深拷贝
# import copy
# user_deque2 = copy.deepcopy(user_deque)


user_deque2 = deque(["madison1", "madison2", "madison3"])
# 就当前元素进行修改
user_deque.extend(user_deque2)
user_deque2.insert(0, "ella")
user_deque2.reverse()

print(id(user_deque), id(user_deque2))
print(user_deque)
print(user_deque2)
print(user_deque2[1])
