"""
Boyer-Moore字符串匹配算法 - 简化版本
"""


def boyer_moore_search(text, pattern):
    """
    Boyer-Moore算法 - 在文本中搜索模式串

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

    # 构建坏字符表
    bad_char_table = {}
    for i in range(m):
        bad_char_table[pattern[i]] = m - i - 1

    matches = []
    i = 0

    while i <= n - m:
        j = m - 1

        # 从右向左比较
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            matches.append(i)
            i += 1
        else:
            # 坏字符规则
            char = text[i + j]
            bad_char_offset = 1

            if char in bad_char_table:
                bad_char_offset = max(1, bad_char_table[char] - j)

            # 字符不在模式中，移动整个模式长度
            i += m

    return matches
