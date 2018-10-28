def swap(li, i):
    """交换两个变量的值"""
    li[i], li[i + 1] = li[i + 1], li[i]


def bubble_sort(li):
    """冒泡排序"""
    n = len(li)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if li[j] > li[j + 1]:
                swap(li, j)
            count += 1
        if 0 == count:
            break

    return a_list


def bubble_sorts(li):
    """冒泡排序2"""
    n = len(li)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if li[j] > li[j + 1]:
                swap(li, j)
            count += 1
        if 0 == count:
            break

    return a_list


def select_sort(li):
    """选择排序"""
    n = len(li)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if li[i] < li[min_index]:
                min_index = i
        if 0 != min_index:
            li[j], li[min_index] = li[min_index], li[j]

    return a_list


def insert_sort(li):
    """插入排序"""
    n = len(li)
    for j in range(n):
        for i in range(j, 0, -1):
            if li[i] < li[i - 1]:
                li[i], li[i - 1] = li[i - 1], li[i]


if __name__ == '__main__':
    a_list = [4, 88, 1, 2, 0, 78]
    print(a_list)
    select_sort(a_list)
    print(a_list)
