"""
Dijkstra最短路径算法
时间复杂度: O(V²) 或 O(E + V log V) 取决于实现
"""

import heapq


def dijkstra_adjacency_matrix(graph, start):
    """
    Dijkstra算法 - 邻接矩阵实现

    参数:
        graph (list): 邻接矩阵表示的图
        start (int): 起始节点

    返回:
        list: 从起始节点到所有节点的最短距离
    """
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    visited = [False] * n

    # 循环n次
    for _ in range(n):
        # 找到未访问节点中距离最小的节点
        min_distance = float("inf")
        min_node = -1

        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_node = v

        if min_node == -1:
            break

        visited[min_node] = True

        # 更新距离
        for v in range(n):
            if graph[min_node][v] > 0:  # 有边
                new_distance = distances[min_node] + graph[min_node][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    return distances


def dijkstra_adjacency_list(graph, start):
    """
    Dijkstra算法 - 邻接列表实现（使用堆优化）

    参数:
        graph (dict): 邻接列表表示的图 {节点: [(邻居, 权重)]}
        start (int): 起始节点

    返回:
        dict: 从起始节点到所有节点的最短距离
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # 优先队列
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # 如果当前距离大于已知距离，跳过
        if current_distance > distances[current_node]:
            continue

        # 遍历邻居
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances


def dijkstra_with_path(graph, start, end):
    """
    Dijkstra算法 - 返回最短路径

    参数:
        graph (dict): 邻接列表表示的图
        start (int): 起始节点
        end (int): 目标节点

    返回:
        tuple: (最短距离, 最短路径)
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        # 如果到达目标节点，可以提前退出
        if current_node == end:
            break

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    # 构建路径
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()

    return distances[end], path


def create_sample_graph():
    """
    创建示例图

    返回:
        dict: 邻接列表表示的图
    """
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 1), (4, 3)],
        2: [(0, 1), (1, 2), (3, 5)],
        3: [(1, 1), (2, 5), (4, 2), (5, 4)],
        4: [(1, 3), (3, 2), (5, 3)],
        5: [(3, 4), (4, 3)],
    }
    return graph


def create_sample_matrix():
    """
    创建示例邻接矩阵

    返回:
        list: 邻接矩阵
    """
    # 6个节点的图
    graph = [
        [0, 4, 1, 0, 0, 0],
        [4, 0, 2, 1, 3, 0],
        [1, 2, 0, 5, 0, 0],
        [0, 1, 5, 0, 2, 4],
        [0, 3, 0, 2, 0, 3],
        [0, 0, 0, 4, 3, 0],
    ]
    return graph


if __name__ == "__main__":
    # 测试邻接矩阵实现
    matrix_graph = create_sample_matrix()
    print("邻接矩阵图:")
    for row in matrix_graph:
        print(row)

    distances_matrix = dijkstra_adjacency_matrix(matrix_graph, 0)
    print(f"从节点0到所有节点的最短距离 (矩阵实现): {distances_matrix}")

    # 测试邻接列表实现
    list_graph = create_sample_graph()
    print("\n邻接列表图:")
    for node, edges in list_graph.items():
        print(f"{node}: {edges}")

    distances_list = dijkstra_adjacency_list(list_graph, 0)
    print(f"从节点0到所有节点的最短距离 (列表实现): {distances_list}")

    # 测试路径查找
    distance, path = dijkstra_with_path(list_graph, 0, 5)
    print(f"\n从节点0到节点5的最短距离: {distance}")
    print(f"最短路径: {path}")

    # 计算所有节点间的距离
    print("\n所有节点间的最短距离:")
    for start_node in range(6):
        distances = dijkstra_adjacency_list(list_graph, start_node)
        print(f"从节点{start_node}: {distances}")
