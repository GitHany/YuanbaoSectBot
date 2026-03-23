"""
冒泡排序算法 (Bubble Sort)
时间复杂度: O(n²)
空间复杂度: O(1)
"""

def bubble_sort(arr):
    """
    冒泡排序 - 通过反复交换相邻元素来排序
    
    参数:
        arr (list): 需要排序的列表
    
    返回:
        list: 排序后的列表
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经排序好
        for j in range(0, n-i-1):
            # 如果当前元素比下一个元素大，交换它们
            if arr[j] > arr[j+1]:
                # 交换元素
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


def bubble_sort_optimized(arr):
    """
    优化版冒泡排序 - 提前终止如果数组已排序
    
    参数:
        arr (list): 需要排序的列表
    
    返回:
        list: 排序后的列表
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # 如果在一次遍历中没有交换发生，说明数组已经排序完成
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # 测试示例
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_arr)
    
    sorted_arr = bubble_sort(test_arr.copy())
    print("冒泡排序结果:", sorted_arr)
    
    optimized_arr = bubble_sort_optimized(test_arr.copy())
    print("优化版冒泡排序结果:", optimized_arr)