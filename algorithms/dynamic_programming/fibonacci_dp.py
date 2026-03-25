"""
动态规划 - 斐波那契数列
时间复杂度: O(n)
空间复杂度: O(n)
"""


def fibonacci_dp(n):
    """
    动态规划计算斐波那契数列

    参数:
        n (int): 斐波那契数列的第n项

    返回:
        int: 斐波那契数列的第n项值
    """
    if n <= 0:
        return 0

    # 创建DP数组
    dp = [0] * (n + 1)
    dp[0] = 0

    if n >= 1:
        dp[1] = 1

    # 动态规划填充
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_dp_optimized(n):
    """
    优化空间版本的动态规划计算斐波那契数列

    参数:
        n (int): 斐波那契数列的第n项

    返回:
        int: 斐波那契数列的第n项值

    空间复杂度: O(1)
    """
    if n <= 0:
        return 0

    a, b = 0, 1

    for i in range(2, n + 1):
        c = a + b
        a, b = b, c

    return b if n > 0 else 0


def fibonacci_bottom_up(n):
    """
    自底向上动态规划

    参数:
        n (int): 斐波那契数列的第n项

    返回:
        int: 斐波那契数列的第n项值
    """
    if n <= 0:
        return 0

    # 初始化基础情况
    dp = [0, 1]

    # 逐步构建
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


def fibonacci_top_down(n):
    """
    自顶向下动态规划（带备忘录）

    参数:
        n (int): 斐波那契数列的第n项

    返回:
        int: 斐波那契数列的第n项值
    """
    memo = {}

    def fib_helper(x):
        if x <= 0:
            return 0
        if x == 1:
            return 1

        if x in memo:
            return memo[x]

        memo[x] = fib_helper(x - 1) + fib_helper(x - 2)
        return memo[x]

    return fib_helper(n)


def fibonacci_matrix_power(n):
    """
    使用矩阵幂计算的斐波那契数列（动态规划视角）

    参数:
        n (int): 斐波那契数列的第n项

    返回:
        int: 斐波那契数列的第n项值

    时间复杂度: O(log n)
    """
    if n <= 0:
        return 0

    def multiply_matrix(A, B):
        """矩阵乘法"""
        return [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ]

    def matrix_power(matrix, power):
        """矩阵快速幂"""
        result = [1, 0, 0, 1]  # 单位矩阵

        while power > 0:
            if power % 2 == 1:
                result = multiply_matrix(result, matrix)
            matrix = multiply_matrix(matrix, matrix)
            power //= 2

        return result

    # 斐波那契数列的矩阵表示
    fib_matrix = [1, 1, 1, 0]

    # 计算矩阵的n-1次幂
    powered_matrix = matrix_power(fib_matrix, n - 1)

    return powered_matrix[0]


def benchmark_dp_methods():
    """
    对比不同动态规划方法的性能
    """
    import time

    test_values = [10, 20, 30, 40]

    print("动态规划方法性能对比:")

    for n in test_values:
        print(f"\n计算 F({n}):")

        start = time.time()
        result1 = fibonacci_dp(n)
        time1 = time.time() - start

        start = time.time()
        result2 = fibonacci_dp_optimized(n)
        time2 = time.time() - start

        start = time.time()
        result3 = fibonacci_top_down(n)
        time3 = time.time() - start

        start = time.time()
        result4 = fibonacci_matrix_power(n)
        time4 = time.time() - start

        print(f"  标准DP: {result1} (耗时: {time1:.6f}s)")
        print(f"  优化DP: {result2} (耗时: {time2:.6f}s)")
        print(f"  自顶向下: {result3} (耗时: {time3:.6f}s)")
        print(f"  矩阵幂: {result4} (耗时: {time4:.6f}s)")

        # 验证所有方法结果一致
        if result1 == result2 == result3 == result4:
            print("  ✓ 所有方法结果一致")


if __name__ == "__main__":
    # 测试动态规划方法
    n = 10
    print(f"斐波那契数列第 {n} 项:")

    print(f"标准动态规划: {fibonacci_dp(n)}")
    print(f"优化空间DP: {fibonacci_dp_optimized(n)}")
    print(f"自底向上DP: {fibonacci_bottom_up(n)}")
    print(f"自顶向下DP: {fibonacci_top_down(n)}")
    print(f"矩阵幂DP: {fibonacci_matrix_power(n)}")

    # 性能对比
    benchmark_dp_methods()
