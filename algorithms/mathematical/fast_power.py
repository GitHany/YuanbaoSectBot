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
        half_power = fast_power_recursive(x, n // 2, mod)
        if mod is None:
            return half_power * half_power
        else:
            return (half_power * half_power) % mod
    else:
        half_power = fast_power_recursive(x, n // 2, mod)
        if mod is None:
            return half_power * half_power * x
        else:
            return (half_power * half_power * x) % mod
