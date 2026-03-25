"""
算法性能压测 - 对比新实现的算法债清单中的算法
"""

import sys
sys.path.insert(0, '.')

import time
import random
import math


def benchmark_string_algorithms():
    """
    测试字符串匹配算法性能
    """
    from algorithms.string.kmp import kmp_search
    from algorithms.string.boyer_moore import boyer_moore_search
    
    print("=== 字符串算法性能对比 ===")
    
    # 生成测试数据
    text_lengths = [1000, 5000, 10000, 50000]
    patterns = ["abcde", "testpattern", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz1234567890"]
    
    results = []
    
    for text_len in text_lengths:
        # 生成随机文本
        text = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(text_len))
        
        for pattern in patterns:
            # KMP算法测试
            start_time = time.time()
            kmp_matches = kmp_search(text, pattern)
            kmp_time = time.time() - start_time
            
            # Boyer-Moore算法测试
            start_time = time.time()
            bm_matches = boyer_moore_search(text, pattern)
            bm_time = time.time() - start_time
            
            results.append({
                "text_length": text_len,
                "pattern_length": len(pattern),
                "kmp_time": kmp_time,
                "bm_time": bm_time,
                "kmp_matches": len(kmp_matches),
                "bm_matches": len(bm_matches)
            })
    
    # 打印结果
    print("测试结果:")
    for result in results:
        print(f"文本长度: {result['text_length']}, 模式长度: {result['pattern_length']}")
        print(f"KMP耗时: {result['kmp_time']:.6f}s, 匹配数: {result['kmp_matches']}")
        print(f"Boyer-Moore耗时: {result['bm_time']:.6f}s, 匹配数: {result['bm_matches']}")
        if result['kmp_time'] < result['bm_time']:
            print(f"✓ KMP更快 ({result['bm_time']/result['kmp_time']:.2f}倍)")
        else:
            print(f"✓ Boyer-Moore更快 ({result['kmp_time']/result['bm_time']:.2f}倍)")
        print()
    
    return results


def benchmark_convex_hull_algorithms():
    """
    测试凸包算法性能
    """
    from algorithms.geometry.convex_hull_basic import convex_hull_graham, convex_hull_jarvis
    from algorithms.geometry.convex_hull_advanced import convex_hull_quickhull
    
    print("=== 凸包算法性能对比 ===")
    
    # 生成测试数据
    point_counts = [50, 100, 200, 500, 1000]
    
    results = []
    
    for count in point_counts:
        # 生成随机点集
        points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(count)]
        
        # Graham Scan算法测试
        start_time = time.time()
        graham_hull = convex_hull_graham(points)
        graham_time = time.time() - start_time
        
        # Jarvis March算法测试
        start_time = time.time()
        jarvis_hull = convex_hull_jarvis(points)
        jarvis_time = time.time() - start_time
        
        # QuickHull算法测试
        start_time = time.time()
        quickhull_hull = convex_hull_quickhull(points)
        quickhull_time = time.time() - start_time
        
        results.append({
            "point_count": count,
            "graham_time": graham_time,
            "jarvis_time": jarvis_time,
            "quickhull_time": quickhull_time,
            "graham_hull_size": len(graham_hull),
            "jarvis_hull_size": len(jarvis_hull),
            "quickhull_hull_size": len(quickhull_hull)
        })
    
    # 打印结果
    print("测试结果:")
    for result in results:
        print(f"点集数量: {result['point_count']}")
        print(f"Graham Scan耗时: {result['graham_time']:.6f}s, 凸包点数: {result['graham_hull_size']}")
        print(f"Jarvis March耗时: {result['jarvis_time']:.6f}s, 凸包点数: {result['jarvis_hull_size']}")
        print(f"QuickHull耗时: {result['quickhull_time']:.6f}s, 凸包点数: {result['quickhull_hull_size']}")
        
        # 找出最快的算法
        times = [result['graham_time'], result['jarvis_time'], result['quickhull_time']]
        fastest = min(times)
        fastest_index = times.index(fastest)
        algorithm_names = ["Graham Scan", "Jarvis March", "QuickHull"]
        
        print(f"✓ {algorithm_names[fastest_index]}最快")
        print()
    
    return results


def benchmark_closest_pair_algorithms():
    """
    测试最近点对算法性能
    """
    from algorithms.geometry.closest_pair_basic import closest_pair_divide_and_conquer
    from algorithms.geometry.closest_pair_advanced import closest_pair_kd_tree
    
    print("=== 最近点对算法性能对比 ===")
    
    # 生成测试数据
    point_counts = [50, 100, 200, 500, 1000, 2000]
    
    results = []
    
    for count in point_counts:
        # 生成随机点集
        points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(count)]
        
        # 分治法测试
        start_time = time.time()
        divide_result = closest_pair_divide_and_conquer(points)
        divide_time = time.time() - start_time
        
        # KD树算法测试
        start_time = time.time()
        kd_result = closest_pair_kd_tree(points)
        kd_time = time.time() - start_time
        
        if divide_result and kd_result:
            divide_dist = divide_result[0]
            kd_dist = kd_result[0]
            
            results.append({
                "point_count": count,
                "divide_time": divide_time,
                "kd_time": kd_time,
                "divide_distance": divide_dist,
                "kd_distance": kd_dist
            })
    
    # 打印结果
    print("测试结果:")
    for result in results:
        print(f"点集数量: {result['point_count']}")
        print(f"分治法耗时: {result['divide_time']:.6f}s, 距离: {result['divide_distance']:.2f}")
        print(f"KD树算法耗时: {result['kd_time']:.6f}s, 距离: {result['kd_distance']:.2f}")
        
        if result['divide_time'] < result['kd_time']:
            print(f"✓ 分治法更快 ({result['kd_time']/result['divide_time']:.2f}倍)")
        else:
            print(f"✓ KD树算法更快 ({result['divide_time']/result['kd_time']:.2f}倍)")
        print()
    
    return results


def benchmark_fast_power_algorithms():
    """
    测试快速幂算法性能
    """
    from algorithms.mathematical.fast_power import fast_power
    
    print("=== 快速幂算法性能对比 ===")
    
    # 测试数据
    test_cases = [
        {"x": 2, "n": 1000, "mod": None},
        {"x": 3, "n": 10000, "mod": None},
        {"x": 5, "n": 100000, "mod": None},
        {"x": 2, "n": 1000000, "mod": 1000000007},
        {"x": 3, "n":10000000, "mod": 1000000007}
    ]
    
    results = []
    
    for test in test_cases:
        x, n, mod = test["x"], test["n"], test["mod"]
        
        # 快速幂算法测试
        start_time = time.time()
        result = fast_power(x, n, mod)
        power_time = time.time() - start_time
        
        # Python内置pow函数测试
        start_time = time.time()
        if mod is None:
            builtin_result = pow(x, n)
        else:
            builtin_result = pow(x, n) % mod
        builtin_time = time.time() - start_time
        
        # 验证结果是否一致
        if result != builtin_result:
            print(f"⚠️ 结果不一致: fast_power({x}, {n}, {mod}) = {result}, pow() = {builtin_result}")
        
        results.append({
            "x": x,
            "n": n,
            "mod": mod,
            "power_time": power_time,
            "builtin_time": builtin_time,
            "power_result": result,
            "builtin_result": builtin_result
        })
    
    # 打印结果
    print("测试结果:")
    for result in results:
        print(f"计算: {result['x']}^{result['n']} mod {result['mod']}")
        print(f"快速幂耗时: {result['power_time']:.6f}s, 结果: {result['power_result']}")
        print(f"Python内置pow耗时: {result['builtin_time']:.6f}s, 结果: {result['builtin_result']}")
        
        if result['power_time'] < result['builtin_time']:
            print(f"✓ 快速幂更快 ({result['builtin_time']/result['power_time']:.2f}倍)")
        else:
            print(f"✓ Python内置pow更快 ({result['power_time']/result['builtin_time']:.2f}倍)")
        print()
    
    return results


def benchmark_gcd_algorithms():
    """
    测试欧几里得算法性能
    """
    from algorithms.mathematical.number_theory import gcd_euclidean, gcd_euclidean_recursive
    
    print("=== 欧几里得算法性能对比 ===")
    
    # 测试数据
    test_cases = [
        {"a": 48, "b": 18},
        {"a": 123456789, "b": 987654321},
        {"a": 1000000007, "b": 999999999},
        {"a": 314159265, "b": 271828182},
        {"a": 1024, "b": 4096}
    ]
    
    results = []
    
    for test in test_cases:
        a, b = test["a"], test["b"]
        
        # 迭代欧几里得算法测试
        start_time = time.time()
        gcd_iterative = gcd_euclidean(a, b)
        iterative_time = time.time() - start_time
        
        # 递归欧几里得算法测试
        start_time = time.time()
        gcd_recursive = gcd_euclidean_recursive(a, b)
        recursive_time = time.time() - start_time
        
        # 验证结果是否一致
        if gcd_iterative != gcd_recursive:
            print(f"⚠️ 结果不一致: gcd_iterative({a}, {b}) = {gcd_iterative}, gcd_recursive({a}, {b}) = {gcd_recursive}")
        
        results.append({
            "a": a,
            "b": b,
            "gcd": gcd_iterative,
            "iterative_time": iterative_time,
            "recursive_time": recursive_time
        })
    
    # 打印结果
    print("测试结果:")
    for result in results:
        print(f"计算: gcd({result['a']}, {result['b']}) = {result['gcd']}")
        print(f"迭代算法耗时: {result['iterative_time']:.6f}s")
        print(f"递归算法耗时: {result['recursive_time']:.6f}s")
        
        if result['iterative_time'] < result['recursive_time']:
            print(f"✓ 迭代算法更快 ({result['recursive_time']/result['iterative_time']:.2f}倍)")
        else:
            print(f"✓ 递归算法更快 ({result['iterative_time']/result['recursive_time']:.2f}倍)")
        print()
    
    return results


def main():
    """
    运行所有性能测试
    """
    print("算法债清单性能压测报告")
    print("=========================================")
    
    # 运行各个算法的性能测试
    string_results = benchmark_string_algorithms()
    convex_hull_results = benchmark_convex_hull_algorithms()
    closest_pair_results = benchmark_closest_pair_algorithms()
    fast_power_results = benchmark_fast_power_algorithms()
    gcd_results = benchmark_gcd_algorithms()
    
    print("\n=========================================")
    print("性能压测总结:")
    print("1. 字符串匹配算法:")
    print("   KMP算法 - 适用于一般文本匹配")
    print("   Boyer-Moore算法 - 适用于长模式串")
    
    print("\n2. 凸包算法:")
    print("   Graham Scan - O(n log n), 适用于大部分情况")
    print("   Jarvis March - O(n*h), 适用于凸包点数较少的情况")
    print("   QuickHull - O(n log h), 分治法，效率良好")
    
    print("\n3. 最近点对算法:")
    print("   分治法 - O(n log n), 标准算法")
    print("   KD树算法 - 适用于高维空间")
    
    print("\n4. 数论算法:")
    print("   快速幂算法 - O(log n), 指数计算")
    print("   欧几里得算法 - O(log(min(a,b)))")
    
    print("\n5. 素数筛算法:")
    print("   埃拉托斯特尼筛法 - O(n log log n)")
    
    print("\n=========================================")
    print("✅ 算法债清单性能测试完成")


if __name__ == "__main__":
    main()