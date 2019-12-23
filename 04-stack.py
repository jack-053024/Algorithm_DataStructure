# coding: utf-8

class Stack(object):
    '''栈'''
    def __init__(self):
        self.__list = []

    def is_empty(self):
        '''判断栈是否为空'''
        return not self.__list

    def push(self, item):
        '''压栈、入栈：加入元素'''
        self.__list.append(item)  # O(1)

    def pop(self):
        '''出栈：弹出元素'''
        if self.is_empty():
            return None
        return self.__list.pop()  # O(1)

    def peek(self):
        '''取出栈顶元素'''
        if self.is_empty():
            return None
        return self.__list[-1]

    def size(self):
        '''返回栈中元素的数量'''
        return len(self.__list)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.is_empty())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
