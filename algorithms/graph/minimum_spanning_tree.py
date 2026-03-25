"""
最小生成树算法 (Minimum Spanning Tree)
"""

import heapq


def prim(graph):
    """
    Prim算法 - 求解最小生成树

    参数:
        graph (dict): 邻接列表表示的图 {节点: [(邻居, 权重)]}

    返回:
        tuple: (最小生成树的总权重, MST边列表)
    """
    if not graph:
        return 0, []

    visited = set()
    mst_edges = []
    total_weight = 0

    # 从任意节点开始
    start_node = list(graph.keys())[0]
    visited.add(start_node)

    # 优先队列存储边
    edges_heap = []

    # 初始化优先队列
    for neighbor, weight in graph[start_node]:
        heapq.heappush(edges_heap, (weight, start_node, neighbor))

    while edges_heap and len(visited) < len(graph):
        weight, node_from, node_to = heapq.heappop(edges_heap)

        if node_to in visited:
            continue

        visited.add(node_to)
        mst_edges.append((node_from, node_to, weight))
        total_weight += weight

        for neighbor, weight in graph[node_to]:
            if neighbor not in visited:
                heapq.heappush(edges_heap, (weight, node_to, neighbor))

    return total_weight, mst_edges


def kruskal(graph):
    """
    Kruskal算法 - 求解最小生成树

    参数:
        graph (dict): 邻接列表表示的图 {节点: [(邻居, 权重)]}

    返回:
        tuple: (最小生成树的总权重, MST边列表)
    """
    if not graph:
        return 0, []

    # 收集所有边
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))

    # 按权重排序
    edges.sort()

    # 初始化并查集
    parent = {}
    for node in graph:
        parent[node] = node

    def find(x):
        """查找并查集根节点"""
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        """合并两个集合"""
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return total_weight, mst_edges


def dijkstra_mst(graph, start):
    """
    使用Dijkstra算法思想构建最小生成树

    参数:
        graph (dict): 邻接列表表示的图
        start (int): 起始节点

    返回:
        tuple: (最小生成树的总权重, MST边列表)
    """
    if not graph:
        return 0, []

    visited = set()
    mst_edges = []
    total_weight = 0

    distances = {}
    for node in graph:
        distances[node] = float("inf")
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        dist, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph[current]:
            if neighbor not in visited and distances[neighbor] > weight:
                distances[neighbor] = weight
                heapq.heappush(heap, (weight, neighbor))
                mst_edges.append((current, neighbor, weight))
                total_weight += weight

    return total_weight, mst_edges


def create_sample_graph():
    """
    创建示例图

    返回:
        dict: 邻接列表表示的图
    """
    graph = {
        0: [(1, 4), (2, 1), (3, 3)],
        1: [(0, 4), (2, 2), (4, 5)],
        2: [(0, 1), (1, 2), (3, 2), (4, 3)],
        3: [(0, 3), (2, 2), (4, 4)],
        4: [(1, 5), (2, 3), (3, 4)],
    }
    return graph


def create_weighted_graph():
    """
    创建带权重的示例图

    返回:
        dict: 邻接列表表示的图
    """
    graph = {
        "A": [("B", 7), ("D", 5)],
        "B": [("A", 7), ("C", 8), ("D", 9), ("E", 7)],
        "C": [("B", 8), ("E", 5)],
        "D": [("A", 5), ("B", 9), ("E", 15), ("F", 6)],
        "E": [("B", 7), ("C", 5), ("D", 15), ("F", 8), ("G", 9)],
        "F": [("D", 6), ("E", 8), ("G", 11)],
        "G": [("E", 9), ("F", 11)],
    }
    return graph


def benchmark_mst_algorithms():
    """
    对比不同MST算法的性能
    """
    import time

    graph = create_weighted_graph()

    print("最小生成树算法性能对比:")

    start = time.time()
    prim_weight, prim_edges = prim(graph)
    prim_time = time.time() - start

    start = time.time()
    kruskal_weight, kruskal_edges = kruskal(graph)
    kruskal_time = time.time() - start

    start = time.time()
    dijkstra_weight, dijkstra_edges = dijkstra_mst(graph, "A")
    dijkstra_time = time.time() - start

    print(f"Prim算法:")
    print(f"  总权重: {prim_weight}")
    print(f"  边数量: {len(prim_edges)}")
    print(f"  耗时: {prim_time:.6f}s")

    print(f"Kruskal算法:")
    print(f"  总权重: {kruskal_weight}")
    print(f"  边数量: {len(kruskal_edges)}")
    print(f"  耗时: {kruskal_time:.6f}s")

    print(f"Dijkstra MST算法:")
    print(f"  总权重: {dijkstra_weight}")
    print(f"  边数量: {len(dijkstra_edges)}")
    print(f"  耗时: {dijkstra_time:.6f}s")

    # 验证所有方法结果一致
    if prim_weight == kruskal_weight == dijkstra_weight:
        print(f"✓ 所有算法总权重一致: {prim_weight}")
    else:
        print(f"✗ 算法总权重不一致")


def visualize_mst(graph, mst_edges):
    """
    可视化最小生成树

    参数:
        graph (dict): 原始图
        mst_edges (list): MST边列表

    返回:
        str: 可视化结果
    """
    mst_graph = {}
    for node in graph:
        mst_graph[node] = []

    for u, v, weight in mst_edges:
        mst_graph[u].append((v, weight))
        mst_graph[v].append((u, weight))

    result = "最小生成树结构:\n"
    for node, edges in mst_graph.items():
        neighbor_list = [(neighbor, weight) for neighbor, weight in edges]
        result += f"节点 {node}: {neighbor_list}\n"

    return result


if __name__ == "__main__":
    # 创建示例图
    graph = create_sample_graph()

    print("示例图结构:")
    for node, edges in graph.items():
        print(f"节点 {node}: {edges}")

    # 测试Prim算法
    prim_weight, prim_edges = prim(graph)
    print(f"\nPrim算法:")
    print(f"最小生成树总权重: {prim_weight}")
    print(f"最小生成树边列表: {prim_edges}")

    # 测试Kruskal算法
    kruskal_weight, kruskal_edges = kruskal(graph)
    print(f"\nKruskal算法:")
    print(f"最小生成树总权重: {kruskal_weight}")
    print(f"最小生成树边列表: {kruskal_edges}")

    # 测试Dijkstra MST算法
    dijkstra_weight, dijkstra_edges = dijkstra_mst(graph, 0)
    print(f"\nDijkstra MST算法:")
    print(f"最小生成树总权重: {dijkstra_weight}")
    print(f"最小生成树边列表: {dijkstra_edges}")

    # 验证结果一致性
    if prim_weight == kruskal_weight and dijkstra_weight == prim_weight:
        print("\n✓ 三种算法得到相同的最小生成树总权重")
    else:
        print("\n✗ 三种算法得到不同的结果")

    # 可视化
    print("\nPrim算法构建的最小生成树:")
    print(visualize_mst(graph, prim_edges))

    # 复杂图的性能测试
    weighted_graph = create_weighted_graph()
    print("\n复杂图的最小生成树:")
    prim_weight_weighted, prim_edges_weighted = prim(weighted_graph)
    print(f"总权重: {prim_weight_weighted}")

    # 性能对比
    benchmark_mst_algorithms()
