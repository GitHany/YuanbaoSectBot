"""
凸包算法
包括：
1. Graham Scan算法
2. Jarvis March算法
3. QuickHull算法
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
    
    # 找到最左边和最右边的点
    min_point = min(points, key=lambda p: p[0])
    max_point = max(points, key=lambda p: p[0])
    
    hull = []
    
    # 递归找到上部和下部凸包
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


def convex_hull_performance_test():
    """
    测试不同凸包算法的性能
    
    返回:
        str: 性能测试结果
    """
    import time
    import random
    
    # 生成随机点集
    def generate_points(n):
        return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]
    
    test_sizes = [10, 50, 100, 500]
    algorithms = [
        ("Graham Scan", convex_hull_graham),
        ("Jarvis March", convex_hull_jarvis),
        ("QuickHull", convex_hull_quickhull),
        ("Brute Force", convex_hull_brute_force)
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
            
            result_entry[algo_name] = {
                "points": len(hull),
                "time": elapsed
            }
        
        results.append(result_entry)
    
    result_str = "凸包算法性能测试:\n"
    for entry in results:
        result_str += f"\n点数: {entry['n']}\n"
        for algo_name, data in entry.items():
            if algo_name != "n":
                result_str += f"{algo_name}: 凸包点数={data['points']}, 耗时={data['time']:.6f}s\n"
    
    return result_str


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


if __name__ == "__main__":
    # 测试数据
    test_points = [
        (0, 0), (1, 2), (2, 1), (3, 3), (4, 1),
        (5, 0), (6, 2), (7, 4), (8, 1), (9, 0),
        (10, 3), (11, 2), (12, 1), (13, 5), (14, 3)
    ]
    
    print("凸包算法测试:")
    
    # Graham Scan算法
    graham_hull = convex_hull_graham(test_points)
    print(f"Graham Scan凸包点数: {len(graham_hull)}")
    print(f"Graham Scan凸包点: {graham_hull}")
    
    # Jarvis March算法
    jarvis_hull = convex_hull_jarvis(test_points)
    print(f"Jarvis March凸包点数: {len(jarvis_hull)}")
    print(f"Jarvis March凸包点: {jarvis_hull}")
    
    # QuickHull算法
    quickhull_hull = convex_hull_quickhull(test_points)
    print(f"QuickHull凸包点数: {len(quickhull_hull)}")
    print(f"QuickHull凸包点: {quickhull_hull}")
    
    # 验证三种算法是否得到相同结果
    graham_set = set(graham_hull)
    jarvis_set = set(jarvis_hull)
    quickhull_set = set(quickhull_hull)
    
    if graham_set == jarvis_set and jarvis_set == quickhull_set:
        print("\n✓ 三种算法得到相同的凸包点")
    else:
        print("\n✗ 三种算法得到不同的凸包点")
    
    # 可视化
    print("\n" + convex_hull_visualize(test_points, graham_hull))
    
    # 性能测试
    print("\n" + convex_hull_performance_test())
    
    # 计算凸包距离
    distances = convex_hull_distance(graham_hull)
    print(f"\n凸包相邻点距离:")
    for i, dist in enumerate(distances):
        print(f"点{i}到点{i+1}: {dist:.2f}")
    
    print(f"凸包周长: {sum(distances):.2f}")
    
    # 复杂测试
    complex_points = [
        (0, 0), (1, 5), (2, 2), (3, 7), (4, 1),
        (5, 6), (6, 3), (7, 4), (8, 8), (9, 0),
        (10, 9), (11, 1), (12, 6), (13, 3), (14, 7),
        (15, 2), (16, 10), (17, 0), (18, 5), (19, 4)
    ]
    
    print("\n复杂点集凸包测试:")
    complex_hull = convex_hull_graham(complex_points)
    print(f"点数: {len(complex_points)}")
    print(f"凸包点数: {len(complex_hull)}")
    print(f"凸包点: {complex_hull}")
    print("\n" + convex_hull_visualize(complex_points, complex_hull))