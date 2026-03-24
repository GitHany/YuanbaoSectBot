"""
数学算法模块
"""

from .primes import is_prime, sieve_of_eratosthenes, prime_factors, gcd, lcm
from .fibonacci import fibonacci_recursive, fibonacci_iterative, fibonacci_dynamic, fibonacci_memoization, fibonacci_matrix, fibonacci_sequence
from .number_theory import (
    gcd_euclidean,
    gcd_euclidean_recursive,
    extended_gcd,
    fast_power,
    fast_power_recursive,
    sieve_of_eratosthenes,
    sieve_of_eratosthenes_optimized,
    sieve_of_eratosthenes_bitwise,
    segmented_sieve,
    prime_count_approximation,
    prime_generator,
    verify_prime,
    calculate_lcm,
    modular_inverse
)