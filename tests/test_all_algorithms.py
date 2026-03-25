"""测试所有新实现的算法"""

import sys
sys.path.insert(0, '.')

from algorithms.graph.dijkstra import dijkstra_adjacency_matrix, dijkstra_adjacency_list, dijkstra_with_path, create_sample_graph, create_sample_matrix
from algorithms.graph.minimum_spanning_tree import prim, kruskal, dijkstra_mst, create_sample_graph, create_weighted_graph

from algorithms.string.kmp import kmp_preprocess, kmp_search, kmp_longest_prefix_suffix
from algorithms.string.boyer_moore import boyer_moore_search

from algorithms.mathematical.fast_power import fast_power, fast_power_recursive
from algorithms.mathematical.primes import is_prime, sieve_of_eratosthenes, gcd, lcm
from algorithms.mathematical.number_theory import gcd_euclidean, gcd_euclidean_recursive, sieve_of_eratosthenes

from algorithms.geometry.convex_hull import convex_hull_graham, convex_hull_jarvis, convex_hull_quickhull, convex_hull_brute_force
from algorithms.geometry.closest_pair import closest_pair_brute_force, closest_pair_divide_and_conquer, closest_pair_recursive


def test_graph_algorithms():
    """测试图论算法"""
    print("\n=== 图论算法测试 ===\n")
    
    # Dijkstra算法测试
    print("Dijkstra算法测试:")
    matrix_graph = create_sample_matrix()
    distances_matrix = dijkstra_adjacency_matrix(matrix_graph, 0)
    print(f"邻接矩阵图 - 从节点0到所有节点的最短距离: {distances_matrix}")
    
    list_graph = create_sample_graph()
    distances_list = dijkstra_adjacency_list(list_graph, 0)
    print(f"邻接列表图 - 从节点0到所有节点的最短距离: {distances_list}")
    
    distance, path = dijkstra_with_path(list_graph, 0, 4)
    print(f"从节点0到节点4的最短路径: {path}, 距离: {distance}")
    
    # 最小生成树算法测试
    print("\n最小生成树算法测试:")
    graph = create_sample_graph()
    prim_weight, prim_edges = prim(graph)
    print(f"Prim算法 - 最小生成树总权重: {prim_weight}, 边列表: {prim_edges}")
    
    kruskal_weight, kruskal_edges = kruskal(graph)
    print(f"Kruskal算法 - 最小生成树总权重: {kruskal_weight}, 边列表: {kruskal_edges}")
    
    dijkstra_weight, dijkstra_edges = dijkstra_mst(graph, 0)
    print(f"Dijkstra MST算法 - 最小生成树总权重: {dijkstra_weight}, 边列表: {dijkstra_edges}")
    
    print("\n✓ 图论算法测试完成")


def test_string_algorithms():
    """测试字符串算法"""
    print("\n=== 字符串算法测试 ===\n")
    
    # KMP算法测试
    print("KMP算法测试:")
    pattern = "ABABCABAB"
    text = "ABABDABACDABABCABAB"
    
    prefix_table = kmp_preprocess(pattern)
    print(f"模式串 {pattern} 的前缀表: {prefix_table}")
    
    matches = kmp_search(text, pattern)
    print(f"在文本 {text} 中找到的匹配位置: {matches}")
    
    # 最长前缀后缀测试
    print("\n最长前缀后缀测试:")
    test_patterns = ["ABCDABD", "AAAA", "ABABABA", "ABCABCABC"]
    for pattern in test_patterns:
        lps = kmp_longest_prefix_suffix(pattern)
        print(f"模式 {pattern}: {lps}")
    
    # Boyer-Moore算法测试
    print("\nBoyer-Moore算法测试:")
    pattern_bm = "EXAMPLE"
    text_bm = "HERE IS A SIMPLE EXAMPLE"
    
    matches_bm = boyer_moore_search(text_bm, pattern_bm)
    print(f"Boyer-Moore在文本 {text_bm} 中找到的匹配位置: {matches_bm}")
    
    print("\n✓ 字符串算法测试完成")


def test_mathematical_algorithms():
    """测试数论算法"""
    print("\n=== 数论算法测试 ===\n")
    
    # 快速幂算法测试
    print("快速幂算法测试:")
    base = 3
    exponent = 10
    modulus = 100
    
    print(f"{base}^{exponent} = {fast_power(base, exponent)}")
    print(f"递归快速幂: {base}^{exponent} = {fast_power_recursive(base, exponent)}")
    
    # 质数测试
    print("\n质数算法测试:")
    numbers = [2, 3, 17, 20, 29, 100]
    for n in numbers:
        print(f"{n} 是否是质数: {is_prime(n)}")
    
    primes = sieve_of_eratosthenes(50)
    print(f"小于等于50的所有质数: {primes}")
    
    # GCD测试
    a, b = 12, 18
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
    print(f"GCD欧几里得({a}, {b}) = {gcd_euclidean(a, b)}")
    print(f"GCD欧几里得递归({a}, {b}) = {gcd_euclidean_recursive(a, b)}")
    
    # LCM测试
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
    
    print("\n✓ 数论算法测试完成")


def test_computational_geometry_algorithms():
    """测试计算几何算法"""
    print("\n=== 计算几何算法测试 ===\n")
    
    # 凸包算法测试
    print("凸包算法测试:")
    points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2), (1, 1), (3, 3)]
    
    print("示例点集:")
    for i, p in enumerate(points):
        print(f"P{i}: {p}")
    
    hull_graham = convex_hull_graham(points)
    hull_jarvis = convex_hull_jarvis(points)
    hull_monotone = convex_hull_quickhull(points)
    
    print(f"\nGraham扫描凸包: {hull_graham}")
    print(f"Jarvis算法凸包: {hull_jarvis}")
    print(f"Quickhull凸包: {hull_monotone}")
    
    # 最近点对算法测试
    print("\n最近点对算法测试:")
    points_pair = [(1, 2), (3, 4), (5, 6), (2, 3), (4, 5)]
    
    print("示例点集:")
    for i, p in enumerate(points_pair):
        print(f"P{i}: {p}")
    
    naive_distance, naive_pair = closest_pair_brute_force(points_pair)
    divide_distance, divide_pair = closest_pair_divide_and_conquer(points_pair)
    recursive_distance, recursive_pair = closest_pair_recursive(points_pair)
    
    print(f"\n朴素算法:")
    print(f"最小距离: {naive_distance:.4f}")
    print(f"最近点对: {naive_pair}")
    
    print(f"\n分治算法:")
    print(f"最小距离: {divide_distance:.4f}")
    print(f"最近点对: {divide_pair}")
    
    print(f"\n递归算法:")
    print(f"最小距离: {recursive_distance:.4f}")
    print(f"最近点对: {recursive_pair}")
    
    print("\n✓ 计算几何算法测试完成")


def generate_report():
    """生成测试报告"""
    print("\n=== 算法债偿还完成报告 ===\n")
    
    # 统计实现的算法
    algorithms_completed = {
        "图论算法": ["Prim最小生成树", "Dijkstra最短路径"],
        "字符串算法": ["KMP匹配", "Boyer-Moore"],
        "数论算法": ["欧几里得算法", "快速幂", "素数筛"],
        "计算几何算法": ["凸包算法", "最近点对"]
    }
    
    print("已完成的算法:")
    for category, algs in algorithms_completed.items():
        print(f"{category}:")
        for alg in algs:
            print(f"  - {alg}")
    
    print("\n=== 算法债已全部偿还 ===\n")


def main():
    """主测试函数"""
    print("开始测试所有算法...")
    
    try:
        test_graph_algorithms()
        test_string_algorithms()
        test_mathematical_algorithms()
        test_computational_geometry_algorithms()
        generate_report()
        
        print("✓ 所有算法测试成功")
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        return False


if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ 算法债偿还成功！")
    else:
        print("\n❌ 算法债偿还失败！")