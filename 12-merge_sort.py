def merge_sort(alist):
    """merge sort"""
    if len(alist) <= 1:
        return alist
    alist_len = len(alist)
    mid = alist_len // 2

    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result
# analyse: stable; time complexity: O(nlogn); space complexity: O(n)


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    ret = merge_sort(alist)
    print(alist)
    print(ret)