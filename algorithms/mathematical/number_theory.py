"""
数论算法 - 简化版本
"""

def gcd_euclidean(a, b):
    """
    欧几里得算法 - 计算最大公约数
    
    参数:
        a (int): 第一个整数
        b (int): 第二个整数
    
    返回:
        int: a和b的最大公约数
    
    时间复杂度: O(log(min(a, b)))
    """
    while b != 0:
        a, b = b, a % b
    return a


def gcd_euclidean_recursive(a, b):
    """
    欧几里得算法 - 递归版本
    
    参数:
        a (int): 第一个整数
        b (int): 第二个整数
    
    返回:
        int: a和b的最大公约数
    """
    if b == 0:
        return a
    return gcd_euclidean_recursive(b, a % b)


def sieve_of_eratosthenes(n):
    """
    埃拉托斯特尼筛法 - 生成小于等于n的所有素数
    
    参数:
        n (int): 上限
    
    返回:
        list: 素数列表
    
    时间复杂度: O(n log log n)
    """
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    primes = []
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # 收集剩余的素数
    for i in range(int(n**0.5) + 1, n + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes