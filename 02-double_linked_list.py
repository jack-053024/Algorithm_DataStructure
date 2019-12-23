# coding: utf-8

class Node(object):
    '''双链表节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    '''双向链表'''
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''返回链表的长度'''
        # 1.定义一个游标，让游标指向头节点
        cursor = self.__head
        # 2.定义变量count记录节点个数
        count = 0
        while cursor != None:
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cursor = self.__head
        while cursor != None:
            print(cursor.elem, end=' ')
            cursor = cursor.next
        print()

    def add(self, item):
        '''链表头增加一个元素，头插法'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        '''链表尾增加一个元素，尾插法
        :param item: 新加入的元素值
        '''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cursor = self.__head
        while cursor.next != None:
            cursor = cursor.next
        cursor.next = node
        node.prev = cursor

    def insert(self, pos, item):
        '''在指定位置增加元素
        :param pos: 加入新元素的位置
        :param item: 加入的新元素的值
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cursor = self.__head
            count = 0
            while count < pos:
                count += 1
                cursor = cursor.next
            # 跳出循环后，开始修改节点指向
            # 先将新节点指向下一个节点，再把前一个节点指向新节点
            node.next = cursor
            node.prev = cursor.prev
            cursor.prev.next = node
            cursor.prev = node

    def remove(self, item):
        '''删除节点
        :param item: 待删除的元素
        '''
        cursor = self.__head
        while cursor != None:
            if cursor.elem == item:
                if cursor == self.__head:
                    self.__head = cursor.next
                    if cursor.next:
                        cursor.next.prev = None
                else:
                    cursor.prev.next = cursor.next
                    if cursor.next:
                        cursor.next.prev = cursor.prev
                break
            else:
                cursor = cursor.next

    def search(self, item):
        '''查询元素是否存在
        :param item: 待查询的元素
        :return: 是否存在
        '''
        cursor = self.__head
        while cursor != None:
            if cursor.elem == item:
                return True
            cursor = cursor.next
        return False


if __name__ == '__main__':
    double_linked_list = DoubleLinkedList()
    print(double_linked_list.is_empty())
    print(double_linked_list.length())

    double_linked_list.append(1)
    print(double_linked_list.is_empty())
    print(double_linked_list.length())

    double_linked_list.add(8)

    double_linked_list.append(2)
    double_linked_list.append(3)
    double_linked_list.append(4)
    double_linked_list.append(5)
    double_linked_list.append(6)

    double_linked_list.travel()  # 8 1 2 3 4 5 6

    double_linked_list.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    double_linked_list.travel()
    double_linked_list.insert(8, 10)  # 9 8 1 2 3 4 5 6 10
    double_linked_list.travel()
    double_linked_list.insert(2, 11)  # 9 8 11 1 2 3 4 5 6 10
    double_linked_list.travel()

    double_linked_list.remove(9)
    double_linked_list.remove(11)
    double_linked_list.remove(10)
    double_linked_list.travel()  # 8 1 2 3 4 5 6

    print(double_linked_list.search(1))
