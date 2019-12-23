def binary_search(alist, item):
    '''二分查找--no recursive'''
    alist_len = len(alist)
    start = 0
    end = alist_len - 1
    while start <= end:
        mid_index = (start + end) // 2
        if alist[mid_index] == item:
            return True
        elif alist[mid_index] > item:
            end = mid_index - 1
        elif alist[mid_index] < item:
            start = mid_index + 1
    return False

if __name__ == '__main__':
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search(alist, 3))
    print(binary_search(alist, 13))
