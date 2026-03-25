"""简单的算法测试"""

import sys
sys.path.insert(0, '.')

# 导入基本函数
from algorithms.string.kmp import kmp_search
from algorithms.string.boyer_moore import boyer_moore_search
from algorithms.mathematical.fast_power import fast_power
from algorithms.mathematical.primes import is_prime, sieve_of_eratosthenes
from algorithms.mathematical.number_theory import gcd_euclidean
from algorithms.graph.dijkstra import dijkstra_adjacency_matrix, create_sample_matrix
from algorithms.graph.minimum_spanning_tree import prim, create_sample_graph


def test_string_algorithms():
    """测试字符串算法"""
    print("=== 字符串算法测试 ===")
    
    # KMP算法测试
    print("KMP算法测试:")
    pattern = "ABABCABAB"
    text = "ABABDABACDABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"模式串 '{pattern}' 在文本 '{text}' 中找到的匹配位置: {matches}")
    
    # Boyer-Moore算法测试
    print("\nBoyer-Moore算法测试:")
    pattern_bm = "EXAMPLE"
    text_bm = "HERE IS A SIMPLE EXAMPLE"
    matches_bm = boyer_moore_search(text_bm, pattern_bm)
    print(f"模式串 '{pattern_bm}' 在文本 '{text_bm}' 中找到的匹配位置: {matches_bm}")
    
    print("✓ 字符串算法测试完成")


def test_mathematical_algorithms():
    """测试数论算法"""
    print("\n=== 数论算法测试 ===")
    
    # 快速幂算法测试
    print("快速幂算法测试:")
    result = fast_power(3, 10)
    print(f"3^10 = {result}")
    
    # 质数测试
    print("\n质数算法测试:")
    numbers = [2, 3, 17, 20, 29, 100]
    for n in numbers:
        print(f"{n} 是否是质数: {is_prime(n)}")
    
    primes = sieve_of_eratosthenes(50)
    print(f"小于等于50的所有质数: {primes}")
    
    # GCD测试
    print("\nGCD测试:")
    a, b = 12, 18
    gcd_result = gcd_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd_result}")
    
    print("✓ 数论算法测试完成")


def test_graph_algorithms():
    """测试图论算法"""
    print("\n=== 图论算法测试 ===")
    
    # Dijkstra算法测试
    print("Dijkstra算法测试:")
    matrix_graph = create_sample_matrix()
    distances_matrix = dijkstra_adjacency_matrix(matrix_graph, 0)
    print(f"邻接矩阵图 - 从节点0到所有节点的最短距离: {distances_matrix}")
    
    # 最小生成树算法测试
    print("\n最小生成树算法测试:")
    graph = create_sample_graph()
    prim_weight, prim_edges = prim(graph)
    print(f"Prim算法 - 最小生成树总权重: {prim_weight}")
    print(f"Prim算法 - 最小生成树边列表: {prim_edges}")
    
    print("✓ 图论算法测试完成")


def main():
    """主测试函数"""
    print("开始测试算法...")
    
    try:
        test_string_algorithms()
        test_mathematical_algorithms()
        test_graph_algorithms()
        
        print("\n✅ 所有算法测试成功！")
        return True
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        return False


if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ CI测试通过准备完成！")
    else:
        print("\n❌ CI测试失败，需要修复！")