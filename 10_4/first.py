# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 0031 23:07
# @Author  : GXl
# @File    : name_function.py
# @Software: PyCharm
# 课时一 储存数据
# 使用json.dump()和json.load()
# 方式一用dump
# import json
# numbers=[2,3,4,5,6,7]
# filename='numbers.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)

import json
filename='numbers.json'
with open(filename) as f:
    numbers=json.load(f)
print(numbers)