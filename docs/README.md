# YuanbaoSectBot 算法库中文文档

## 📚 项目简介

YuanbaoSectBot 是一个包含常见 Python 算法的开源库，旨在为开发者提供参考和学习资源。本项目包含 6 大类算法，共计 25 个详细的 Python 实现文件。

## 🗂️ 目录结构

### 🗂️ algorithms/
主要算法目录，包含以下子目录：

#### 📁 sorting/ - 排序算法
- `bubble_sort.py` - 冒泡排序（包含优化版）
- `quick_sort.py` - 快速排序（递归和原地版本）
- `merge_sort.py` - 归并排序（递归和迭代版本）

#### 📁 data_structures/ - 数据结构实现
- `linked_list.py` - 链表（单向和双向链表实现）
- `stack_queue.py` - 栈、队列、双端队列

#### 📁 search/ - 搜索算法
- `binary_search.py` - 二分搜索（标准、递归、左右边界搜索）
- `dfs.py` - 深度优先搜索（递归、迭代、路径查找、环检测、拓扑排序）
- `bfs.py` - 广度优先搜索（层级遍历、最短路径、双向BFS）

#### 📁 graph/ - 图算法
- `dijkstra.py` - Dijkstra最短路径算法（邻接矩阵和邻接列表实现）
- `minimum_spanning_tree.py` - 最小生成树算法（Prim和Kruskal算法）

#### 📁 mathematical/ - 数学算法
- `primes.py` - 质数生成、质因数分解、GCD、LCM
- `fibonacci.py` - 斐波那契数列（递归、迭代、动态规划、矩阵幂等实现）

#### 📁 dynamic_programming/ - 动态规划算法
- `fibonacci_dp.py` - 斐波那契数列的动态规划实现（标准、优化、自顶向下）
- `knapsack00.py` - 背包问题（0/1背包、完全背包、多重背包，包含物品选择追踪）

### 📄 主文件
- `main.py` - 示例演示文件
- `requirements.txt` - Python依赖文件
- `setup.py` - 项目配置文件
- `LICENSE` - MIT许可证
- `.gitignore` - Git忽略文件

### 📄 测试文件
- `tests/test_sorting.py` - 排序算法测试
- `tests/test_data_structures.py` - 数据结构测试
- `tests/test_search.py` - 搜索算法测试

## 📖 如何使用

### 安装依赖
```bash
pip install -r requirements.txt
```

### 导入算法
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

### 运行测试
```bash
# 运行所有测试
python -m pytest tests/

# 运行单个测试文件
python -m pytest tests/test_sorting.py

# 运行测试并生成覆盖率报告
python -m pytest tests/ --cov=algorithms --cov-report=term-missing
```

## 📊 算法详情

### 排序算法
1. **冒泡排序** (Bubble Sort)
   - 时间复杂度：O(n²)
   - 空间复杂度：O(1)
   - 特点：简单直观，适用于小数据集

2. **快速排序** (Quick Sort)
   - 时间复杂度：O(n log n)
   - 空间复杂度：O(log n)
   - 特点：高效、递归实现、分治策略

3. **归并排序** (Merge Sort)
   - 时间复杂度：O(n log n)
   - 空间复杂度：O(n)
   - 特点：稳定排序、适合大数据集

### 数据结构
1. **链表** (Linked List)
   - 单向链表：支持追加、前置、删除、搜索
   - 双向链表：支持正向和反向遍历

2. **栈和队列**
   - 栈：LIFO（后进先出）数据结构
   - 队列：FIFO（先进先出）数据结构
   - 双端队列：可以从两端添加或删除元素

### 搜索算法
1. **二分搜索** (Binary Search)
   - 时间复杂度：O(log n)
   - 适用场景：有序数组
   - 特点：高效、适用于大数据集

2. **深度优先搜索** (DFS)
   - 递归和迭代实现
   - 路径查找、环检测、拓扑排序
   - 连通分量计算

3. **广度优先搜索** (BFS)
   - 最短路径查找
   - 层级遍历、双向BFS
   - 连通分量计算

### 图算法
1. **Dijkstra最短路径算法**
   - 邻接矩阵和邻接列表实现
   - 适用于加权图
   - 找到最短路径

2. **最小生成树算法**
   - Prim算法：贪心策略
   - Kruskal算法：并集查找

### 数学算法
1. **质数生成**
   - 质数判断、筛法、质因数分解
   - GCD（最大公约数）、LCM（最小公倍数）

2. **斐波那契数列**
   - 递归、迭代、动态规划、矩阵幂实现
   - 性能对比和优化

### 动态规划算法
1. **斐波那契数列DP**
   - 标准DP、优化空间DP
   - 自顶向下、自底向上方法

2. **背包问题**
   - 0/1背包：每个物品只能选择一次
   - 完全背包：每个物品可以选择多次
   - 多重背包：每个物品有数量限制

## 🧪 测试覆盖率

项目包含完整的单元测试，确保算法正确性：
- **排序算法测试**：验证各种排序算法的正确性和性能
- **数据结构测试**：验证链表、栈、队列的功能
- **搜索算法测试**：验证搜索算法的正确性和边界情况

## 🔧 GitHub Actions

项目配置了 GitHub Actions 自动化流程：
- **测试自动化**：每次提交时自动运行单元测试
- **代码质量检查**：自动检查代码格式和语法
- **覆盖率报告**：生成代码覆盖率报告

## 🚀 后续开发计划

1. **更多算法**：添加选择排序、插入排序、堆排序等
2. **更多数据结构**：二叉树、哈希表、堆等
3. **性能测试**：各算法的性能对比和优化
4. **可视化工具**：算法的可视化演示
5. **中文文档**：完善的中文使用文档

## 📄 许可证

本项目采用 MIT 许可证，详情请查看 LICENSE 文件。

## 🤝 贡献指南

欢迎贡献新的算法实现或改进现有算法！

1. Fork 项目
2. 创建新的分支
3. 实现新的算法
4. 添加单元测试
5. 提交更改
6. 创建 Pull Request