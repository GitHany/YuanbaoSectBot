"""
最近点对算法 - KD树算法
"""

import math

from .closest_pair_basic import distance


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


def closest_pair_kd_tree(points):
    """
    KD树算法 - 寻找最近点对

    参数:
        points (list): 点列表

    返回:
        tuple: (最小距离, 最近的两个点)
    """
    if len(points) < 2:
        return None

    # 构建KD树
    root = KDTree(points[0], 0)
    for point in points[1:]:
        root.insert(point)

    # 为每个点寻找最近邻
    min_dist = float("inf")
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

    def generate_points(n):
        return [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(n)]

    test_sizes = [10, 50, 100, 500, 1000]
    algorithms = [
        ("暴力算法", brute_force),
        ("分治法", divide_and_conquer),
        ("递归分治法", recursive),
        ("KD树算法", kd_tree),
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
                    result_entry[algo_name] = {"distance": result[0], "time": elapsed}
            except Exception as e:
                result_entry[algo_name] = {"error": str(e), "time": elapsed}

        results.append(result_entry)

    result_str = "最近点对算法性能测试:\n"
    for entry in results:
        result_str += f"\n点数: {entry['n']}\n"
        for algo_name, data in entry.items():
            if algo_name != "n":
                if "distance" in data:
                    result_str += f"{algo_name}: 最小距离={data['distance']:.2f}, 耗时={data['time']:.6f}s\n"
                else:
                    result_str += (
                        f"{algo_name}: 错误={data['error']}, 耗时={data['time']:.6f}s\n"
                    )

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
        min_dist = float("inf")
        closest_point = None

        for j, other_point in enumerate(points):
            if i == j:
                continue

            dist = distance(point, other_point)
            if dist < min_dist:
                min_dist = dist

        distances.append(min_dist)

    return distances
