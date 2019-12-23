def quick_sort(alist, first, last):
    '''快速排序-不稳定排序-最坏为O(n^2)-最优为O(nlogn)'''
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high:
            if alist[high] <= mid_value:
                alist[low] = alist[high]
                break
            else:
                high -= 1

        while low < high:
            if alist[low] > mid_value:
                alist[high] = alist[low]
                break
            else:
                low += 1

    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    alist = [54,226,93,17,77,31,44,55,20]
    print(alist)
    quick_sort(alist, 0, len(alist)-1)
    print(alist)
