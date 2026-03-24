"""
计算几何算法模块
包括凸包算法和最近点对算法
"""

from .convex_hull_basic import (
    convex_hull_graham,
    convex_hull_jarvis,
    convex_hull_distance,
    convex_hull_visualize
)

from .convex_hull_advanced import (
    convex_hull_quickhull,
    convex_hull_brute_force,
    convex_hull_performance_test
)

from .closest_pair_basic import (
    distance,
    closest_pair_brute_force,
    closest_pair_divide_and_conquer,
    closest_pair_recursive
)

from .closest_pair_advanced import (
    closest_pair_kd_tree,
    closest_pair_performance_test,
    closest_pair_visualize,
    closest_pair_all_points
)