#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:40
# @Author  : Jack
class Node(object):
    """node"""
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BinarySearchTree(object):
    """binary search tree"""
    def __init__(self, node=None):
        self.root = node

    def insert(self, item):
        """
        insert an elem to the binary search tree
        :param item: the value of the elem to be inserted
        :return: res of adding elem
        """
        # bulid a node
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        cur_node = self.root
        while True:
            if node.val > cur_node.val:
                if cur_node.right == None:
                    cur_node.right = node
                    return
                cur_node = cur_node.right
            else:
                if cur_node.left == None:
                    cur_node.left = node
                    return
                cur_node = cur_node.left

    def search(self, target):
        """
        Finding the target from the binary search tree
        :param target: the value to find
        :return: If found, returns the target node, if not, returns "Not Found!"
        """
        cur_node = self.root    # define a pointer
        while cur_node:
            if cur_node.val == target:
                return cur_node
            elif cur_node.val > target:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return "Not Found!"

    def delete(self, item):
        """
        delete an elem from the binary search tree
        :param item: the elem to delete
        :return: if not found, return "Not Found!". if the deletion is successful, returns "S"
        """
        # first, find the node
        parent = None
        cur_node = self.root
        while cur_node and cur_node.val != item:
            parent = cur_node
            cur_node = cur_node.left if cur_node.val > item else cur_node.right
        if not cur_node: return "Not Found!"

        # 2 delete the node
        # 2.1 the node has two children
        if cur_node.left and cur_node.right:
            temp = cur_node.right
            temp_parent = cur_node
            while temp.left:                        # 找到最小节点
                temp_parent = temp
                temp = temp.left
            cur_node.val = temp.val                 # 找到节点替换到要删除的节点上
            cur_node, parent = temp, temp_parent    # 将最小节点删除，转换为待删除节点没有节点或只有一个节点

        # 2.2 the node has one child or none
        child = cur_node.left if cur_node.left else cur_node.right
        if not parent:
            self.root = child
        elif parent.left == cur_node:
            parent.left = child
        else:
            parent.right = child



