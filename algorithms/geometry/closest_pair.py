"""
最近点对算法
包括：
1. 暴力算法 O(n²)
2. 分治法 O(n log n)
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
    
    min_distance = float('inf')
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
        min_pair = left_result[1] if left_result[0] < right_result[0] else right_result[1]
        
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


def closest_pair_kd_tree(points):
    """
    KD树算法 - 寻找最近点对
    
    参数:
        points (list): 点列表
    
    返回:
        tuple: (最小距离, 最近的两个点)
    """
    # KD树实现
    class KDTree:
        def __init__(self, point, axis):
            self.point = point
            self.axis = axis
            self.left = None
            self.right = None
        
        def insert(self, point, depth=0):
            axis = depth % 2  # 交替使用x和y轴
            if point[axis] < self.point[axis]:
                if self.left is None:
                    self.left = KDTree(point, axis)
                else:
                    self.left.insert(point, depth + 1)
            else:
                if self.right is None:
                    self.right = KDTree(point, axis)
                else:
                    self.right.insert(point, depth + 1)
        
        def nearest(self, target, depth=0):
            axis = depth % 2
            dist = distance(self.point, target)
            nearest_node = self
            nearest_dist = dist
            
            # 搜索左右子树
            if target[axis] < self.point[axis]:
                if self.left:
                    left_node, left_dist = self.left.nearest(target, depth + 1)
                    if left_dist < nearest_dist:
                        nearest_node = left_node
                        nearest_dist = left_dist
                
                # 检查右子树
                if self.right and abs(target[axis] - self.point[axis]) < nearest_dist:
                    right_node, right_dist = self.right.nearest(target, depth + 1)
                    if right_dist < nearest_dist:
                        nearest_node = right_node
                        nearest_dist = right_dist
            else:
                if self.right:
                    right_node, right_dist = self.right.nearest(target, depth + 1)
                    if right_dist < nearest_dist:
                        nearest_node = right_node
                        nearest_dist = right_dist
                
                # 检查左子树
                if self.left and abs(target[axis] - self.point[axis]) < nearest_dist:
                    left_node, left_dist = self.left.nearest(target, depth + 1)
                    if left_dist < nearest_dist:
                        nearest_node = left_node
                        nearest_dist = left_dist
            
            return nearest_node, nearest_dist
    
    # 构建KD树
    root = KDTree(points[0], 0)
    for point in points[1:]:
        root.insert(point)
    
    # 为每个点寻找最近邻
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        nearest_node, nearest_dist = root.nearest(points[i])
        if nearest_dist < min_dist and nearest_node.point != points[i]:
            min_dist = nearest_dist
            closest_pair = (points[i], nearest_node.point)
    
    return min_dist, closest_pair


def closest_pair_performance_test():
    """
    测试不同最近点对算法的性能
    
    返回:
        str: 性能测试结果
    """
    import time
    import random
    
    # 生成随机点集
    def generate_points(n):
        return [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(n)]
    
    test_sizes = [10, 50, 100, 500, 1000]
    algorithms = [
        ("暴力算法", closest_pair_brute_force),
        ("分治法", closest_pair_divide_and_conquer),
        ("递归分治法", closest_pair_recursive),
        ("KD树算法", closest_pair_kd_tree)
    ]
    
    results = []
    
    for n in test_sizes:
        points = generate_points(n)
        
        result_entry = {"n": n}
        for algo_name, algo_func in algorithms:
            if n > 200 and algo_name == "暴力算法":
                # 暴力算法太慢，跳过
                continue
            
            start_time = time.time()
            try:
                result = algo_func(points)
                elapsed = time.time() - start_time
                
                if result:
                    result_entry[algo_name] = {
                        "distance": result[0],
                        "time": elapsed
                    }
            except Exception as e:
                result_entry[algo_name] = {
                    "error": str(e),
                    "time": elapsed
                }
        
        results.append(result_entry)
    
    result_str = "最近点对算法性能测试:\n"
    for entry in results:
        result_str += f"\n点数: {entry['n']}\n"
        for algo_name, data in entry.items():
            if algo_name != "n":
                if "distance" in data:
                    result_str += f"{algo_name}: 最小距离={data['distance']:.2f}, 耗时={data['time']:.6f}s\n"
                else:
                    result_str += f"{algo_name}: 错误={data['error']}, 耗时={data['time']:.6f}s\n"
    
    return result_str


def closest_pair_visualize(points, pair):
    """
    可视化最近点对
    
    参数:
        points (list): 点列表
        pair (tuple): 最近的两个点
    
    返回:
        str: 可视化结果
    """
    if not pair:
        return "没有找到最近点对"
    
    min_distance, closest_points = pair
    
    result = f"""
最近点对可视化:
所有点数量: {len(points)}
最小距离: {min_distance:.2f}
最近点对: ({closest_points[0][0]}, {closest_points[0][1]}), ({closest_points[1][0]}, {closest_points[1][1]})
"""
    
    # 列出所有点
    result += f"\n所有点坐标:\n"
    for i, point in enumerate(points):
        result += f"点{i}: ({point[0]}, {point[1]})\n"
    
    # 标记最近点对
    result += f"\n最近点对用*标记:\n"
    for i, point in enumerate(points):
        if point == closest_points[0] or point == closest_points[1]:
            result += f"*点{i}: ({point[0]}, {point[1]})\n"
        else:
            result += f"点{i}: ({point[0]}, {point[1]})\n"
    
    return result


def closest_pair_all_points(points):
    """
    计算所有点到最近邻的距离
    
    参数:
        points (list): 点列表
    
    返回:
        list: 每个点到最近邻的距离
    """
    distances = []
    for i, point in enumerate(points):
        # 找到除自己之外的最近邻
        min_dist = float('inf')
        closest_point = None
        
        for j, other_point in enumerate(points):
            if i == j:
                continue
            
            dist = distance(point, other_point)
            if dist < min_dist:
                min_dist = dist
                closest_point = other_point
        
        distances.append(min_dist)
    
    return distances


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
        print(f"最近点对: {brute_pair}")
    
    # 分治法
    divide_result = closest_pair_divide_and_conquer(test_points)
    if divide_result:
        divide_distance, divide_pair = divide_result
        print(f"分治法最小距离: {divide_distance:.2f}")
        print(f"最近点对: {divide_pair}")
    
    # 递归分治法
    recursive_result = closest_pair_recursive(test_points)
    if recursive_result:
        recursive_distance, recursive_pair = recursive_result
        print(f"递归分治法最小距离: {recursive_distance:.2f}")
        print(f"最近点对: {recursive_pair}")
    
    # KD树算法
    kd_tree_result = closest_pair_kd_tree(test_points)
    if kd_tree_result:
        kd_tree_distance, kd_tree_pair = kd_tree_result
        print(f"KD树算法最小距离: {kd_tree_distance:.2f}")
        print(f"最近点对: {kd_tree_pair}")
    
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
    
    # 复杂测试
    complex_points = [
        (100, 200), (150, 250), (200, 300), (250, 350), (300, 400),
        (350, 450), (400, 500), (450, 550), (500, 600), (550, 650),
        (600, 700), (650, 750), (700, 800), (750, 850), (800, 900),
        (850, 950), (900, 1000), (950, 1050), (1000, 1100), (1050, 1150)
    ]
    
    print("\n复杂点集最近点对测试:")
    complex_result = closest_pair_divide_and_conquer(complex_points)
    if complex_result:
        complex_distance, complex_pair = complex_result
        print(f"点数: {len(complex_points)}")
        print(f"最小距离: {complex_distance:.2f}")
        print(f"最近点对: {complex_pair}")
        print("\n" + closest_pair_visualize(complex_points, complex_result))