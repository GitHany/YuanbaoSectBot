"""
快速排序算法 (Quick Sort)
时间复杂度: O(n log n) - 平均情况, O(n²) - 最坏情况
空间复杂度: O(log n)
"""


def quick_sort(arr):
    """
    快速排序 - 分治算法，选择一个基准元素将数组分为两部分

    参数:
        arr (list): 需要排序的列表

    返回:
        list: 排序后的列表
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    原地快速排序 - 不使用额外空间的快速排序实现

    参数:
        arr (list): 需要排序的列表
        low (int): 起始索引
        high (int): 结束索引

    返回:
        list: 排序后的列表
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 分区操作，找到基准元素的正确位置
        pivot_index = partition(arr, low, high)

        # 递归排序左半部分和右半部分
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    """
    分区函数 - 用于原地快速排序

    参数:
        arr (list): 数组
        low (int): 起始索引
        high (int): 结束索引

    返回:
        int: 基准元素的最终位置
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # 测试示例
    test_arr = [10, 7, 8, 9, 1, 5]
    print("原始数组:", test_arr)

    sorted_arr = quick_sort(test_arr.copy())
    print("快速排序结果:", sorted_arr)

    inplace_arr = test_arr.copy()
    quick_sort_inplace(inplace_arr)
    print("原地快速排序结果:", inplace_arr)
