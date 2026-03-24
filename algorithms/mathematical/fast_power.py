"""
快速幂算法
时间复杂度: O(log n)
"""

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


def fast_power_binary(x, n, mod=None):
    """
    快速幂算法 - 二进制分解版本
    
    参数:
        x (int): 底数
        n (int): 指数
        mod (int): 模数，可选
    
    返回:
        int: x^n或x^n mod mod
    """
    result = 1
    
    if mod is None:
        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
    else:
        while n > 0:
            if n & 1:
                result = (result * x) % mod
            x = (x * x) % mod
            n >>= 1
    
    return result


def fast_power_modular_inverse(x, mod):
    """
    快速幂计算模逆元
    
    参数:
        x (int): 整数
        mod (int): 模数
    
    返回:
        int: x mod mod的逆元，如果不存在则返回None
    
    使用费马小定理: x^(-1) = x^(mod-2) mod mod
    """
    if mod <= 1:
        return None
    
    # 检查gcd(x, mod)是否为1
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    if gcd(x, mod) != 1:
        return None
    
    return fast_power(x, mod - 2, mod)


def fast_power_performance_test():
    """
    测试快速幂算法的性能
    
    返回:
        str: 性能测试结果
    """
    import time
    
    tests = [
        {"x": 2, "n": 1000000, "mod": 1000000007},
        {"x": 3, "n": 1000000, "mod": None},
        {"x": 5, "n": 100000, "mod": 1000000007},
        {"x": 7, "n": 500000, "mod": None}
    ]
    
    results = []
    
    for test in tests:
        x = test["x"]
        n = test["n"]
        mod = test["mod"]
        
        # 朴素算法
        start_time = time.time()
        if mod:
            naive_result = pow(x, n) % mod
        else:
            naive_result = pow(x, n)
        naive_time = time.time() - start_time
        
        # 快速幂算法
        start_time = time.time()
        fast_result = fast_power(x, n, mod)
        fast_time = time.time() - start_time
        
        # 递归快速幂算法
        start_time = time.time()
        recursive_result = fast_power_recursive(x, n, mod)
        recursive_time = time.time() - start_time
        
        # 二进制分解版本
        start_time = time.time()
        binary_result = fast_power_binary(x, n, mod)
        binary_time = time.time() - start_time
        
        results.append({
            "x": x,
            "n": n,
            "mod": mod,
            "naive_time": naive_time,
            "fast_time": fast_time,
            "recursive_time": recursive_time,
            "binary_time": binary_time
        })
    
    result_str = "快速幂算法性能测试:\n"
    for r in results:
        result_str += f"""
底数: {r['x']}, 指数: {r['n']}, 模数: {r['mod']}
朴素算法耗时: {r['naive_time']:.6f}s
快速幂算法耗时: {r['fast_time']:.6f}s
递归快速幂算法耗时: {r['recursive_time']:.6f}s
二进制分解版本耗时: {r['binary_time']:.6f}s
"""
    
    return result_str


def fast_power_comparison():
    """
    比较不同指数的性能
    
    返回:
        str: 比较结果
    """
    import time
    
    x = 2
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    
    results = []
    for n in n_values:
        # 快速幂算法
        start_time = time.time()
        fast_result = fast_power(x, n)
        fast_time = time.time() - start_time
        
        # Python内置pow函数
        start_time = time.time()
        builtin_result = pow(x, n)
        builtin_time = time.time() - start_time
        
        results.append({
            "n": n,
            "fast_time": fast_time,
            "builtin_time": builtin_time
        })
    
    result_str = "快速幂算法与内置pow函数性能对比:\n"
    for r in results:
        result_str += f"""
指数: {r['n']}
快速幂算法耗时: {r['fast_time']:.6f}s
Python内置pow函数耗时: {r['builtin_time']:.6f}s
"""
    
    return result_str


def modular_power_tests():
    """
    模幂运算测试
    
    返回:
        str: 测试结果
    """
    tests = [
        {"x": 2, "n": 100, "mod": 7},
        {"x": 3, "n": 1000, "mod": 11},
        {"x": 5, "n": 10000, "mod": 13},
        {"x": 7, "n": 100000, "mod": 17}
    ]
    
    result_str = "模幂运算测试:\n"
    for test in tests:
        x = test["x"]
        n = test["n"]
        mod = test["mod"]
        
        result = fast_power(x, n, mod)
        expected = pow(x, n) % mod
        
        result_str += f"""
底数: {x}, 指数: {n}, 模数: {mod}
快速幂结果: {result}
标准计算结果: {expected}
一致性检查: {result == expected}
"""
    
    return result_str


if __name__ == "__main__":
    # 基本测试
    print("快速幂算法测试:")
    
    # 测试无模数的情况
    print("\n无模数测试:")
    test1 = fast_power(2, 10)
    test2 = fast_power(3, 5)
    test3 = fast_power(5, 3)
    
    print(f"2^10 = {test1} (期望值: 1024)")
    print(f"3^5 = {test2} (期望值: 243)")
    print(f"5^3 = {test3} (期望值: 125)")
    
    # 测试有模数的情况
    print("\n模运算测试:")
    mod_test1 = fast_power(2, 10, 7)
    mod_test2 = fast_power(3, 5, 11)
    mod_test3 = fast_power(5, 3, 13)
    
    print(f"2^10 mod 7 = {mod_test1} (期望值: 1024 mod 7 = 4)")
    print(f"3^5 mod 11 = {mod_test2} (期望值: 243 mod 11 = 1)")
    print(f"5^3 mod 13 = {mod_test3} (期望值: 125 mod 13 = 8)")
    
    # 递归版本测试
    print("\n递归版本测试:")
    rec_test1 = fast_power_recursive(2, 10)
    rec_test2 = fast_power_recursive(3, 5, 11)
    
    print(f"递归: 2^10 = {rec_test1}")
    print(f"递归: 3^5 mod 11 = {rec_test2}")
    
    # 二进制分解版本测试
    print("\n二进制分解版本测试:")
    binary_test1 = fast_power_binary(2, 10)
    binary_test2 = fast_power_binary(3, 5, 11)
    
    print(f"二进制分解: 2^10 = {binary_test1}")
    print(f"二进制分解: 3^5 mod 11 = {binary_test2}")
    
    # 模逆元测试
    print("\n模逆元测试:")
    mod = 7
    for x in range(1, mod):
        inverse = fast_power_modular_inverse(x, mod)
        print(f"{x} mod {mod} 的逆元: {inverse}")
    
    # 性能测试
    print("\n性能测试:")
    print(fast_power_performance_test())
    
    # 与Python内置pow函数的对比
    print("\n与内置pow函数对比:")
    print(fast_power_comparison())
    
    # 模幂运算测试
    print("\n模幂运算测试:")
    print(modular_power_tests())
    
    # 错误检查
    print("\n错误检查:")
    try:
        invalid_inverse = fast_power_modular_inverse(7, 7)
        print(f"7 mod 7 的逆元: {invalid_inverse} (应该为None)")
    except Exception as e:
        print(f"错误: {e}")