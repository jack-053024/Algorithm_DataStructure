class Queue(object):
    '''队列'''
    def __init__(self):
        self.__list = []  # python's list is equivalent to array

    def is_empty(self):
        '''判空'''
        return not self.__list

    def size(self):
        '''求队列长度'''
        return len(self.__list)

    def enqueue(self, item):
        '''往队列尾加入一个item元素'''
        self.__list.insert(0, item)  # o(n)

    def dequeue(self):
        '''从队列头取出一个元素'''
        return self.__list.pop()  # O(1)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('zhong')
    queue.enqueue('yu')
    queue.enqueue('ming')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

