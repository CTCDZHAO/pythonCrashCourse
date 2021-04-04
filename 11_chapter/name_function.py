# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 0004 20:07
# @Author  : GXl
# @File    : name_function.py
# @Software: PyCharm
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
