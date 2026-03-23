"""
排序算法单元测试
"""

import unittest
import sys
sys.path.append('/root/.openclaw/workspace/YuanbaoSectBot')

from algorithms.sorting.bubble_sort import bubble_sort, bubble_sort_optimized
from algorithms.sorting.quick_sort import quick_sort, quick_sort_inplace
from algorithms.sorting.merge_sort import merge_sort, merge_sort_iterative


class TestSortingAlgorithms(unittest.TestCase):
    """排序算法测试类"""
    
    def setUp(self):
        """设置测试数据"""
        self.test_cases = [
            ([], []),  # 空列表
            ([1], [1]),  # 单个元素
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # 已排序
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # 逆序
            ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]),  # 随机
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),  # 示例
        ]
    
    def test_bubble_sort(self):
        """测试冒泡排序"""
        for input_arr, expected in self.test_cases:
            result = bubble_sort(input_arr.copy())
            self.assertEqual(result, expected)
            # 验证排序后数组长度不变
            self.assertEqual(len(result), len(input_arr))
    
    def test_bubble_sort_optimized(self):
        """测试优化版冒泡排序"""
        for input_arr, expected in self.test_cases:
            result = bubble_sort_optimized(input_arr.copy())
            self.assertEqual(result, expected)
            self.assertEqual(len(result), len(input_arr))
    
    def test_quick_sort(self):
        """测试快速排序"""
        for input_arr, expected in self.test_cases:
            result = quick_sort(input_arr.copy())
            self.assertEqual(result, expected)
            self.assertEqual(len(result), len(input_arr))
    
    def test_quick_sort_inplace(self):
        """测试原地快速排序"""
        for input_arr, expected in self.test_cases:
            # 原地排序会修改原数组
            arr_copy = input_arr.copy()
            quick_sort_inplace(arr_copy)
            self.assertEqual(arr_copy, expected)
            self.assertEqual(len(arr_copy), len(input_arr))
    
    def test_merge_sort(self):
        """测试归并排序"""
        for input_arr, expected in self.test_cases:
            result = merge_sort(input_arr.copy())
            self.assertEqual(result, expected)
            self.assertEqual(len(result), len(input_arr))
    
    def test_merge_sort_iterative(self):
        """测试迭代版归并排序"""
        for input_arr, expected in self.test_cases:
            result = merge_sort_iterative(input_arr.copy())
            self.assertEqual(result, expected)
            self.assertEqual(len(result), len(input_arr))
    
    def test_sort_performance(self):
        """测试排序算法性能（不验证结果，只验证能够处理较大数组）"""
        large_array = [i for i in range(1000, 0, -1)]  # 1000个元素，逆序
        expected = list(range(1, 1001))  # 1到1000
        
        # 冒泡排序
        result_bubble = bubble_sort(large_array.copy())
        self.assertEqual(result_bubble, expected)
        
        # 快速排序
        result_quick = quick_sort(large_array.copy())
        self.assertEqual(result_quick, expected)
        
        # 归并排序
        result_merge = merge_sort(large_array.copy())
        self.assertEqual(result_merge, expected)
    
    def test_sort_edge_cases(self):
        """测试边界情况"""
        # 重复元素
        arr_with_duplicates = [5, 2, 8, 2, 5, 8, 2]
        sorted_with_duplicates = sorted(arr_with_duplicates)
        
        self.assertEqual(bubble_sort(arr_with_duplicates.copy()), sorted_with_duplicates)
        self.assertEqual(quick_sort(arr_with_duplicates.copy()), sorted_with_duplicates)
        self.assertEqual(merge_sort(arr_with_duplicates.copy()), sorted_with_duplicates)
        
        # 负数
        arr_with_negatives = [-5, 2, -8, 0, 7, -3]
        sorted_with_negatives = sorted(arr_with_negatives)
        
        self.assertEqual(bubble_sort(arr_with_negatives.copy()), sorted_with_negatives)
        self.assertEqual(quick_sort(arr_with_negatives.copy()), sorted_with_negatives)
        self.assertEqual(merge_sort(arr_with_negatives.copy()), sorted_with_negatives)


if __name__ == "__main__":
    unittest.main()