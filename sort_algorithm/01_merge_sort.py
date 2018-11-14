def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if 1 == n:
        return alist
    mid = n // 2

    # 对左半部分进行归并排序
    left_sorted_li = merge_sort(alist[:mid])

    # 对右半部分进行归并排序
    right_sorted_li = merge_sort(alist[mid:])

    # 合并两个有序集合
    left, right = 0, 0
    merge_sorted_li = []

    left_n = len(left_sorted_li)
    right_n = len(right_sorted_li)

    while left < left_n and right < right_n:
        if left_sorted_li[left] <= right_sorted_li[right]:
            merge_sorted_li.append(left_sorted_li[left])
            left += 1
        else:
            merge_sorted_li.append(right_sorted_li[right])
            right += 1

    merge_sorted_li += left_sorted_li[left:]
    merge_sorted_li += right_sorted_li[right:]

    return merge_sorted_li


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before sort: %s" % alist)
    sorted_alist = merge_sort(alist)
    print("sorted new list: %s" % sorted_alist)
