"""
算法库根目录
"""

# 版本信息
__version__ = "1.0.0"
__author__ = "GitHany/YuanbaoSectBot"

# 导入路径
from algorithms.sorting.bubble_sort import bubble_sort, bubble_sort_optimized
from algorithms.sorting.quick_sort import quick_sort, quick_sort_inplace
from algorithms.sorting.merge_sort import merge_sort, merge_sort_iterative

from algorithms.data_structures.linked_list import LinkedList, DoublyLinkedList
from algorithms.data_structures.stack_queue import Stack, Queue, Deque

from algorithms.search.binary_search import binary_search, binary_search_recursive, binary_search_leftmost, binary_search_rightmost

from algorithms.graph.dijkstra import dijkstra_adjacency_matrix, dijkstra_adjacency_list, dijkstra_with_path

from algorithms.mathematical.primes import is_prime, sieve_of_eratosthenes, prime_factors, gcd, lcm
from algorithms.mathematical.fibonacci import fibonacci_recursive, fibonacci_iterative, fibonacci_dynamic, fibonacci_memoization, fibonacci_matrix, fibonacci_sequence