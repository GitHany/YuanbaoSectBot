"""
搜索算法单元测试
"""

import unittest
import sys
sys.path.insert(0, '../.')

from algorithms.search.binary_search import binary_search, binary_search_recursive, binary_search_leftmost, binary_search_rightmost
from algorithms.search.dfs import dfs_recursive, dfs_iterative, dfs_with_path, dfs_cycle_detection, dfs_topological_sort, dfs_connected_components
from algorithms.search.bfs import bfs, bfs_levels, bfs_with_path, bfs_connected_components, bfs_bidirectional, bfs_distance, bfs_max_distance


class TestBinarySearch(unittest.TestCase):
    """二分搜索测试类"""
    
    def setUp(self):
        """设置测试数据"""
        self.test_array = [1, 3, 5, 7, 9, 11, 13, 15]
        self.test_array_with_duplicates = [1, 3, 5, 7, 7, 7, 9, 11]
    
    def test_binary_search_exists(self):
        """测试二分搜索 - 元素存在"""
        target = 7
        expected_index = 3
        
        # 标准二分搜索
        result = binary_search(self.test_array, target)
        self.assertEqual(result, expected_index)
        
        # 递归二分搜索
        result_recursive = binary_search_recursive(self.test_array, target)
        self.assertEqual(result_recursive, expected_index)
    
    def test_binary_search_not_exists(self):
        """测试二分搜索 - 元素不存在"""
        target = 8
        
        # 标准二分搜索
        result = binary_search(self.test_array, target)
        self.assertIsNone(result)
        
        # 递归二分搜索
        result_recursive = binary_search_recursive(self.test_array, target)
        self.assertIsNone(result_recursive)
    
    def test_binary_search_leftmost(self):
        """测试左边界二分搜索"""
        target = 7
        expected_index = 3
        
        result = binary_search_leftmost(self.test_array_with_duplicates, target)
        self.assertEqual(result, expected_index)
    
    def test_binary_search_rightmost(self):
        """测试右边界二分搜索"""
        target = 7
        expected_index = 5
        
        result = binary_search_rightmost(self.test_array_with_duplicates, target)
        self.assertEqual(result, expected_index)
    
    def test_binary_search_empty_array(self):
        """测试空数组"""
        empty_array = []
        target = 5
        
        result = binary_search(empty_array, target)
        self.assertIsNone(result)
        
        result_recursive = binary_search_recursive(empty_array, target)
        self.assertIsNone(result_recursive)
    
    def test_binary_search_edge_cases(self):
        """测试边界情况"""
        # 最小元素
        result_min = binary_search(self.test_array, 1)
        self.assertEqual(result_min, 0)
        
        # 最大元素
        result_max = binary_search(self.test_array, 15)
        self.assertEqual(result_max, 7)
        
        # 只有一个元素的数组
        single_array = [5]
        result_single = binary_search(single_array, 5)
        self.assertEqual(result_single, 0)
        
        result_single_not_exist = binary_search(single_array, 3)
        self.assertIsNone(result_single_not_exist)


class TestDFS(unittest.TestCase):
    """深度优先搜索测试类"""
    
    def setUp(self):
        """设置测试图"""
        self.graph = {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 4],
            3: [1, 5],
            4: [2, 5],
            5: [3, 4],
            6: [7],
            7: [6]
        }
        
        self.dag_graph = {  # 有向无环图
            0: [1, 2],
            1: [3],
            2: [3],
            3: [4],
            4: [],
            5: [6],
            6: []
        }
    
    def test_dfs_recursive(self):
        """测试递归DFS"""
        result = dfs_recursive(self.graph, 0)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5])
    
    def test_dfs_iterative(self):
        """测试迭代DFS"""
        result = dfs_iterative(self.graph, 0)
        # DFS遍历顺序可能不同，但应该包含所有节点
        self.assertEqual(len(result), 6)
        self.assertEqual(set(result), {0, 1, 2, 3, 4, 5})
    
    def test_dfs_with_path(self):
        """测试DFS路径查找"""
        path = dfs_with_path(self.graph, 0, 5)
        self.assertTrue(path is not None)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 5)
        
        # 不可达路径
        unreachable_path = dfs_with_path(self.graph, 0, 8)
        self.assertIsNone(unreachable_path)
    
    def test_dfs_cycle_detection(self):
        """测试DFS环检测"""
        # 测试有环图
        has_cycle = dfs_cycle_detection(self.graph)
        self.assertTrue(has_cycle)
        
        # 测试无环图
        no_cycle = dfs_cycle_detection(self.dag_graph)
        self.assertFalse(no_cycle)
    
    def test_dfs_topological_sort(self):
        """测试拓扑排序"""
        topological_order = dfs_topological_sort(self.dag_graph)
        # 拓扑排序结果应该满足有向边的关系
        self.assertEqual(len(topological_order), 7)
        
        # 验证排序顺序
        for node in topological_order:
            if node in self.dag_graph:
                for neighbor in self.dag_graph[node]:
                    # 节点应该在邻居之前
                    self.assertTrue(
                        topological_order.index(node) < topological_order.index(neighbor)
                    )
    
    def test_dfs_connected_components(self):
        """测试连通分量"""
        components = dfs_connected_components(self.graph)
        # 应该有两个连通分量
        self.assertEqual(len(components), 2)
        
        # 第一个分量包含节点0-5
        component1 = components[0]
        self.assertEqual(set(component1), {0, 1, 2, 3, 4, 5})
        
        # 第二个分量包含节点6,7
        component2 = components[1]
        self.assertEqual(set(component2), {6, 7})
    
    def test_dfs_empty_graph(self):
        """测试空图"""
        empty_graph = {}
        result = dfs_iterative(empty_graph, 0)
        self.assertEqual(result, [])
        
        # 图中不存在起始节点
        result = dfs_iterative(empty_graph, 1)
        self.assertEqual(result, [])


class TestBFS(unittest.TestCase):
    """广度优先搜索测试类"""
    
    def setUp(self):
        """设置测试图"""
        self.graph = {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 4],
            3: [1, 5],
            4: [2, 5],
            5: [3, 4],
            6: [7],
            7: [6]
        }
    
    def test_bfs(self):
        """测试BFS"""
        result = bfs(self.graph, 0)
        # BFS应该按层级顺序遍历
        self.assertEqual(len(result), 6)
        self.assertEqual(set(result), {0, 1, 2, 3, 4, 5})
    
    def test_bfs_with_path(self):
        """测试BFS最短路径查找"""
        path = bfs_with_path(self.graph, 0, 5)
        self.assertTrue(path is not None)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 5)
        # 最短路径长度
        self.assertTrue(len(path) <= 3)
        
        # 不可达路径
        unreachable_path = bfs_with_path(self.graph, 0, 8)
        self.assertIsNone(unreachable_path)
    
    def test_bfs_levels(self):
        """测试BFS层级"""
        levels = bfs_levels(self.graph, 0)
        
        # 节点层级验证
        self.assertEqual(levels[0], 0)
        self.assertEqual(levels[1], 1)
        self.assertEqual(levels[2], 1)
        
        # 更远的节点
        self.assertEqual(levels[5], 2)
    
    def test_bfs_connected_components(self):
        """测试BFS连通分量"""
        components = bfs_connected_components(self.graph)
        # 应该有两个连通分量
        self.assertEqual(len(components), 2)
        
        # 第一个分量包含节点0-5
        component1 = components[0]
        self.assertEqual(set(component1), {0, 1, 2, 3, 4, 5})
        
        # 第二个分量包含节点6,7
        component2 = components[1]
        self.assertEqual(set(component2), {6, 7})
    
    def test_bfs_bidirectional(self):
        """测试双向BFS"""
        # 正常路径
        distance = bfs_bidirectional(self.graph, 0, 5)
        self.assertEqual(distance, 2)  # 0->1->3->5 或 0->2->4->5
        
        # 相同节点
        distance_zero = bfs_bidirectional(self.graph, 0, 0)
        self.assertEqual(distance_zero, 0)
        
        # 不可达路径
        distance_unreachable = bfs_bidirectional(self.graph, 0, 8)
        self.assertIsNone(distance_unreachable)
    
    def test_bfs_distance(self):
        """测试BFS距离"""
        distances = bfs_distance(self.graph, 0)
        
        self.assertEqual(distances[0], 0)
        self.assertEqual(distances[1], 1)
        self.assertEqual(distances[2], 1)
        self.assertEqual(distances[5], 2)
    
    def test_bfs_max_distance(self):
        """测试BFS最大距离"""
        farthest_node, max_distance = bfs_max_distance(self.graph, 0)
        
        # 最远的节点应该是5，距离是2
        self.assertEqual(farthest_node, 5)
        self.assertEqual(max_distance, 2)
    
    def test_bfs_empty_graph(self):
        """测试空图"""
        empty_graph = {}
        result = bfs(empty_graph, 0)
        self.assertEqual(result, [])
        
        # 图中不存在起始节点
        result = bfs(empty_graph, 1)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()