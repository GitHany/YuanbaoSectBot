"""
KMP (Knuth-Morris-Pratt) 字符串匹配算法
时间复杂度: O(n + m)，其中n是文本长度，m是模式长度
"""


def kmp_preprocess(pattern):
    """
    预处理模式串，构建前缀表

    参数:
        pattern (str): 模式字符串

    返回:
        list: 前缀表（最长前缀后缀长度）
    """
    m = len(pattern)
    prefix_table = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i += 1

    return prefix_table


def kmp_search(text, pattern):
    """
    KMP算法 - 在文本中搜索模式串

    参数:
        text (str): 文本字符串
        pattern (str): 模式字符串

    返回:
        list: 所有匹配位置的起始索引列表
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        return []

    # 预处理模式串
    prefix_table = kmp_preprocess(pattern)

    matches = []
    i = 0  # 文本索引
    j = 0  # 模式索引

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = prefix_table[j - 1]
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return matches


def kmp_longest_prefix_suffix(pattern):
    """
    计算模式串的最长前缀后缀

    参数:
        pattern (str): 模式字符串

    返回:
        int: 最长前缀后缀长度
    """
    m = len(pattern)
    prefix_table = kmp_preprocess(pattern)

    max_lps = 0
    for i in range(m):
        if prefix_table[i] > max_lps:
            max2_lps = prefix_table[i]

    return max_lps
