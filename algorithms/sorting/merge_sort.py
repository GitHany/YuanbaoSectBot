"""
归并排序算法 (Merge Sort)
时间复杂度: O(n log n)
空间复杂度: O(n)
"""


def merge_sort(arr):
    """
    归并排序 - 分治算法，将数组分成两半，排序后合并

    参数:
        arr (list): 需要排序的列表

    返回:
        list: 排序后的列表
    """
    if len(arr) <= 1:
        return arr

    # 分割数组
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 合并两个排序好的子数组
    return merge(left, right)


def merge(left, right):
    """
    合并两个已排序的列表

    参数:
        left (list): 左子数组
        right (list): 右子数组

    返回:
        list: 合并后的排序数组
    """
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 添加剩余的元素
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_iterative(arr):
    """
    迭代版归并排序 - 不使用递归的实现

    参数:
        arr (list): 需要排序的列表

    返回:
        list: 排序后的列表
    """
    n = len(arr)
    step = 1

    while step < n:
        for i in range(0, n, step * 2):
            left = arr[i : i + step]
            right = arr[i + step : i + step * 2]
            merged = merge(left, right)
            arr[i : i + step * 2] = merged
        step *= 2

    return arr


if __name__ == "__main__":
    # 测试示例
    test_arr = [12, 11, 13, 5, 6, 7]
    print("原始数组:", test_arr)

    sorted_arr = merge_sort(test_arr.copy())
    print("递归归并排序结果:", sorted_arr)

    iterative_arr = merge_sort_iterative(test_arr.copy())
    print("迭代归并排序结果:", iterative_arr)
