def swop(li, i):
    """交换两个变量的值"""
    li[i], li[i + 1] = li[i + 1], li[i]


def bubble_sort(a_list):
    """冒泡排序"""
    n = len(a_list)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if a_list[j] > a_list[j + 1]:
                swop(a_list, j)
            count += 1
        if 0 == count:
            break

    return a_list


def bubble_sorts(a_list):
    """冒泡排序2"""
    n = len(a_list)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                swop(a_list, j)
            count += 1
        if 0 == count:
            break

    return a_list


def select_sort(a_list):
    """选择排序"""
    n = len(a_list)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if a_list[i] < a_list[min_index]:
                min_index = i
        if 0 != min_index:
            a_list[j], a_list[min_index] = a_list[min_index], a_list[j]

    return a_list


def insert_sort(a_list):
    """插入排序"""
    n = len(a_list)
    for j in range(n):
        for i in range(j, 0, -1):
            if a_list[i] < a_list[i - 1]:
                a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]


if __name__ == '__main__':
    a_list = [4, 88, 1, 2, 0, 78]
    print(a_list)
    bubble_sort(a_list)
    print(a_list)
