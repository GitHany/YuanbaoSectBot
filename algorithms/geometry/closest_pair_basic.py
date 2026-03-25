"""
最近点对算法 - 基础实现
"""

import math


def distance(point1, point2):
    """
    计算两点之间的欧几里得距离

    参数:
        point1, point2: 点坐标 (x, y)

    返回:
        float: 两点之间的距离
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def distance(point1, point2):
    """
    计算两点之间的欧几里得距离

    参数:
        point1, point2: 点坐标 (x, y)

    返回:
        float: 两点之间的距离
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def closest_pair_brute_force(points):
    """
    暴力算法 - 寻找最近点对

    参数:
        points (list): 点列表 [(x1, y1), (x2, y2), ...]

    返回:
        tuple: (最小距离, 最近的两个点)

    时间复杂度: O(n²)
    """
    if len(points) < 2:
        return None

    min_distance = float("inf")
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair


def closest_pair_divide_and_conquer(points):
    """
    分治法 - 寻找最近点对

    参数:
        points (list): 点列表 [(x1, y1), (x2, y2), ...]

    返回:
        tuple: (最小距离, 最近的两个点)

    时间复杂度: O(n log n)
    """
    if len(points) <= 3:
        return closest_pair_brute_force(points)

    # 按照x坐标排序
    points_sorted_x = sorted(points, key=lambda p: p[0])

    def divide(points):
        n = len(points)
        if n <= 3:
            return closest_pair_brute_force(points)

        # 分割点集
        mid = n // 2
        left_points = points[:mid]
        right_points = points[mid:]

        # 递归处理左右两部分
        left_result = divide(left_points)
        right_result = divide(right_points)

        # 选择较小的距离
        min_dist = min(left_result[0], right_result[0])
        min_pair = (
            left_result[1] if left_result[0] < right_result[0] else right_result[1]
        )

        # 考虑跨越中线的点
        mid_x = points[mid][0]
        strip_points = []

        for point in points:
            if abs(point[0] - mid_x) < min_dist:
                strip_points.append(point)

        # 按照y坐标排序strip_points
        strip_points.sort(key=lambda p: p[1])

        # 检查strip_points中的点
        for i in range(len(strip_points)):
            for j in range(i + 1, len(strip_points)):
                if strip_points[j][1] - strip_points[i][1] > min_dist:
                    break

                dist = distance(strip_points[i], strip_points[j])
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (strip_points[i], strip_points[j])

        return min_dist, min_pair

    return divide(points_sorted_x)


def closest_pair_recursive(points):
    """
    递归分治法 - 寻找最近点对

    参数:
        points (list): 点列表

    返回:
        tuple: (最小距离, 最近的两个点)
    """
    # 预处理：按照x坐标排序
    points_x = sorted(points, key=lambda p: p[0])

    def closest_pair_recursive_helper(points_x):
        if len(points_x) <= 3:
            return closest_pair_brute_force(points_x)

        # 分割
        mid = len(points_x) // 2
        left_points = points_x[:mid]
        right_points = points_x[mid:]

        # 递归调用
        left_dist, left_pair = closest_pair_recursive_helper(left_points)
        right_dist, right_pair = closest_pair_recursive_helper(right_points)

        # 选择较小的距离
        min_dist = min(left_dist, right_dist)
        min_pair = left_pair if left_dist < right_dist else right_pair

        # 处理跨越中线的点
        mid_x = points_x[mid][0]
        strip_points = []

        for point in points_x:
            if abs(point[0] - mid_x) < min_dist:
                strip_points.append(point)

        # 按照y坐标排序strip_points
        strip_points.sort(key=lambda p: p[1])

        # 检查strip_points中的点
        for i in range(len(strip_points)):
            for j in range(i + 1, len(strip_points)):
                if strip_points[j][1] - strip_points[i][1] > min_dist:
                    break

                dist = distance(strip_points[i], strip_points[j])
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (strip_points[i], strip_points[j])

        return min_dist, min_pair

    return closest_pair_recursive_helper(points_x)
