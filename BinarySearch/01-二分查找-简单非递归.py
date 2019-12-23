#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 12:13
# @Author  : Jack
def binary_search(alist, target):
    """
    alist有序，alist 数组中没有重复元素，用简单的二分查找确定 target 是否在数组中，
    如果在，返回下标，如果不在，返回 -1。
    用非递归的形式实现。
    Difficulty: easy
    :param alist: 有序数组
    :param target: 待查找的元素
    :return: 如果不在，返回 -1，如果在，返回结果下标
    """
    alist_len = len(alist)         # 先求出数组长度
    low = 0                        # 定义两个初始指针，分别指向第一个元素和最后一个元素
    high = alist_len - 1
    while low <= high:             # 当 low <= high 时，注意要 =
        mid = low + ((high - low) >> 1)  # mid 的最优写法，通用且位操作效率更快，
        if alist[mid] == target:
            return mid
        elif alist[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
"""analyse:
time complexity is O(logn)
"""


if __name__ == "__main__":
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search(alist, 3))
    print(binary_search(alist, 13))


