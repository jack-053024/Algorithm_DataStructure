def binary_search(alist, item):
    '''二分查找--递归实现'''
    # 二分查找只能作用的对象必须满足两个条件：
    # 1.有序  2.顺序表：因为用到了下标
    # 先计算列表长度
    alist_len = len(alist)
    if alist_len < 1:
        return False
    mid_index = (alist_len - 1) // 2
    if alist[mid_index] == item:
        return True
    elif alist[mid_index] > item:
        return binary_search(alist[:mid_index], item)
    elif alist[mid_index] < item:
        return binary_search(alist[mid_index+1:], item)
    return False


if __name__ == "__main__":
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binary_search(alist, 3))
    print(binary_search(alist, 13))
