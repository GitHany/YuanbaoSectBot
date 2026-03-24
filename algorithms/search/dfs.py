"""
深度优先搜索算法 (DFS)
"""

def dfs_recursive(graph, start):
    """
    递归深度优先搜索
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
    
    返回:
        list: DFS遍历顺序
    """
    visited = set()
    result = []
    
    def dfs_helper(node):
        visited.add(node)
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    dfs_helper(start)
    return result


def dfs_iterative(graph, start):
    """
    迭代深度优先搜索
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
    
    返回:
        list: DFS遍历顺序
    """
    visited = set()
    stack = []
    result = []
    
    # 检查起始节点是否在图中
    if start not in graph:
        return result
    
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # 将邻居节点加入栈
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def dfs_with_path(graph, start, end):
    """
    DFS查找路径
    
    参数:
        graph (dict): 邻接表表示的图
        start (int): 起始节点
        end (int): 目标节点
    
    返回:
        list or None: 从start到end的路径，如果不存在则返回None
    """
    visited = set()
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        
        if node == end:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    
    return None


def dfs_cycle_detection(graph):
    """
    使用DFS检测图中是否存在环
    
    参数:
        graph (dict): 邻接表表示的图
    
    返回:
        bool: True如果存在环
    """
    visited = set()
    rec_stack = set()
    
    def has_cycle(node):
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if has_cycle(node):
                return True
    
    return False


def dfs_topological_sort(graph):
    """
    使用DFS进行拓扑排序
    
    参数:
        graph (dict): 邻接表表示的图
    
    返回:
        list: 拓扑排序结果
    
    注意: 要求图为有向无环图 (DAG)
    """
    visited = set()
    stack = []
    
    def topological_helper(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                topological_helper(neighbor)
        
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            topological_helper(node)
    
    return stack[::-1]


def dfs_connected_components(graph):
    """
    使用DFS查找连通分量
    
    参数:
        graph (dict): 邻接表表示的图
    
    返回:
        list: 连通分量列表
    """
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            # 对当前节点进行DFS
            component = []
            stack = [node]
            
            while stack:
                current = stack.pop()
                
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            
            components.append(component)
    
    return components


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


def dfs_benchmark():
    """
    对比递归和迭代DFS的性能
    """
    import time
    
    graph = create_sample_graph()
    start_node = 0
    
    print("DFS性能对比:")
    
    start = time.time()
    recursive_result = dfs_recursive(graph, start_node)
    recursive_time = time.time() - start
    
    start = time.time()
    iterative_result = dfs_iterative(graph, start_node)
    iterative_time = time.time() - start
    
    print(f"递归DFS结果: {recursive_result}")
    print(f"递归DFS耗时: {recursive_time:.6f}s")
    
    print(f"迭代DFS结果: {iterative_result}")
    print(f"迭代DFS耗时: {iterative_time:.6f}s")
    
    # 验证结果一致
    if recursive_result == iterative_result:
        print("✓ 递归和迭代DFS结果一致")
    else:
        print("✗ 递归和迭代DFS结果不一致")


if __name__ == "__main__":
    # 创建示例图
    graph = create_sample_graph()
    
    print("示例图结构:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    
    # 测试DFS遍历
    print("\nDFS遍历结果:")
    recursive_result = dfs_recursive(graph, 0)
    print(f"递归DFS: {recursive_result}")
    
    iterative_result = dfs_iterative(graph, 0)
    print(f"迭代DFS: {iterative_result}")
    
    # 测试DFS查找路径
    path = dfs_with_path(graph, 0, 5)
    print(f"\n从节点0到节点5的路径: {path}")
    
    # 测试环检测
    has_cycle = dfs_cycle_detection(graph)
    print(f"图中有环吗? {has_cycle}")
    
    # 测试连通分量
    components = dfs_connected_components(graph)
    print(f"连通分量: {components}")
    
    # 测试拓扑排序
    # 创建一个没有环的图
    dag_graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: [],
        5: [6],
        6: []
    }
    
    topological_order = dfs_topological_sort(dag_graph)
    print(f"拓扑排序结果: {topological_order}")
    
    # 性能对比
    dfs_benchmark()