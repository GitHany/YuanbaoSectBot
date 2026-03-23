"""
动态规划 - 背包问题
包括0/1背包问题和完全背包问题的解决方案
"""

def knapsack_01(weights, values, capacity):
    """
    0/1背包问题 - 每个物品只能选择一次
    
    参数:
        weights (list): 物品的重量列表
        values (list): 物品的价值列表
        capacity (int): 背包容量
    
    返回:
        int: 最大价值
    """
    n = len(weights)
    
    # 创建DP表格
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # 填充DP表格
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # 可以选择物品或不选择
                dp[i][w] = max(
                    dp[i - 1][w],  # 不选择物品
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # 选择物品
                )
            else:
                # 物品太重，不能选择
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def knapsack_01_optimized(weights, values, capacity):
    """
    0/1背包问题 - 优化空间版本
    
    参数:
        weights (list): 物品的重量列表
        values (list): 物品的价值列表
        capacity (int): 背包容量
    
    返回:
        int: 最大价值
    
    空间复杂度: O(capacity)
    """
    n = len(weights)
    
    # 使用一维数组优化空间
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # 从容量大到小更新（避免重复选择物品）
        for w in range(capacity, weights[i] - 1, -1):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def knapsack_unbounded(weights, values, capacity):
    """
    完全背包问题 - 每个物品可以选择多次
    
    参数:
        weights (list): 物品的重量列表
        values (list): 物品的价值列表
        capacity (int): 背包容量
    
    返回:
        int: 最大价值
    """
    n = len(weights)
    
    dp = [0] * (capacity + 1)
    
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def knapsack_multi(weights, values, counts, capacity):
    """
    多重背包问题 - 每个物品有指定的数量限制
    
    参数:
        weights (list): 物品的重量列表
        values (list): 物品的价值列表
        counts (list): 物品的数量限制列表
        capacity (int): 背包容量
    
    返回:
        int: 最大价值
    """
    n = len(weights)
    
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # 将多重背包转换为0/1背包
        k = 1
        while k <= counts[i]:
            weight = weights[i] * k
            value = values[i] * k
            
            if weight > capacity:
                break
            
            for w in range(capacity, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + value)
            
            k *= 2
    
    return dp[capacity]


def knapsack_with_items(weights, values, capacity):
    """
    0/1背包问题 - 返回选择的物品列表
    
    参数:
        weights (list): 物品的重量列表
        values (list): 物品的价值列表
        capacity (int): 背包容量
    
    返回:
        tuple: (最大价值, 选择的物品索引列表)
    """
    n = len(weights)
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # 记录选择
    keep = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                with_item = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                without_item = dp[i - 1][w]
                
                if with_item > without_item:
                    dp[i][w] = with_item
                    keep[i][w] = 1
                else:
                    dp[i][w] = without_item
            else:
                dp[i][w] = dp[i - 1][w]
    
    # 回溯找出选择的物品
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if keep[i][w] == 1:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    return dp[n][capacity], selected_items


def knapsack_problem_examples():
    """
    背包问题示例
    """
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    print("背包问题示例:")
    print(f"物品重量: {weights}")
    print(f"物品价值: {values}")
    print(f"背包容量: {capacity}")
    
    max_value = knapsack_01(weights, values, capacity)
    print(f"0/1背包最大价值: {max_value}")
    
    optimized_value = knapsack_01_optimized(weights, values, capacity)
    print(f"优化版0/1背包最大价值: {optimized_value}")
    
    unbounded_value = knapsack_unbounded(weights, values, capacity)
    print(f"完全背包最大价值: {unbounded_value}")
    
    # 多重背包示例
    counts = [2, 1, 3, 2]
    multi_value = knapsack_multi(weights, values, counts, capacity)
    print(f"多重背包最大价值: {multi_value}")
    
    # 获取选择的物品
    max_value_with_items, selected = knapsack_with_items(weights, values, capacity)
    print(f"0/1背包最大价值: {max_value_with_items}")
    print(f"选择的物品索引: {selected}")
    print(f"选择的物品重量: {[weights[i] for i in selected]}")
    print(f"选择的物品价值: {[values[i] for i in selected]}")
    
    # 验证所有方法结果一致
    if max_value == optimized_value:
        print("✓ 标准DP和优化DP结果一致")


if __name__ == "__main__":
    # 运行示例
    knapsack_problem_examples()
    
    # 测试不同容量
    capacities = [5, 8, 10]
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    
    print("\n不同容量的背包问题:")
    for capacity in capacities:
        max_value = knapsack_01_optimized(weights, values, capacity)
        print(f"容量 {capacity}: 最大价值 {max_value}")