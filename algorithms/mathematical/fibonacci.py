"""
斐波那契数列算法
"""

def fibonacci_recursive(n):
    """
    递归计算斐波那契数列
    
    参数:
        n (int): 斐波那契数列的第n项
    
    返回:
        int: 斐波那契数列的第n项值
    
    注意: 递归方法时间复杂度为O(2^n)，不适合大的n
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    迭代计算斐波那契数列
    
    参数:
        n (int): 斐波那契数列的第n项
    
    返回:
        int: 斐波那契数列的第n项值
    
    时间复杂度: O(n)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def fibonacci_dynamic(n):
    """
    动态规划计算斐波那契数列
    
    参数:
        n (int): 斐波那契数列的第n项
    
    返回:
        int: 斐波那契数列的第n项值
    
    时间复杂度: O(n)
    """
    if n <= 0:
        return 0
    
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]


def fibonacci_memoization(n, memo=None):
    """
    使用记忆化计算的斐波那契数列
    
    参数:
        n (int): 斐波那契数列的第n项
        memo (dict): 记忆化字典
    
    返回:
        int: 斐波那契数列的第n项值
    
    时间复杂度: O(n)
    """
    if memo is None:
        memo = {}
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_matrix(n):
    """
    使用矩阵幂计算的斐波那契数列
    
    参数:
        n (int): 斐波那契数列的第n项
    
    返回:
        int: 斐波那契数列的第n项值
    
    时间复杂度: O(log n)
    """
    if n <= 0:
        return 0
    
    def matrix_multiply(A, B):
        """矩阵乘法"""
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]
    
    def matrix_power(matrix, power):
        """矩阵快速幂"""
        result = [[1, 0], [0, 1]]  # 单位矩阵
        
        while power > 0:
            if power % 2 == 1:
                result = matrix_multiply(result, matrix)
            matrix = matrix_multiply(matrix, matrix)
            power //= 2
        
        return result
    
    # 斐波那契数列的矩阵表示
    fib_matrix = [[1, 1], [1, 0]]
    
    # 计算矩阵的n-1次幂
    powered_matrix = matrix_power(fib_matrix, n - 1)
    
    return powered_matrix[0][0]


def fibonacci_sequence(n):
    """
    生成斐波那契数列的前n项
    
    参数:
        n (int): 要生成的数量
    
    返回:
        list: 斐波那契数列的前n项
    """
    sequence = []
    if n <= 0:
        return sequence
    
    if n == 1:
        sequence.append(0)
        return sequence
    
    sequence.append(0)
    sequence.append(1)
    
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


if __name__ == "__main__":
    # 测试各种斐波那契计算方法
    n = 10
    
    print(f"斐波那契数列的第 {n} 项:")
    print(f"递归方法: {fibonacci_recursive(n)}")
    print(f"迭代方法: {fibonacci_iterative(n)}")
    print(f"动态规划: {fibonacci_dynamic(n)}")
    print(f"记忆化: {fibonacci_memoization(n)}")
    print(f"矩阵幂: {fibonacci_matrix(n)}")
    
    # 生成斐波那契数列
    sequence = fibonacci_sequence(15)
    print(f"前15项斐波那契数列: {sequence}")
    
    # 性能对比（n较大时）
    print("\n性能测试 (n=30):")
    import time
    
    n_large = 30
    
    start = time.time()
    iterative_result = fibonacci_iterative(n_large)
    iterative_time = time.time() - start
    
    start = time.time()
    memo_result = fibonacci_memoization(n_large)
    memo_time = time.time() - start
    
    start = time.time()
    matrix_result = fibonacci_matrix(n_large)
    matrix_time = time.time() - start
    
    print(f"迭代方法: {iterative_result} (耗时: {iterative_time:.6f}s)")
    print(f"记忆化方法: {memo_result} (耗时: {memo_time:.6f}s)")
    print(f"矩阵幂方法: {matrix_result} (耗时: {matrix_time:.6f}s)")
    
    # 注意：递归方法对于n=30会非常慢，不建议测试