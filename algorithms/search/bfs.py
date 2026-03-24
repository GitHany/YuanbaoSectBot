"""
广度优先搜索算法 (BFS)
"""

def bfs(graph, start):
    """
    广度优先搜索
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
    
    返回:
        list: BFS遍历顺序
    """
    visited = set()
    result = []
    
    # 检查起始节点是否在图中
    if start not in graph:
        return result
    
    visited.add(start)
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_with_path(graph, start, end):
    """
    BFS查找最短路径
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
        end (int): 目标节点
    
    返回:
        list or None: 从start到end的最短路径，如果不存在则返回None
    """
    visited = set()
    queue = [(start, [start])]
    visited.add(start)
    
    while queue:
        node, path = queue.pop(0)
        
        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None


def bfs_levels(graph, start):
    """
    BFS按层级遍历
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
    
    返回:
        dict: 每个节点的层级
    """
    visited = set()
    queue = [(start, 0)]
    visited.add(start)
    levels = {start: 0}
    
    while queue:
        node, level = queue.pop(0)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                levels[neighbor] = level + 1
                queue.append((neighbor, level + 1))
    
    return levels


def bfs_connected_components(graph):
    """
    使用BFS查找连通分量
    
    参数:
        graph (dict): 邻接表表示的图
    
    返回:
        list: 连通分量列表
    """
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            # 对当前节点进行BFS
            component = []
            queue = [node]
            visited.add(node)
            
            while queue:
                current = queue.pop(0)
                component.append(current)
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            components.append(component)
    
    return components


def bfs_bidirectional(graph, start, end):
    """
    双向BFS
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
        end (int): 目标节点
    
    返回:
        list or None: 从start到end的最短路径，如果不存在则返回None
    """
    if start == end:
        return [start]
    
    visited_start = {start: 0}
    visited_end = {end: 0}
    queue_start = [start]
    queue_end = [end]
    
    while queue_start and queue_end:
        # 扩展start侧
        node_start = queue_start.pop(0)
        for neighbor in graph[node_start]:
            if neighbor in visited_end:
                # 找到交汇点
                return visited_start[node_start] + visited_end[neighbor] + 1
            
            if neighbor not in visited_start:
                visited_start[neighbor] = visited_start[node_start] + 1
                queue_start.append(neighbor)
        
        # 扩展end侧
        node_end = queue_end.pop(0)
        for neighbor in graph[node_end]:
            if neighbor in visited_start:
                # 找到交汇点
                return visited_start[neighbor] + visited_end[node_end] + 1
            
            if neighbor not in visited_end:
                visited_end[neighbor] = visited_end[node_end] + 1
                queue_end.append(neighbor)
    
    return None


def bfs_distance(graph, start):
    """
    使用BFS计算距离
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
    
    返回:
        dict: 每个节点到起始节点的距离
    """
    visited = set()
    distances = {}
    queue = [(start, 0)]
    visited.add(start)
    distances[start] = 0
    
    while queue:
        node, distance = queue.pop(0)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distance + 1
                # 队列中的distance是0？
                queue.append((neighbor, distance + 1))
    
    return distances


def bfs_max_distance(graph, start):
    """
    使用BFS查找最大距离
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
    
    返回:
        tuple: (最大距离节点, 距离)
    """
    distances = bfs_distance(graph, start)
    
    if not distances:
        return None, 0
    
    max_distance = 0
    farthest_node = start
    
    for node, distance in distances.items():
        if distance > max_distance:
            max_distance = distance
            farthest_node = node
    
    return farthest_node, max_distance


def bfs_benchmark():
    """
    对比DFS和BFS的性能
    """
    import time
    
    from algorithms.search.dfs import dfs_iterative
    
    graph = create_sample_graph()
    start_node = 0
    
    print("DFS和BFS性能对比:")
    
    start = time.time()
    dfs_result = dfs_iterative(graph, start_node)
    dfs_time = time.time() - start
    
    start = time.time()
    bfs_result = bfs(graph, start_node)
    bfs_time = time.time() - start
    
    print(f"DFS遍历结果: {dfs_result}")
    print(f"DFS耗时: {dfs_time:.6f}s")
    
    print(f"BFS遍历结果: {bfs_result}")
    print(f"BFS耗时: {bfs_time:.6f}s")
    
    # 验证结果
    if len(dfs_result) == len(bfs_result):
        print(f"✓ 两种遍历都找到了 {len(dfs_result)} 个节点")


def create_sample_graph():
    """
    创建示例图
    
    返回:
        dict: 邻接表表示的图
    """
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1, 5],
        4: [2, 5],
        5: [3, 4],
        6: [7],
        7: [6]
    }
    return graph


if __name__ == "__main__":
    # 创建示例图
    graph = create_sample_graph()
    
    print("示例图结构:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    
    # 测试BFS遍历
    bfs_result = bfs(graph, 0)
    print(f"\nBFS遍历结果: {bfs_result}")
    
    # 测试BFS查找路径
    path = bfs_with_path(graph, 0, 5)
    print(f"从节点0到节点5的最短路径: {path}")
    
    # 测试按层级遍历
    levels = bfs_levels(graph, 0)
    print(f"层级信息:")
    for node, level in levels.items():
        print(f"节点{node}: 层级{level}")
    
    # 测试连通分量
    components = bfs_connected_components(graph)
    print(f"连通分量: {components}")
    
    # 测试距离计算
    distances = bfs_distance(graph, 0)
    print(f"距离信息:")
    for node, distance in distances.items():
        print(f"节点{node}到节点0的距离: {distance}")
    
    # 测试最大距离
    farthest_node, max_distance = bfs_max_distance(graph, 0)
    print(f"最远的节点: {farthest_node}, 距离: {max_distance}")
    
    # 性能对比
    bfs_benchmark()