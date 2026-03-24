"""
Boyer-Moore字符串匹配算法
时间复杂度: 平均O(n/m)，最好情况O(n/m)，最坏情况O(nm)
"""

def boyer_moore_bad_character_table(pattern):
    """
    构建坏字符表
    
    参数:
        pattern (str): 模式字符串
    
    返回:
        dict: 坏字符表，字符 -> 偏移量
    """
    m = len(pattern)
    bad_char_table = {}
    
    for i in range(m):
        # 记录每个字符在模式串中最右边的位置
        bad_char_table[pattern[i]] = m - i - 1
    
    # 添加默认偏移（字符不在模式串中）
    return bad_char_table


def boyer_moore_good_suffix_table(pattern):
    """
    构建好后缀表
    
    参数:
        pattern (str): 模式字符串
    
    返回:
        list: 好后缀表
    """
    m = len(pattern)
    good_suffix_table = [m] * (m + 1)
    
    # 计算后缀表
    for i in range(m - 1):
        j = m - 1
        k = i
        
        while j >= 0 and pattern[j] == pattern[k]:
            j -= 1
            k -= 1
        
        if j < 0:
            # 完全匹配
            good_suffix_table[m - i - 1] = i + 1
    
    # 处理部分匹配
    for i in range(m):
        good_suffix_table[i] = max(1, m - i - 1)
    
    return good_suffix_table


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
    
    # 构建坏字符表和好后缀表
    bad_char_table = boyer_moore_bad_character_table(pattern)
    good_suffix_table = boyer_moore_good_suffix_table(pattern)
    
    matches = []
    i = 0  # 文本索引
    
    while i <= n - m:
        j = m - 1  # 模式索引
        
        # 从右向左比较
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        
        # 如果完全匹配
        if j < 0:
            matches.append(i)
            i += 1  # 移动1个位置以支持重叠匹配
        else:
            # 坏字符规则
            char = text[i + j]
            bad_char_offset = 1
            
            if char in bad_char_table:
                bad_char_offset = max(1, bad_char_table[char] - j)
            
            # 好后缀规则
            good_suffix_offset = good_suffix_table[j]
            
            # 选择较大的偏移
            i += max(bad_char_offset, good_suffix_offset)
    
    return matches