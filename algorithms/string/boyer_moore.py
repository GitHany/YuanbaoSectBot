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
    good_suffix_table = [0] * (m + 1)
    
    # 第一步：计算前缀表
    prefix_table = [0] * m
    length = 0
    
    for i in range(1, m):
        while length > 0 and pattern[i] != pattern[length]:
            length = prefix_table[length - 1]
        
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
    
    # 第二步：构建好后缀表
    suffix_positions = [0] * m
    
    for i in range(m):
        suffix_positions[i] = m - prefix_table[i]
    
    return suffix_positions


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
            # 使用好后缀表移动模式串
            i += good_suffix_table[0]
        else:
            # 坏字符规则
            bad_char_offset = m - j - 1
            
            # 好后缀规则
            good_suffix_offset = good_suffix_table[j]
            
            # 选择较大的偏移
            i += max(bad_char_offset, good_suffix_offset)
    
    return matches


def boyer_moore_simple_search(text, pattern):
    """
    Boyer-Moore算法的简化版本（只使用坏字符规则）
    
    参数:
        pattern (str): 模式字符串
        text (str): 文本字符串
    
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
            i += m  # 完全匹配时移动整个模式长度
        else:
            # 坏字符规则
            char = text[i + j]
            
            if char in bad_char_table:
                offset = bad_char_table[char]
                i += max(1, m - j - offset)
            else:
                # 字符不在模式中，移动整个模式长度
                i += m
    
    return matches


def boyer_moore_visualize(pattern, text):
    """
    可视化Boyer-Moore匹配过程
    
    参数:
        pattern (str): 模式字符串
        text (str): 文本字符串
    
    返回:
        str: 可视化结果
    """
    bad_char_table = boyer_moore_bad_character_table(pattern)
    good_suffix_table = boyer_moore_good_suffix_table(pattern)
    matches = boyer_moore_search(text, pattern)
    
    result = f"""
Boyer-Moore算法可视化:
模式串: {pattern}
坏字符表: {bad_char_table}
好后缀表: {good_suffix_table}
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


def boyer_moore_performance_test():
    """
    测试Boyer-Moore算法性能
    
    返回:
        str: 性能测试结果
    """
    import time
    
    # 测试不同长度的模式串
    test_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    patterns = ["ABC", "XYZ", "ABCDEFGHIJKLM", "OPQRSTUVWXYZ", "NOTFOUND"]
    
    results = []
    for pattern in patterns:
        start_time = time.time()
        matches = boyer_moore_search(test_text, pattern)
        elapsed = time.time() - start_time
        
        results.append({
            "pattern": pattern,
            "pattern_length": len(pattern),
            "matches": len(matches),
            "positions": matches,
            "time": elapsed
        })
    
    result_str = "Boyer-Moore算法性能测试:\n"
    for r in results:
        result_str += f"""
模式: {r['pattern']} (长度: {r['pattern_length']})
匹配数量: {r['matches']}
匹配位置: {r['positions']}
耗时: {r['time']:.6f}s
"""
    
    return result_str


def boyer_moore_vs_kmp_comparison():
    """
    比较Boyer-Moore和KMP算法的性能
    
    返回:
        str: 比较结果
    """
    import time
    
    # 从KMP模块导入函数
    from kmp import kmp_search
    
    test_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet."
    patterns = ["Lorem", "ipsum dolor", "Lorem ipsum dolor", "sit amet"]
    
    results = []
    for pattern in patterns:
        # Boyer-Moore测试
        start_time = time.time()
        boyer_moore_matches = boyer_moore_search(test_text, pattern)
        boyer_moore_time = time.time() - start_time
        
        # KMP测试
        start_time = time.time()
        kmp_matches = kmp_search(test_text, pattern)
        kmp_time = time.time() - start_time
        
        results.append({
            "pattern": pattern,
            "pattern_length": len(pattern),
            "boyer_moore_matches": len(boyer_moore_matches),
            "boyer_moore_time": boyer_moore_time,
            "kmp_matches": len(kmp_matches),
            "kmp_time": kmp_time
        })
    
    result_str = "Boyer-Moore vs KMP算法性能对比:\n"
    for r in results:
        result_str += f"""
模式: {r['pattern']} (长度: {r['pattern_length']})
Boyer-Moore匹配数量: {r['boyer_moore_matches']}, 耗时: {r['boyer_moore_time']:.6f}s
KMP匹配数量: {r['kmp_matches']}, 耗时: {r['kmp_time']:.6f}s
"""
    
    return result_str


if __name__ == "__main__":
    # 基础测试
    text = "Here is a simple example with example pattern"
    pattern = "example"
    
    print(f"文本: {text}")
    print(f"模式: {pattern}")
    
    # 坏字符表
    bad_char_table = boyer_moore_bad_character_table(pattern)
    print(f"坏字符表: {bad_char_table}")
    
    # 好后缀表
    good_suffix_table = boyer_moore_good_suffix_table(pattern)
    print(f"好后缀表: {good_suffix_table}")
    
    # 完整Boyer-Moore搜索
    matches_full = boyer_moore_search(text, pattern)
    print(f"完整Boyer-Moore匹配位置: {matches_full}")
    
    # 简化Boyer-Moore搜索
    matches_simple = boyer_moore_simple_search(text, pattern)
    print(f"简化Boyer-Moore匹配位置: {matches_simple}")
    
    # 可视化演示
    print("\n可视化:")
    if matches_full:
        for match_pos in matches_full:
            print(f"位置 {match_pos}: {text[:match_pos]}[{text[match_pos:match_pos+len(pattern)]}]{text[match_pos+len(pattern):]}")
    
    # 性能测试
    print("\n性能测试:")
    print(boyer_moore_performance_test())
    
    # 复杂测试
    text2 = "ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD"
    pattern2 = "ABCDABCD"
    
    matches2 = boyer_moore_search(text2, pattern2)
    print(f"\n复杂文本匹配:")
    print(f"文本长度: {len(text2)}")
    print(f"模式长度: {len(pattern2)}")
    print(f"匹配位置: {matches2}")
    
    # 可视化测试
    print("\n" + boyer_moore_visualize(pattern, text))
    
    # 算法对比
    print("\n" + boyer_moore_vs_kmp_comparison())