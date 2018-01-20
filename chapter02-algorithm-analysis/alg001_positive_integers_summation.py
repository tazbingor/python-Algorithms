#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 下午6:18
# @Author  : Aries
# @Site    : 
# @File    : alg001_positive_integers_summation.py
# @Software: PyCharm
'''
前N个正整数求和的各种实现,

一般使用迭代方式逐步the_sum不断自增,从而很直观的求得结果,但对与计算机来说,n越大,迭代运算的时间也会越长
然而sum_of_n_3也并非绝对高效的算法,倘若运行环境老旧,可能也会消耗更长的时间.所以以上两种解法都受制于运行环境,
所以需要一个不依赖程序或者运行环境的指标. 时间复杂度
'''
import time


def sum_of_n(n):
    '''
    一般情况下的前n个正整数求和
    :param n:
    :return:
    '''
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i
    return the_sum


def foo(tom):
    '''
    蜜汁前N个整数求和
    :param tom:
    :return:
    '''
    fred = 0
    for bilibili in range(1, tom + 1):
        barney = bilibili
        fred = fred + barney

    return fred


def sum_of_n_2(n):
    '''
        一般情况下的前n个正整数求和,并同时计算运算时间
    :param n:
    :return:
    '''
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i
    end = time.time()
    return the_sum, end - start


def sum_of_n_3(n):
    '''
    无迭代求和
    :param n:
    :return:
    '''
    start = time.time()
    return (n * (n + 1)) / 2, time.time() - start


if __name__ == '__main__':
    print(sum_of_n(10))  # 55
    print(foo(10))  # 55

    for i in range(5):
        print('Sum is %d required % 10.7f seconds' % sum_of_n_2(10000))

    # Sum is 50005000 required  0.0010130 seconds
    # Sum is 50005000 required  0.0008521 seconds
    # Sum is 50005000 required  0.0008922 seconds
    # Sum is 50005000 required  0.0011799 seconds
    # Sum is 50005000 required  0.0011282 seconds
    print('-' * 50)

    for i in range(5):
        print('Sum is %d required % 10.7f seconds' % sum_of_n_2(1000000))
    # Sum is 500000500000 required  0.0827148 seconds
    # Sum is 500000500000 required  0.0827019 seconds
    # Sum is 500000500000 required  0.0838501 seconds
    # Sum is 500000500000 required  0.0811579 seconds
    # Sum is 500000500000 required  0.0865130 seconds
    print('-' * 50)

    print('Sum is %d required % 10.7f seconds' % sum_of_n_3(10))
    # Sum is 55 required  0.0000010 seconds

    print('Sum is %d required % 10.7f seconds' % sum_of_n_3(10000))
    # Sum is 50005000 required  0.0000010 seconds

    print('Sum is %d required % 10.7f seconds' % sum_of_n_3(100000))
    # Sum is 5000050000 required  0.0000010 seconds

    print('Sum is %d required % 10.7f seconds' % sum_of_n_3(1000000))
    # Sum is 500000500000 required  0.0000000 seconds
