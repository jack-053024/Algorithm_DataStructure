class Dequeue(object):
    '''Double-end queue'''
    def __init__(self):
        self.__list = []  # python中的list是一个顺序表

    def add_front(self, item):
        '''在队列头增加一个item元素'''
        self.__list.insert(0, item)  # O(n)

    def add_rear(self, item):
        '''在队列尾增加一个item元素'''
        self.__list.append(item)  # O(1)

    def remove_front(self):
        '''在队列头取出一个元素'''
        return self.__list.pop(0)  # O(n)

    def remove_rear(self):
        '''在队列尾取出一个元素'''
        return self.__list.pop()  # O(1)

    def is_empty(self):
        '''判空'''
        return not self.__list

    def size(self):
        '''返回双端队列的长度'''
        return len(self.__list)


if __name__ == '__main__':
    deque = Dequeue()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.is_empty())
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
