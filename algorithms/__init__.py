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
from algorithms.graph.minimum_spanning_tree import prim, kruskal, dijkstra_mst

from algorithms.mathematical.primes import is_prime, sieve_of_eratosthenes, prime_factors, gcd, lcm
from algorithms.mathematical.fibonacci import fibonacci_recursive, fibonacci_iterative, fibonacci_dynamic, fibonacci_memoization, fibonacci_matrix, fibonacci_sequence
from algorithms.mathematical.fast_power import fast_power, fast_power_recursive
from algorithms.mathematical.number_theory_simple import (
    gcd_euclidean,
    gcd_euclidean_recursive,
    sieve_of_eratosthenes
)

from algorithms.string.kmp import kmp_preprocess, kmp_search, kmp_search_with_prefix_table, kmp_longest_prefix_suffix, kmp_visualize, kmp_performance_test
from algorithms.string.boyer_moore_simple import boyer_moore_search

from algorithms.geometry.convex_hull import convex_hull_graham, convex_hull_jarvis, convex_hull_quickhull, convex_hull_brute_force, convex_hull_visualize, convex_hull_performance_test, convex_hull_distance
from algorithms.geometry.closest_pair import closest_pair_brute_force, closest_pair_divide_and_conquer, closest_pair_recursive, closest_pair_kd_tree, closest_pair_performance_test, closest_pair_visualize, closest_pair_all_points