"""
二分搜索算法 (Binary Search)
时间复杂度: O(log n)
"""


def binary_search(arr, target):
    """
    二分搜索 - 在有序数组中查找元素

    参数:
        arr (list): 有序数组
        target (int): 要查找的目标值

    返回:
        int or None: 目标值的索引，如果未找到则返回None
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binary_search_recursive(arr, target, low=0, high=None):
    """
    递归二分搜索

    参数:
        arr (list): 有序数组
        target (int): 要查找的目标值
        low (int): 搜索范围起始索引
        high (int): 搜索范围结束索引

    返回:
        int or None: 目标值的索引，如果未找到则返回None
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return None

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def binary_search_leftmost(arr, target):
    """
    查找最左边的匹配位置

    参数:
        arr (list): 有序数组
        target (int): 要查找的目标值

    返回:
        int or None: 最左边的匹配索引，如果未找到则返回None
    """
    low, high = 0, len(arr) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # 继续在左边搜索
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def binary_search_rightmost(arr, target):
    """
    查找最右边的匹配位置

    参数:
        arr (list): 有序数组
        target (int): 要查找的目标值

    返回:
        int or None: 最右边的匹配索引，如果未找到则返回None
    """
    low, high = 0, len(arr) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1  # 继续在右边搜索
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


if __name__ == "__main__":
    # 测试示例
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    print("有序数组:", arr)
    print("目标值:", target)

    # 标准二分搜索
    index = binary_search(arr, target)
    print(f"二分搜索找到索引: {index}")

    # 递归二分搜索
    recursive_index = binary_search_recursive(arr, target)
    print(f"递归二分搜索找到索引: {recursive_index}")

    # 测试左边界搜索
    arr_with_duplicates = [1, 3, 5, 7, 7, 7, 9, 11]
    leftmost = binary_search_leftmost(arr_with_duplicates, 7)
    print(f"重复数组中最左边的7: {leftmost}")

    # 测试右边界搜索
    rightmost = binary_search_rightmost(arr_with_duplicates, 7)
    print(f"重复数组中最右边的7: {rightmost}")

    # 测试未找到的情况
    not_found = binary_search(arr, 10)
    print(f"查找不存在的10: {not_found}")
