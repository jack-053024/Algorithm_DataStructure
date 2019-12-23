#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 21:29
# @Author  : Jack
def _heapify(alist, ind_last, i):
    """
    从某个节点开始，自上而下进行堆化
    :param alist: 节点所在的数组
    :param ind_last: 数组的最后一个元素
    :param i: 当前要堆化的节点
    :return: 某个节点堆化好的数组
    """
    while True:
        max_pos = i
        if 2 * i + 1 <= ind_last and alist[2*i+1] > alist[max_pos]:
            max_pos = 2 * i + 1
        if 2 * i + 2 <= ind_last and alist[2*i+2] > alist[max_pos]:
            max_pos = 2 * i + 2
        if max_pos == i: break
        alist[i], alist[max_pos] = alist[max_pos], alist[i]
        i = max_pos


def _build_heap(alist):
    """
    build a big top heap for the data
    :param data: to be built
    :return: a heap
    """
    # 1. 从数组的最后一个非叶子节点开始向前遍历节点，分别进行堆化
    # 1.1 获取数组最后一个元素的下标
    ind_last = len(alist) - 1
    # 1.2 获得最后一个非叶子节点的下标
    ind_cur = (ind_last - 1) >> 1
    # 1.3 开始遍历
    for cur in range(ind_cur, -1, -1):
        _heapify(alist, ind_last, cur)
    return alist

def _sort(heap):
    """
    给一个已建好的大顶堆进行排序
    :param heap:
    :return: an ordered list
    """
    # 1. 交换堆顶元素与最后一个元素
    ind_last = len(heap) - 1
    while ind_last > 0:
        heap[0], heap[ind_last] = heap[ind_last], heap[0]
        ind_last -= 1
        # 2. 从堆顶自上由下堆化
        _heapify(heap, ind_last, 0)
    return heap



def heap_sort(alist):
    """
    heap sorting, 对给定的数据进行堆排序, the data must be a list
    :param data: data to be sorted
    :return: none
    """
    # 1. build heap: the process of heapify
    heap = _build_heap(alist)
    # 2. sorting
    return _sort(heap)


if __name__ == "__main__":
    alist = [54,226,93,17,77,31,44,55,20]
    print(alist)
    print(heap_sort(alist))

