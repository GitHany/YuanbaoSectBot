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


def kmp_search_with_prefix_table(text, pattern, prefix_table):
    """
    KMP算法 - 使用预计算的前缀表
    
    参数:
        text (str): 文本字符串
        pattern (str): 模式字符串
        prefix_table (list): 预处理的前缀表
    
    返回:
        list: 所有匹配位置的起始索引列表
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []
    
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
            max_lps = prefix_table[i]
    
    return max_lps


def kmp_visualize(pattern, text):
    """
    可视化KMP匹配过程
    
    参数:
        pattern (str): 模式字符串
        text (str): 文本字符串
    
    返回:
        str: 可视化结果
    """
    prefix_table = kmp_preprocess(pattern)
    matches = kmp_search(text, pattern)
    
    result = f"""
KMP算法可视化:
模式串: {pattern}
前缀表: {prefix_table}
文本: {text}
匹配位置: {matches}
"""
    
    # 可视化匹配过程
    if matches:
        result += "\n匹配位置可视化:\n"
        for match_pos in matches:
            visual_text = text[:match_pos] + "[" + text[match_pos:match_pos+len(pattern)] + "]" + text[match_pos+len(pattern):]
            result += f"位置 {match_pos}: {visual_text}\n"
    
    return result


def kmp_performance_test():
    """
    测试KMP算法性能
    
    返回:
        str: 性能测试结果
    """
    import time
    
    # 测试不同长度的模式串
    test_text = "ababcababcababcababcababcababcababcababcababcababc"
    patterns = ["abc", "ababc", "ababcababc", "notfound"]
    
    results = []
    for pattern in patterns:
        start_time = time.time()
        matches = kmp_search(test_text, pattern)
        elapsed = time.time() - start_time
        
        results.append({
            "pattern": pattern,
            "pattern_length": len(pattern),
            "matches": len(matches),
            "positions": matches,
            "time": elapsed
        })
    
    result_str = "KMP算法性能测试:\n"
    for r in results:
        result_str += f"""
模式: {r['pattern']} (长度: {r['pattern_length']})
匹配数量: {r['matches']}
匹配位置: {r['positions']}
耗时: {r['time']:.6f}s
"""
    
    return result_str


if __name__ == "__main__":
    # 基础测试
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    print(f"文本: {text}")
    print(f"模式: {pattern}")
    
    prefix_table = kmp_preprocess(pattern)
    print(f"前缀表: {prefix_table}")
    
    matches = kmp_search(text, pattern)
    print(f"匹配位置: {matches}")
    
    # 可视化演示
    if matches:
        print(f"\n可视化匹配:")
        for match_pos in matches:
            print(f"位置 {match_pos}: {text[:match_pos]}[{text[match_pos:match_pos+len(pattern)]}]{text[match_pos+len(pattern):]}")
    
    # 测试最长前缀后缀
    test_patterns = ["ABCDABD", "AAAA", "ABABABA", "ABCABCABC"]
    print(f"\n最长前缀后缀测试:")
    for pattern in test_patterns:
        lps = kmp_longest_prefix_suffix(pattern)
        print(f"模式 {pattern}: {lps}")
    
    # 性能测试
    print("\n" + kmp_performance_test())
    
    # 复杂测试
    text2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet."
    pattern2 = "Lorem ipsum dolor"
    
    matches2 = kmp_search(text2, pattern2)
    print(f"\n复杂文本匹配:")
    print(f"文本长度: {len(text2)}")
    print(f"模式长度: {len(pattern2)}")
    print(f"匹配位置: {matches2}")
    
    # 可视化测试
    print("\n" + kmp_visualize(pattern, text))