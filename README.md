# YuanbaoSectBot - Python 算法库

这是一个包含常见 Python 算法的项目，旨在为开发者提供参考和学习资源。

## 目录结构

- `algorithms/` - 主要算法目录
  - `sorting/` - 排序算法
    - `bubble_sort.py` - 冒泡排序
    - `quick_sort.py` - 快速排序
    - `merge_sort.py` - 归并排序
  - `data_structures/` - 数据结构实现
    - `linked_list.py` - 链表（单向、双向）
    - `stack_queue.py` - 栈、队列、双端队列
  - `search/` - 搜索算法
    - `binary_search.py` - 二分搜索
    - `dfs.py` - 深度优先搜索
    - `bfs.py` - 广度优先搜索
  - `graph/` - 图算法
    - `dijkstra.py` - Dijkstra最短路径算法
    - `minimum_spanning_tree.py` - 最小生成树算法
  - `mathematical/` - 数学算法
    - `primes.py` - 质数生成、质因数分解、GCD、LCM
    - `fibonacci.py` - 斐波那契数列（多种实现）
  - `dynamic_programming/` - 动态规划算法
    - `fibonacci_dp.py` - 斐波那契数列的动态规划实现
    - `knapsack.py` - 背包问题（0/1、完全、多重背包）

## 算法分类

### 排序算法
1. **冒泡排序** (Bubble Sort)
2. **快速排序** (Quick Sort)
3. **归并排序** (Merge Sort)

### 数据结构
1. **链表** (Linked List) - 单向和双向链表实现
2. **栈** (Stack) - LIFO数据结构
3. **队列** (Queue) - FIFO数据结构
4. **双端队列** (Deque) - 双向操作数据结构

### 搜索算法
1. **二分搜索** (Binary Search) - 标准、递归、左右边界搜索
2. **深度优先搜索** (DFS) - 递归、迭代实现，包含路径查找和环检测
3. **广度优先搜索** (BFS) - 标准、最短路径、双向BFS等

### 图算法
1. **最短路径** (Dijkstra算法) - 邻接矩阵和邻接列表实现
2. **最小生成树** (Prim、Kruskal算法)

### 数学算法
1. **质数生成** (Prime Numbers) - 质数判断、筛法、质因数分解
2. **最大公约数** (GCD) - Euclidean算法
3. **最小公倍数** (LCM) - 基于GCD计算
4. **斐波那契数列** (Fibonacci) - 递归、迭代、动态规划、矩阵幂等

### 动态规划算法
1. **斐波那契数列** - 多种DP实现（标准、优化、自顶向下、自底向上）
2. **背包问题** - 0/1背包、完全背包、多重背包，包含物品选择追踪

## 使用方法

每个算法文件都包含详细的注释和使用示例。

```python
from algorithms.sorting.bubble_sort import bubble_sort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

```python
from algorithms.search.binary_search import binary_search

arr = [1, 3, 5, 7, 9, 11, 13, 15]
index = binary_search(arr, 7)
print(f"目标值索引: {index}")  # 3
```

```python
from algorithms.dynamic_programming.knapsack import knapsack_01

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
max_value = knapsack_01(weights, values, capacity)
print(f"最大价值: {max_value}")  # 11
```

## 项目特点

1. **详细的注释** - 每个算法都有详细的注释说明
2. **多种实现方式** - 同一个算法可能有多种不同的实现
3. **性能对比** - 部分文件包含不同算法的性能对比测试
4. **示例测试** - 每个文件都包含完整的测试用例
5. **代码清晰** - 代码结构清晰，易于理解和学习

## 📊 项目统计

- **总共 32 个文件**
- **超过 4000 行代码**
- **6 个主要分类**: 排序算法、数据结构、搜索算法、图算法、数学算法、动态规划
- **每个文件都有完整的测试用例**
- **详细的注释说明每个算法的原理和使用方法**

## 🧪 测试与质量保证

项目包含完整的单元测试：

- `tests/test_sorting.py` - 排序算法测试
- `tests/test_data_structures.py` - 数据结构测试
- `tests/test_search.py` - 搜索算法测试

### 运行测试
```bash
# 运行所有测试
python tests/run_all_tests.py

# 运行单个测试模块
python -m unittest tests/test_sorting.py
```

## 🔧 GitHub Actions 自动化

项目配置了 GitHub Actions 自动化流程，包含：
- **自动化测试** - 每次提交时自动运行单元测试
- **代码质量检查** - 自动检查代码格式和语法
- **覆盖率报告** - 生成代码覆盖率报告

## 📖 详细文档

查看 `docs/README.md` 获取完整的中文文档，包括：
- **算法分类详细介绍**
- **API接口说明**
- **性能分析和复杂度说明**
- **使用示例和最佳实践**

## 🤝 贡献

欢迎提交新的算法实现或改进现有算法。请遵循以下步骤：

1. Fork 项目
2. 创建新的分支
3. 实现新的算法
4. **必须添加对应的单元测试**
5. 提交更改
6. 创建 Pull Request

## 🔐 安全规范

项目包含 `.gitignore` 文件，防止隐私文件（如 SSH 密钥、配置文件）被意外上传到 GitHub。

## 许可证

MIT License