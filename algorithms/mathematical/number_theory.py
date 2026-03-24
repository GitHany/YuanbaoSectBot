"""
数论算法模块
包括欧几里得算法、素数筛算法
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


def fast_power(x, n, mod=None):
    """
    快速幂算法 - 计算x^n
    
    参数:
        x (int): 底数
        n (int): 指数
        mod (int): 模数，可选
    
    返回:
        int: x^n或x^n mod mod
    
    时间复杂度: O(log n)
    """
    result = 1
    base = x
    
    if mod is None:
        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2
    else:
        while n > 0:
            if n % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            n //= 2
    
    return result


def fast_power_recursive(x, n, mod=None):
    """
    快速幂算法 - 递归版本
    
    参数:
        x (int): 底数
        n (int): 指数
        mod (int): 模数，可选
    
    返回:
        int: x^n或x^n mod mod
    """
    if n == 0:
        return 1
    if n == 1:
        return x if mod is None else x % mod
    
    if n % 2 == 0:
        half_power = fast_power_recursive(x, n//2, mod)
        if mod is None:
            return half_power * half_power
        else:
            return (half_power * half_power) % mod
    else:
        half_power = fast_power_recursive(x, n//2, mod)
        if mod is None:
            return half_power * half_power * x
        else:
            return (half_power * half_power * x) % mod


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


def sieve_of_eratosthenes_bitwise(n):
    """
    位运算埃拉托斯特尼筛法 - 内存优化版
    
    参数:
        n (int): 上限
    
    返回:
        list: 素数列表
    """
    if n < 2:
        return []
    
    primes = []
    
    # 使用字节数组
    is_prime = bytearray((n + 1) // 2)
    
    for i in range(3, n + 1, 2):
        index = i // 2
        if not is_prime[index]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                if j % 2 == 1:
                    is_prime[j // 2] = 1
    
    if n >= 2:
        primes.append(2)
    
    return primes


def segmented_sieve(n):
    """
    分段筛法 - 适用于大范围的素数筛选
    
    参数:
        n (int): 上限
    
    返回:
        list: 素数列表
    """
    if n < 2:
        return []
    
    segment_size = 1000000  # 每段大小为1M
    primes = []
    
    if n >= 2:
        primes.append(2)
    
    is_prime = bytearray((segment_size // 2))
    
    for segment_start in range(3, n + 1, segment_size):
        segment_end = min(segment_start + segment_size, n)
        
        # 初始化当前分段
        for i in range(len(is_prime)):
            is_prime[i] = 0
        
        # 筛选当前分段
        for p in primes:
            if p * p > segment_end:
                break
            
            start = segment_start
            if start % p != 0:
                start = segment_start + p - (segment_start % p)
            
            for j in range(start, segment_end + 1, p):
                if j % 2 == 1:
                    is_prime[(j - segment_start) // 2] = 1
        
        # 收集当前分段的素数
        for i in range(segment_start, segment_end + 1):
            if i % 2 == 1 and not is_prime[(i - segment_start) // 2]:
                primes.append(i)
    
    return primes


def prime_count_approximation(n):
    """
    使用素数定理估计小于等于n的素数数量
    
    参数:
        n (int): 上限
    
    返回:
        int: 估计的素数数量
    """
    if n < 2:
        return 0
    
    # π(n) ≈ n / ln(n)
    import math
    return int(n / math.log(n))


def prime_generator(n):
    """
    素数生成器 - 生成小于等于n的所有素数
    
    参数:
        n (int): 上限
    
    返回:
        generator: 素数生成器
    """
    primes = sieve_of_eratosthenes(n)
    for prime in primes:
        yield prime


def verify_prime(n):
    """
    验证一个数是否为素数
    
    参数:
        n (int): 待验证的数
    
    返回:
        bool: True如果是素数，False如果不是
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def calculate_lcm(a, b):
    """
    计算最小公倍数
    
    参数:
        a (int): 第一个整数
        b (int): 第二个整数
    
    返回:
        int: a和b的最小公倍数
    """
    gcd = gcd_euclidean(a, b)
    return a * b // gcd


def modular_inverse(a, mod):
    """
    计算模逆元
    
    参数:
        a (int): 整数
        mod (int): 模数
    
    返回:
        int: a mod mod的逆元，如果不存在则返回None
    """
    gcd, x, y = extended_gcd(a, mod)
    
    if gcd != 1:
        return None  # 没有逆元
    
    return (x % mod + mod) % mod


if __name__ == "__main__":
    import math
    
    # 欧几里得算法测试
    print("欧几里得算法测试:")
    pairs = [(48, 18), (101, 103), (1701, 3768), (123456789, 987654321)]
    for a, b in pairs:
        gcd = gcd_euclidean(a, b)
        lcm = calculate_lcm(a, b)
        print(f"gcd({a}, {b}) = {gcd}, lcm({a}, {b}) = {lcm}")
    
    # 扩展欧几里得算法测试
    print("\n扩展欧几里得算法测试:")
    for a, b in pairs[:2]:
        gcd, x, y = extended_gcd(a, b)
        print(f"gcd({a}, {b}) = {gcd}, {a}*{x} + {b}*{y} = {gcd}")
    
    # 快速幂算法测试
    print("\n快速幂算法测试:")
    tests = [(2, 10), (3, 15), (5, 20), (7, 8)]
    for x, n in tests:
        power = fast_power(x, n)
        power_mod = fast_power(x, n, 100)
        print(f"{x}^{n} = {power}")
        print(f"{x}^{n} mod 100 = {power_mod}")
    
    # 素数筛算法测试
    print("\n素数筛算法测试:")
    n_values = [10, 50, 100, 1000]
    for n in n_values:
        primes_standard = sieve_of_eratosthenes(n)
        primes_optimized = sieve_of_eratosthenes_optimized(n)
        primes_bitwise = sieve_of_eratosthenes_bitwise(n)
        
        print(f"\nn = {n}")
        print(f"标准筛法: 前{len(primes_standard)}个素数: {primes_standard[:10] if len(primes_standard) > 10 else primes_standard}")
        print(f"优化筛法: 前{len(primes_optimized)}个素数: {primes_optimized[:10] if len(primes_optimized) > 10 else primes_optimized}")
        print(f"位运算筛法: 前{len(primes_bitwise)}个素数: {primes_bitwise[:10] if len(primes_bitwise) > 10 else primes_bitwise}")
    
    # 大范围素数测试
    print("\n大范围素数测试:")
    large_n = 10000
    primes_large = sieve_of_eratosthenes(large_n)
    print(f"小于等于{large_n}的素数数量: {len(primes_large)}")
    print(f"最后一个素数: {primes_large[-1]}")
    
    # 分段筛法测试
    if large_n > 10000:
        primes_segmented = segmented_sieve(large_n)
        print(f"分段筛法素数数量: {len(primes_segmented)}")
        print(f"分段筛法最后一个素数: {primes_segmented[-1]}")
    
    # 验证素数
    print("\n素数验证:")
    numbers = [2, 3, 17, 100, 101, 997]
    for num in numbers:
        is_prime = verify_prime(num)
        print(f"{num} 是否为素数: {is_prime}")
    
    # 模逆元测试
    print("\n模逆元测试:")
    pairs_mod = [(3, 11), (5, 13), (7, 19), (4, 12)]
    for a, mod in pairs_mod:
        inverse = modular_inverse(a, mod)
        print(f"{a} mod {mod} 的逆元: {inverse}")
    
    # 性能比较
    print("\n算法性能比较:")
    import time
    
    x, n, mod = 2, 1000000, 1000000007
    
    start_time = time.time()
    result_naive = x ** n % mod
    naive_time = time.time() - start_time
    
    start_time = time.time()
    result_fast = fast_power(x, n, mod)
    fast_time = time.time() - start_time
    
    start_time = time.time()
    result_recursive = fast_power_recursive(x, n, mod)
    recursive_time = time.time() - start_time
    
    print(f"x={x}, n={n}, mod={mod}")
    print(f"朴素算法结果: {result_naive}, 耗时: {naive_time:.6f}s")
    print(f"快速幂算法结果: {result_fast}, 耗时: {fast_time:.6f}s")
    print(f"递归快速幂结果: {result_recursive}, 耗时: {recursive_time:.6f}s")