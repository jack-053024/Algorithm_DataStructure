#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 14:41
# @Author  : Jack
def binary_search(alist, low, high, target):
    """
    alist有序，alist 数组中没有重复元素，用简单的二分查找确定 target 是否在数组中，
    如果在，返回下标，如果不在，返回 -1。
    用递归的形式实现。
    Difficulty: easy
    :param alist: 有序数组
    :param target: 待查找的元素
    :return: 如果不在，返回 -1，如果在，返回结果下标
    """
    if low > high:          # 递归终止条件，当 low > high 时，说明查询完毕，且没有找到元素
        return -1
    mid = low + ((high - low) >> 1)
    if alist[mid] == target:
        return mid
    elif alist[mid] < target:
        return binary_search(alist, mid+1, high, target)
    else:
        return binary_search(alist, low, mid-1, target)

"""analyse
原地查找，使用了双指针；time complexity is O(logn)；
相比非递归，两者基本差不多，虽然递归需要调用系统栈，但由于二分查找的次数很少，
所以哪怕规模很大的数据，也基本不会出现栈溢出；
需要注意的是，递归终止的条件；
非递归写法，相对复杂，但还是比递归效率更高，所以之后的写法，大都用非递归写法。
"""


if __name__ == "__main__":
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search(alist, 0, len(alist)-1, 3))
    print(binary_search(alist, 0, len(alist)-1, 13))

