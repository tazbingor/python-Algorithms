#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/16 下午7:44
# @Author  : Aries
# @Site    : 
# @File    : exercise_002.py
# @Software: PyCharm
'''
1-2. 很多情况下我们希望分数一开始就能保持最简比.
    请修改Fraction类的构造器,让GCD可以对分数立刻进行约分.
    注意,这意味着__add__函数不再需要执行约分的功能
'''
import fractions

if __name__ == '__main__':
    fractions.Fraction