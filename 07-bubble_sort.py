def bubble_sort(alist):  # 传入的列表alist是一个引用，所以最后不返回alist也可以
    alist_len = len(alist)
    for j in range(alist_len-1, 0, -1):
        # 外层循环
        # 加入count记录交换次数，如果第一次外层循环的交换次数为0，则return
        # 加入count是一个优化，虽然最坏时间复杂度没有改变：O(n^2)
        # 但是最优时间复杂度时O(n)
        count = 0
        for i in range(j):
            # 内层循环
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return alist
    return alist


if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print(alist)
    bubble_sort(alist)
    print(alist)

