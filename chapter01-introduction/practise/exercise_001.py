#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/14 上午12:16
# @Author  : Aries
# @Site    : 
# @File    : exercise_001.py
# @Software: PyCharm
'''
1.执行一个简单方法getNum和getDen,以返回分数的分子和分母
'''

from fractions import Fraction


def getNum(fraction):
    return str(fraction).split('/')[0]


def getDen(fraction):
    return str(fraction).split('/')[1]


if __name__ == '__main__':

    fraction = Fraction(1 / 2)
    print(fraction)  # 1/2
    print(type(fraction))  # <class 'fractions.Fraction'>
    print(getNum(fraction))  # 1
    print(getDen(fraction))  # 2
