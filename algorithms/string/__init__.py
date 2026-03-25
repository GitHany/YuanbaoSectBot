"""
字符串算法模块
包括KMP和Boyer-Moore字符串匹配算法
"""

from .kmp import kmp_preprocess, kmp_search, kmp_longest_prefix_suffix

from .boyer_moore import boyer_moore_search
