"""
凸包算法模块
"""

import math

from .convex_hull_basic import (
    convex_hull_graham,
    convex_hull_jarvis,
    convex_hull_distance,
    convex_hull_visualize,
)
from .convex_hull_advanced import (
    convex_hull_quickhull,
    convex_hull_brute_force,
    convex_hull_performance_test,
)


def cross_product(o, a, b):
    """
    计算向量OA和OB的叉积

    参数:
        o, a, b: 点坐标 (x, y)

    返回:
        float: 叉积的值，表示相对角度
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


if __name__ == "__main__":
    # 测试数据
    test_points = [
        (0, 0),
        (1, 2),
        (2, 1),
        (3, 3),
        (4, 1),
        (5, 0),
        (6, 2),
        (7, 4),
        (8, 1),
        (9, 0),
        (10, 3),
        (11, 2),
        (12, 1),
        (13, 5),
        (14, 3),
    ]

    print("凸包算法测试:")

    # Graham Scan算法
    graham_hull = convex_hull_graham(test_points)
    print(f"Graham Scan凸包点数: {len(graham_hull)}")

    # Jarvis March算法
    jarvis_hull = convex_hull_jarvis(test_points)
    print(f"Jarvis March凸包点数: {len(jarvis_hull)}")

    # QuickHull算法
    quickhull_hull = convex_hull_quickhull(test_points)
    print(f"QuickHull凸包点数: {len(quickhull_hull)}")

    # 验证三种算法是否得到相同结果
    graham_set = set(graham_hull)
    jarvis_set = set(jarvis_hull)
    quickhull_set = set(quickhull_hull)

    if graham_set == jarvis_set and jarvis_set == quickhull_set:
        print("✓ 三种算法得到相同的凸包点")
    else:
        print("✗ 三种算法得到不同的凸包点")

    # 可视化
    print("\n" + convex_hull_visualize(test_points, graham_hull))

    # 计算凸包距离
    distances = convex_hull_distance(graham_hull)
    print(f"凸包周长: {sum(distances):.2f}")

    # 性能测试
    print("\n" + convex_hull_performance_test())
