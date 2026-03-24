"""
数论算法模块
包括欧几里得算法和素数筛算法
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


def extended_gcd(a, b):
    """
    扩展欧几里得算法 - 计算最大公约数并找到x,y使得ax+by=gcd(a,b)
    
    参数:
        a (int): 第一个整数
        b (int): 第二个整数
    
    返回:
        tuple: (gcd, x, y)
    """
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


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


def sieve_of_eratosthenes_optimized(n):
    """
    优化版埃拉托斯特尼筛法 - 只使用奇数
    
    参数:
        n (int): 上限
    
    返回:
        list: 素数列表
    """
    if n < 2:
        return []
    
    # 初始化数组，只考虑奇数
    limit = n // 2 + 1
    is_prime = [True] * limit
    primes = []
    
    if n >= 2:
        primes.append(2)
    
    for i in range(1, limit):
        if is_prime[i]:
            prime = 2 * i + 1
            primes.append(prime)
            step = prime
            for j in range(i + step, limit, step):
                is_prime[j] = False
    
    return primes