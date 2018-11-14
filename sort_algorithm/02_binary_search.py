def binary_search(alist, item):
    """
    二分查找 递归实现版本
    :param alist:
    :param item: 查找的元素
    :return: True, False
    """
    n = len(alist)
    if 0 == n:
        return False

    mid = n // 2

    if alist[mid] == item:
        return True
    elif item < alist[mid]:
        return binary_search(alist[:mid], item)
    else:
        return binary_search(alist[mid+1:], item)


def binary_search_2(alist, item):
    """
    二分查找 非递归版本
    :param alist:
    :param item:
    :return: True False
    """
    start = 0
    end = len(alist) - 1

    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    # print(binary_search(testlist, 32))
    # print(binary_search(testlist, 60))
    print(binary_search_2(testlist, 32))
    print(binary_search_2(testlist, 60))
