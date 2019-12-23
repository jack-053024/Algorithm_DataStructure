def select_sort(alist):
    '''选择排序'''
    # 1.分成已排区和未排序区
    # 2.将未排序区中的第一个数假定为最小，并记住它的下标，以此为标识最小数的下标
    # 3.将假定的数与未排序区中的每个数依次比较，如果发现比假定数更小的数，则将标识最小数的下标改为该数下标
    # 4.当遍历完未排序区的数，最终得到的最小数下标，就是本轮找到的最小数
    # 5.把假定的最小数的位置，与真正的最小数的位置进行交换
    # 6.以上循环，直到排序完
    alist_len = len(alist)
    for j in range(0, alist_len-1):
        min_index = j
        for i in range(j+1, alist_len):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

    # 时间复杂度：O(n^2)
    # 空间复杂度：O(1)
    # 稳定性：不稳定（假定选的是最大值）



if __name__ == '__main__':
    alist = [54,226,93,17,77,31,44,55,20]
    print(alist)
    select_sort(alist)
    print(alist)