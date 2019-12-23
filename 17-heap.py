#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 15:18
# @Author  : Jack
class Heap(object):
    """heap and its basic operations"""
    def __init__(self, data=None):
        # data: 给定堆，可能为空，也可为一个有数据的堆。
        if data:
            if type(data) is not list:
                raise Exception("Error: Not a list")
            self._heap = data.insert(0, None)
            self._capacity = len(data)
            self._ind_last = len(data)
        else:
            self._heap = [None] * 20  # cannot create a empty list directly
            self._capacity = 20
            self._ind_last = 0

    def insert(self, item):
        """
        insert an elem at the end of the heap
        :param item: the elem to be inserted
        :return: none
        """
        # 1. judge whether the heap is full
        if self._capacity == self._ind_last:
            raise Exception("heap is full")
        # 2. insert the item
        self._ind_last += 1
        self._heap[self._ind_last] = item
        # 3. heapify, from bottom to top
        i = self._ind_last
        # 3.1 parent node is at most the root and parent node greater than item
        while i // 2 > 0 and self._heap[i//2] < item:
            self._heap[i//2], self._heap[i] = self._heap[i], self._heap[i//2]
            i = i // 2

    def remove_max(self):
        """
        remove the top elem from the heap
        :return: none
        """
        # 1. judge whether the heap is empty
        if self._ind_last == 0: return
        # 2. cover the top elem
        self._heap[1] = self._heap[self._ind_last]
        self._ind_last -= 1
        # 3. heapify from top to bottom
        self._heapify_from_top()

    def _heapify_from_top(self):
        """
        heapify from top to bottom from the root node
        :return: none
        """
        i = 1
        while True:
            max_pos = i  # make a label for the max node
            if i * 2 <= self._ind_last and self._heap[i*2] > self._heap[max_pos]:
                max_pos = i * 2
            if i * 2 + 1 <= self._ind_last and self._heap[i*2+1] > self._heap[max_pos]:
                max_pos = i * 2 + 1
            # if the current node is max, jump out from cycle
            if max_pos == i: break
            self._heap[i], self._heap[max_pos] = self._heap[max_pos], self._heap[i]
            i = max_pos

    @property
    def heap(self):
        return self._heap[1:self._ind_last+1]




if __name__ == "__main__":
    heap = Heap()
    print(heap.heap)



