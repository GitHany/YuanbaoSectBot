"""
YuanbaoSectBot - Python算法库示例
"""

from algorithms.sorting.bubble_sort import bubble_sort, bubble_sort_optimized
from algorithms.sorting.quick_sort import quick_sort, quick_sort_inplace
from algorithms.sorting.merge_sort import merge_sort, merge_sort_iterative

from algorithms.data_structures.linked_list import LinkedList, DoublyLinkedList
from algorithms.data_structures.stack_queue import Stack, Queue, Deque

from algorithms.search.binary_search import binary_search, binary_search_recursive
from algorithms.search.dfs import dfs_iterative, dfs_recursive
from algorithms.search.bfs import bfs, bfs_with_path

from algorithms.graph.dijkstra import dijkstra_adjacency_matrix, dijkstra_adjacency_list
from algorithms.graph.minimum_spanning_tree import prim, kruskal

from algorithms.mathematical.primes import is_prime, sieve_of_eratosthenes, gcd, lcm
from algorithms.mathematical.fibonacci import fibonacci_iterative, fibonacci_matrix

from algorithms.dynamic_programming.fibonacci_dp import fibonacci_dp, fibonacci_dp_optimized
from algorithms.dynamic_programming.knapsack import knapsack_01, knapsack_unbounded


def demo_sorting():
    """排序算法示例"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("排序算法演示:")
    print(f"原始数组: {arr}")
    
    # 冒泡排序
    bubble_result = bubble_sort(arr.copy())
    print(f"冒泡排序结果: {bubble_result}")
    
    bubble_optimized_result = bubble_sort_optimized(arr.copy())
    print(f"优化冒泡排序结果: {bubble_optimized_result}")
    
    # 快速排序
    quick_result = quick_sort(arr.copy())
    print(f"快速排序结果: {quick_result}")
    
    # 归并排序
    merge_result = merge_sort(arr.copy())
    print(f"归并排序结果: {merge_result}")
    
    merge_iterative_result = merge_sort_iterative(arr.copy())
    print(f"迭代归并排序结果: {merge_iterative_result}")


def demo_data_structures():
    """数据结构示例"""
    print("\n数据结构演示:")
    
    # 链表
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print(f"单向链表: {ll.display()}")
    
    # 双向链表
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print(f"双向链表正向: {dll.display_forward()}")
    print(f"双向链表反向: {dll.display_backward()}")
    
    # 栈
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"栈顶元素: {stack.peek()}")
    print(f"出栈: {stack.pop()}")
    
    # 队列
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"队首元素: {queue.peek()}")
    print(f"出队: {queue.dequeue()}")
    
    # 双端队列
    deque = Deque()
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(0)
    print(f"双端队列前端: {deque.peek_front()}")
    print(f"双端队列后端: {deque.peek_rear()}")


def demo_search():
    """搜索算法示例"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    print("\n搜索算法演示:")
    print(f"搜索数组: {arr}")
    
    # 二分搜索
    target = 7
    index = binary_search(arr, target)
    print(f"二分搜索 {target}: 索引 {index}")
    
    recursive_index = binary_search_recursive(arr, target)
    print(f"递归二分搜索 {target}: 索引 {recursive_index}")


def demo_graph():
    """图算法示例"""
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 1), (4, 3)],
        2: [(0, 1), (1, 2), (3, 5)],
        3: [(1, 1), (2, 5), (4, 2), (5, 4)],
        4: [(1, 3), (3, 2), (5, 3)],
        5: [(3, 4), (4, 3)]
    }
    
    print("\n图算法演示:")
    
    # Dijkstra算法
    distances = dijkstra_adjacency_list(graph, 0)
    print(f"Dijkstra从节点0的距离: {distances}")
    
    # 最小生成树
    mst_weight, mst_edges = prim(graph)
    print(f"Prim算法最小生成树权重: {mst_weight}")
    print(f"Prim算法最小生成树边列表: {mst_edges}")


def demo_mathematical():
    """数学算法示例"""
    print("\n数学算法演示:")
    
    # 质数
    primes = sieve_of_eratosthenes(50)
    print(f"小于50的质数: {primes}")
    
    # GCD和LCM
    a, b = 12, 18
    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)
    print(f"GCD({a}, {b}) = {gcd_result}")
    print(f"LCM({a}, {b}) = {lcm_result}")
    
    # 斐波那契数列
    fib_n = 10
    fib_result = fibonacci_iterative(fib_n)
    matrix_result = fibonacci_matrix(fib_n)
    print(f"斐波那契数列第{fib_n}项: 迭代法 {fib_result}, 矩阵法 {matrix_result}")


def demo_dynamic_programming():
    """动态规划示例"""
    print("\n动态规划演示:")
    
    # 斐波那契数列DP
    fib_n = 10
    fib_dp_result = fibonacci_dp(fib_n)
    fib_optimized_result = fibonacci_dp_optimized(fib_n)
    print(f"斐波那契数列第{fib_n}项: 标准DP {fib_dp_result}, 优化DP {fib_optimized_result}")
    
    # 背包问题
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    knapsack_result = knapsack_01(weights, values, capacity)
    print(f"背包问题: 物品重量{weights}, 物品价值{values}, 背包容量{capacity}")
    print(f"0/1背包最大价值: {knapsack_result}")
    
    unbounded_result = knapsack_unbounded(weights, values, capacity)
    print(f"完全背包最大价值: {unbounded_result}")


if __name__ == "__main__":
    print("=== YuanbaoSectBot Python算法库示例 ===\n")
    
    demo_sorting()
    demo_data_structures()
    demo_search()
    demo_graph()
    demo_mathematical()
    demo_dynamic_programming()
    
    print("\n=== 演示结束 ===")