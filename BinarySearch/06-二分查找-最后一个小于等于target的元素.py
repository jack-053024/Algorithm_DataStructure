#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 21:33
# @Author  : Jack
def binary_search(alist, target):
    """
    数据有重复值，查找出最后一个小于等于 target 的元素，返回下标，若不存在，返回 -1
    Difficulty: easy
    :param alist: 给定有序数组
    :param target: 给定的目标值
    :return: 目标值在数组中的下标，如果不存在则返回 -1
    """
    low = 0                         # 定义两个指针，low 和 high，分别指向第一个和最后一个元素
    high = len(alist) - 1
    while low <= high:              # 当 low <= high 时，所以数组还没查找完毕
        mid = low + ((high - low) >> 1)
        if alist[mid] <= target:
            """继续判断 mid 是否为数组的 last elem，if true, return mid, if not,
            judge whether the next elem of the mid is less than or equal to the target，
            if not, the alist[mid] is the last elem less than or equal to the target,
            otherwise, not the last, should adjust the search range."""
            if mid == (len(alist) - 1) or alist[mid+1] > target:
                return mid
            else:
                low = mid + 1
        else:                       # if alist[mid] > target
            high = mid - 1
    return -1

"""analyse
该题为简单二分查找的变体形式，即数组中存在重复元素，要找出最后一个大于等于 target 的元素；
时间复杂度还是 O(logn)，重点在于当 alist[mid] <= target 时，要进一步判断是否是数组中的最后一个。
"""


if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5, 6, 8, 8, 8, 11, 18]
    print(binary_search(alist, 8))
    print(binary_search(alist, 19))