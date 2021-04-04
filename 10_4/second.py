# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 0001 0:08
# @Author  : GXl
# @File    : second.py
# @Software: PyCharm
# import json
# username=input("What is your name?")
# filename='username.json'
# with open(filename,'w') as f:
#     json.dump(username,f)
#     print(f"'We'll remember you when you come back,{username}'")
# import json
# filename='username.json'
# with open(filename) as f:
#     username=json.load(f)
#     print(f"Welcome back,{username}")
import json
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We'll remember you name when you come back,{username}")
else:
    print(f"Welcome back,{username}")