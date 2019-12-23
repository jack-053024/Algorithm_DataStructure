def insertion_sort(alist):
    """insertion sort"""
    alist_len = len(alist)
    for j in range(1, alist_len):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


def insertion_sort(alist):
    """insertion sort"""
    alist_len = len(alist)
    for i in range(1, alist_len):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break


def insertion_sort(alist):
    """insertion sort"""
    alist_len = len(alist)
    for i in range(1, alist_len):
        temp = alist[i]
        for j in range(i, 0, -1):
            if alist[j-1] > temp:
                alist[j] = alist[j-1]
            else:
                alist[j] = temp
                break
            alist[j-1] = temp


if __name__ == '__main__':
    alist = [54,226,93,17,77,31,44,55,20]
    print(alist)
    insertion_sort(alist)
    print(alist)