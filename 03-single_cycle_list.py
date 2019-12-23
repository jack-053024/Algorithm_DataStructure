# coding:utf-8

# single_cycle_list节点
class Node(object):
    '''单循环链表节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleList(object):
    '''单循环链表'''
    def __init__(self, node=None):
        self.__head = node
        if self.__head:
            # 如果链表不为空
            node.next = self.__head

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''返回链表的长度'''
        if self.is_empty():
            return 0
        # 1.定义一个游标，让游标指向头节点
        cursor = self.__head
        # 2.定义变量count记录节点个数
        count = 1
        while cursor.next != self.__head:
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        cursor = self.__head
        while cursor.next != self.__head:
            print(cursor.elem, end=' ')
            cursor = cursor.next
        print(cursor.elem)

    def add(self, item):
        '''链表头增加一个元素，头插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return
        cursor = self.__head
        while cursor.next != self.__head:
            cursor = cursor.next
        node.next = self.__head
        self.__head = node
        cursor.next = self.__head

    def append(self, item):
        '''链表尾增加一个元素，尾插法
        :param item: 新加入的元素值
        '''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return
        cursor = self.__head
        while cursor.next != self.__head:
            cursor = cursor.next
        cursor.next = node
        node.next = self.__head

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
            # 正常情况下，将数据插入中间
            node = Node(item)
            cursor = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cursor = cursor.next
            # 跳出循环后，开始修改节点指向
            # 先将新节点指向下一个节点，再把前一个节点指向新节点
            node.next = cursor.next
            cursor.next = node

    def remove(self, item):
        '''删除节点
        :param item: 待删除的元素
        '''
        cursor = self.__head
        pre = None
        if self.is_empty():
            return
        while cursor.next != self.__head:
            if cursor.elem == item:
                if cursor == self.__head:
                    # 如果要移除的元素在头节点
                    # 找到尾节点，让尾结点的next指向新的头节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 跳出循环后，rear指向尾节点
                    self.__head = cursor.next
                    rear.next = self.__head
                else:
                    # 如果要移除元素位于单链表中间
                    pre.next = cursor.next
                return
            else:
                pre = cursor
                cursor = cursor.next
        if cursor.elem == item:
            if cursor == self.__head:
                # 如果只有一个节点
                self.__head = None
            else:
                pre.next = self.__head


    def search(self, item):
        '''查询元素是否存在
        :param item: 待查询的元素
        :return: 是否存在
        '''
        if self.is_empty():
            return False
        cursor = self.__head
        while cursor.next != self.__head:
            if cursor.elem == item:
                return True
            cursor = cursor.next
        if cursor.elem == item:
            return True
        return False



if __name__ == '__main__':
    single_cycle_list = SingleCycleList()
    print(single_cycle_list.is_empty())
    print(single_cycle_list.length())

    single_cycle_list.append(1)
    print(single_cycle_list.is_empty())
    print(single_cycle_list.length())

    single_cycle_list.add(8)

    single_cycle_list.append(2)
    single_cycle_list.append(3)
    single_cycle_list.append(4)
    single_cycle_list.append(5)
    single_cycle_list.append(6)

    single_cycle_list.travel()  # 8 1 2 3 4 5 6

    single_cycle_list.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    single_cycle_list.travel()
    single_cycle_list.insert(8, 10)  # 9 8 1 2 3 4 5 6 10
    single_cycle_list.travel()
    single_cycle_list.insert(2, 11)  # 9 8 11 1 2 3 4 5 6 10
    single_cycle_list.travel()

    single_cycle_list.remove(9)
    single_cycle_list.remove(11)
    single_cycle_list.remove(10)
    single_cycle_list.travel()  # 8 1 2 3 4 5 6

    print(single_cycle_list.search(1))




















