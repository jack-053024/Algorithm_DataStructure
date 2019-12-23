def shell_sort(alist):
    '''希尔排序'''
    alist_len = len(alist)
    gap = alist_len // 2
    while gap > 0:
        # 希尔排序跟插入排序的区别在于gap
        for j in range(gap, alist_len):
            i = j
            while i > 0:
                # 当 i > 0 时，说明一次插入比较的过程还没结束，还需要跟前面的值进行比较
                # 插入排序的核心
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    # 指针向前移动
                    i -= gap
                else:
                    # 如果插入比较过程结束，则跳出循环，等待比较下一个值
                    break
        # 使用完gap后，缩短gap步长，再重新进行一次shell sort
        gap = gap // 2


if __name__ == '__main__':
    alist = [54,226,93,17,77,31,44,55,20]
    print(alist)
    shell_sort(alist)
    print(alist)