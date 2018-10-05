def bubble_sort(a_list):
    """冒泡排序"""
    n = len(a_list)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
            count += 1
        if 0 == count:
            break

    return a_list

if __name__ == '__main__':
    a_list = [4, 88, 1, 2, 0, 78]
    print(a_list)
    new_list = bubble_sort(a_list)
    print(new_list)