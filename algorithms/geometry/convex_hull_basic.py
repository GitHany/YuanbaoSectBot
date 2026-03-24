"""
凸包算法 - 基础实现
"""

import math


def cross_product(o, a, b):
    """
    计算向量OA和OB的叉积
    
    参数:
        o, a, b: 点坐标 (x, y)
    
    返回:
        float: 叉积的值，表示相对角度
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull_graham(points):
    """
    Graham Scan算法 - 计算凸包
    
    参数:
        points (list): 点列表 [(x1, y1), (x2, y2), ...]
    
    返回:
        list: 凸包上的点列表
    
    时间复杂度: O(n log n)
    """
    if len(points) < 3:
        return points
    
    # 找到最左下角的点
    min_point = min(points, key=lambda p: (p[0], p[1]))
    
    # 排序所有点，按极角大小排序
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1] - min_point[1], p[0] - min_point[0]), p[0], p[1]))
    
    # Graham Scan算法
    hull = []
    
    for point in sorted_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    
    return hull


def convex_hull_jarvis(points):
    """
    Jarvis March算法 - 计算凸包
    
    参数:
        points (list): 点列表 [(x1, y1), (x2, y2), ...]
    
    返回:
        list: 凸包上的点列表
    
    时间复杂度: O(n * h)，h是凸包上的点数
    """
    if len(points) < 3:
        return points
    
    hull = []
    
    # 找到最左边的点
    leftmost = min(points, key=lambda p: p[0])
    hull.append(leftmost)
    
    current = leftmost
    
    while True:
        next_point = points[0]
        
        for point in points:
            if point == current:
                continue
            
            cross = cross_product(current, next_point, point)
            if cross < 0:
                next_point = point
            elif cross == 0:
                # 如果三点共线，选择距离更远的点
                dist_next = math.sqrt((next_point[0] - current[0]) ** 2 + (next_point[1] - current[1]) ** 2)
                dist_point = math.sqrt((point[0] - current[0]) ** 2 + (point[1] - current[1]) ** 2)
                if dist_point > dist_next:
                    next_point = point
        
        if next_point == hull[0]:
            break
        
        hull.append(next_point)
        current = next_point
    
    return hull


def convex_hull_distance(points):
    """
    计算凸包中相邻点的距离
    
    参数:
        points (list): 凸包上的点
    
    返回:
        list: 相邻点之间的距离列表
    """
    distances = []
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distances.append(distance)
    return distances


def convex_hull_visualize(points, hull_points):
    """
    可视化凸包
    
    参数:
        points (list): 所有点
        hull_points (list): 凸包点
    
    返回:
        str: 可视化结果
    """
    result = f"""
凸包可视化:
所有点数量: {len(points)}
凸包点数量: {len(hull_points)}
"""
    
    # 列出所有点
    result += f"\n所有点坐标:\n"
    for i, point in enumerate(points):
        result += f"点{i}: ({point[0]}, {point[1]})\n"
    
    # 列出凸包点
    result += f"\n凸包点坐标:\n"
    for i, point in enumerate(hull_points):
        result += f"凸包点{i}: ({point[0]}, {point[1]})\n"
    
    # 凸包面积
    if len(hull_points) >= 3:
        area = 0
        for i in range(len(hull_points)):
            x1, y1 = hull_points[i]
            x2, y2 = hull_points[(i + 1) % len(hull_points)]
            area += x1 * y2 - x2 * y1
        area = abs(area) / 2
        result += f"凸包面积: {area}\n"
    
    return result