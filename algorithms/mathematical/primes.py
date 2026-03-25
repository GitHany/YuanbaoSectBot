"""
数学算法 - 质数相关算法
"""


def is_prime(n):
    """
    判断一个数是否为质数

    参数:
        n (int): 要判断的数

    返回:
        bool: True如果是质数
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 检查从3到sqrt(n)的奇数
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def sieve_of_eratosthenes(n):
    """
    埃拉托斯特尼筛法 - 生成小于等于n的所有质数

    参数:
        n (int): 上限

    返回:
        list: 小于等于n的所有质数
    """
    if n < 2:
        return []

    # 创建布尔数组，初始假设所有数都是质数
    is_prime_list = [True] * (n + 1)
    is_prime_list[0] = False
    is_prime_list[1] = False

    p = 2
    while p * p <= n:
        if is_prime_list[p]:
            # 标记p的倍数
            for i in range(p * p, n + 1, p):
                is_prime_list[i] = False
        p += 1

    # 收集所有质数
    primes = [i for i in range(2, n + 1) if is_prime_list[i]]
    return primes


def generate_primes(limit):
    """
    生成一定数量的质数

    参数:
        limit (int): 质数的数量

    返回:
        list: 质数列表
    """
    primes = []
    num = 2

    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes


def prime_factors(n):
    """
    获取一个数的质因数分解

    参数:
        n (int): 要分解的数

    返回:
        list: 质因数列表
    """
    factors = []

    # 处理2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 处理奇数因子
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # 处理剩余的部分
    if n > 2:
        factors.append(n)

    return factors


def gcd(a, b):
    """
    计算最大公约数 (GCD)

    参数:
        a (int): 第一个数
        b (int): 第二个数

    返回:
        int: 最大公约数
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    计算最小公倍数 (LCM)

    参数:
        a (int): 第一个数
        b (int): 第二个数

    返回:
        int: 最小公倍数
    """
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    # 测试质数判断
    print("质数判断:")
    numbers = [2, 3, 17, 20, 29, 100]
    for n in numbers:
        print(f"{n} 是否是质数: {is_prime(n)}")

    # 测试筛法
    n = 50
    primes = sieve_of_eratosthenes(n)
    print(f"小于等于 {n} 的所有质数: {primes}")

    # 测试生成指定数量的质数
    prime_list = generate_primes(10)
    print(f"前10个质数: {prime_list}")

    # 测试质因数分解
    print("质因数分解:")
    test_numbers = [12, 60, 100, 210]
    for num in test_numbers:
        factors = prime_factors(num)
        print(f"{num} 的质因数: {factors}")

    # 测试GCD和LCM
    print("GCD和LCM:")
    a, b = 12, 18
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
