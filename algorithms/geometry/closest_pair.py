"""
最近点对算法模块
"""

from .closest_pair_basic import (
    distance,
    closest_pair_brute_force,
    closest_pair_divide_and_conquer,
    closest_pair_recursive
)

from .closest_pair_advanced import (
    KDTree,
    closest_pair_kd_tree,
    closest_pair_performance_test,
    closest_pair_visualize,
    closest_pair_all_points
)


if __name__ == "__main__":
    # 测试数据
    test_points = [
        (1, 2), (3, 4), (5, 6), (2, 3), (4, 5),
        (6, 7), (3, 2), (5, 4), (7, 6), (1, 5),
        (2, 7), (4, 1), (6, 2), (7, 3), (8, 5)
    ]
    
    print("最近点对算法测试:")
    
    # 暴力算法
    brute_result = closest_pair_brute_force(test_points)
    if brute_result:
        brute_distance, brute_pair = brute_result
        print(f"暴力算法最小距离: {brute_distance:.2f}")
    
    # 分治法
    divide_result = closest_pair_divide_and_conquer(test_points)
    if divide_result:
        divide_distance, divide_pair = divide_result
        print(f"分治法最小距离: {divide_distance:.2f}")
    
    # 递归分治法
    recursive_result = closest_pair_recursive(test_points)
    if recursive_result:
        recursive_distance, recursive_pair = recursive_result
        print(f"递归分治法最小距离: {recursive_distance:.2f}")
    
    # KD树算法
    kd_tree_result = closest_pair_kd_tree(test_points)
    if kd_tree_result:
        kd_tree_distance, kd_tree_pair = kd_tree_result
        print(f"KD树算法最小距离: {kd_tree_distance:.2f}")
    
    # 验证所有算法是否得到相同结果
    all_results = [brute_result, divide_result, recursive_result, kd_tree_result]
    distances = [result[0] for result in all_results if result]
    
    if len(distances) > 0 and all(distances[0] == d for d in distances):
        print("\n✓ 所有算法得到相同的最小距离")
    else:
        print("\n✗ 算法结果不一致")
    
    # 可视化
    print("\n" + closest_pair_visualize(test_points, brute_result))
    
    # 性能测试
    print("\n" + closest_pair_performance_test())
    
    # 计算所有点到最近邻的距离
    print("\n每个点到最近邻的距离:")
    point_distances = closest_pair_all_points(test_points)
    for i, dist in enumerate(point_distances):
        print(f"点{i}: ({test_points[i][0]}, {test_points[i][1]}) 最近邻距离: {dist:.2f}")