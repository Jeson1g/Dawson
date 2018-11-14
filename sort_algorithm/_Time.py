def swap(li, i, j):
    """交换两个变量的值"""
    li[i], li[j] = li[j], li[i]


def bubble_sort(li):
    """冒泡排序"""
    n = len(li)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if li[j] > li[j + 1]:
                swap(li, j, j + 1)
            count += 1
        if 0 == count:
            break

    return li


def bubble_sorts(li):
    """冒泡排序2"""
    n = len(li)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if li[j] > li[j + 1]:
                swap(li, j, j + 1)
            count += 1
        if 0 == count:
            break

    return li


def select_sort(li):
    """选择排序"""
    n = len(li)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if li[i] < li[min_index]:
                min_index = i
        if min_index != j:
            swap(li, j, min_index)

    return li


def insert_sort(li):
    """插入排序"""
    n = len(li)
    for j in range(n):
        for i in range(j, 0, -1):
            if li[i] < li[i - 1]:
                swap(li, i, i - 1)


def shell_sort(alist):
    """希尔排序
    :param alist:
    :return:
    """
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap / 2


if __name__ == '__main__':
    list1 = [4, 88, 1, 2, 0, 78]
    print(list1)
    insert_sort(list1)
    print(list1)
