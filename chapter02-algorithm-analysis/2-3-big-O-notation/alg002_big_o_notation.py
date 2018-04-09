#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 下午8:36
# @Author  : Aries
# @Site    : 
# @File    : alg002_big_o_notation.py
# @Software: PyCharm
'''
大O表示法
'''
fbbs = []
for fbb in range(1, 999):
    fbbs.append(fbb)

print(fbbs)
zx = min(fbbs)
zd = max(fbbs)
print(zx, '-', zd)
