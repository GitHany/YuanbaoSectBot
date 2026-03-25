"""
凸包算法 - 高级算法
"""

import math

from .convex_hull_basic import cross_product


def convex_hull_quickhull(points):
    """
    QuickHull算法 - 计算凸包

    参数:
        points (list): 点列表 [(x1, y1), (x2, y2), ...]

    返回:
        list: 凸包上的点列表

    时间复杂度: O(n log h)，h是凸包上的点数
    """
    if len(points) < 3:
        return points

    hull = []

    def find_hull(points, p1, p2, hull_points, side):
        if not points:
            return

        max_distance = -1
        farthest_point = None

        for point in points:
            distance = abs(cross_product(p1, p2, point))
            if distance > max_distance:
                max_distance = distance
                farthest_point = point

        if farthest_point:
            hull_points.append(farthest_point)

            # 分割点为两个集合
            left_points = []
            right_points = []

            for point in points:
                if point == farthest_point:
                    continue

                if cross_product(p1, farthest_point, point) > 0:
                    left_points.append(point)
                elif cross_product(farthest_point, p2, point) > 0:
                    right_points.append(point)

            find_hull(left_points, p1, farthest_point, hull_points, side)
            find_hull(right_points, farthest_point, p2, hull_points, side)

    # 找到最左边和最右边的点
    min_point = min(points, key=lambda p: p[0])
    max_point = max(points, key=lambda p: p[0])

    # 上部凸包
    upper_points = []
    lower_points = []

    for point in points:
        if point == min_point or point == max_point:
            continue

        if cross_product(min_point, max_point, point) > 0:
            upper_points.append(point)
        else:
            lower_points.append(point)

    hull.append(min_point)
    find_hull(upper_points, min_point, max_point, hull, 1)
    hull.append(max_point)
    find_hull(lower_points, max_point, min_point, hull, -1)

    return hull


def convex_hull_brute_force(points):
    """
    暴力算法 - 计算凸包

    参数:
        points (list): 点列表 [(x1, y1), (x2, y2), ...]

    返回:
        list: 凸包上的点列表

    时间复杂度: O(n^3)
    """
    if len(points) < 3:
        return points

    hull = []

    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue

            # 检查点i和j是否构成凸包边
            valid_edge = True

            for k in range(len(points)):
                if k == i or k == j:
                    continue

                cross = cross_product(points[i], points[j], points[k])
                if cross < 0:
                    valid_edge = False
                    break

            if valid_edge:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    # 按照顺时针方向排序
    center_x = sum(p[0] for p in hull) / len(hull)
    center_y = sum(p[1] for p in hull) / len(hull)
    hull.sort(key=lambda p: math.atan2(p[1] - center_y, p[0] - center_x))

    return hull


def convex_hull_performance_test():
    """
    测试不同凸包算法的性能

    返回:
        str: 性能测试结果
    """
    import time
    import random

    def generate_points(n):
        return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]

    test_sizes = [10, 50, 100, 500]
    algorithms = [
        ("Graham Scan", graham),
        ("Jarvis March", jarvis),
        ("QuickHull", quickhull),
        ("Brute Force", brute_force),
    ]

    results = []

    for n in test_sizes:
        points = generate_points(n)

        result_entry = {"n": n}
        for algo_name, algo_func in algorithms:
            if n > 100 and algo_name == "Brute Force":
                # 暴力算法太慢，跳过
                continue

            start_time = time.time()
            hull = algo_func(points)
            elapsed = time.time() - start_time

            result_entry[algo_name] = {"points": len(hull), "time": elapsed}

        results.append(result_entry)

    result_str = "凸包算法性能测试:\n"
    for entry in results:
        result_str += f"\n点数: {entry['n']}\n"
        for algo_name, data in entry.items():
            if algo_name != "n":
                result_str += f"{algo_name}: 凸包点数={data['points']}, 耗时={data['time']:.6f}s\n"

    return result_str
