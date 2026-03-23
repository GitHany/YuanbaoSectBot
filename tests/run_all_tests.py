"""
运行所有测试的脚本
"""

import unittest
import sys

def run_all_tests():
    """运行所有单元测试"""
    # 发现所有测试
    loader = unittest.TestLoader()
    suite = loader.discover('./tests')
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回测试结果
    if result.failures or result.errors:
        print("\n❌ 测试失败或出错")
        return False
    else:
        print("\n✅ 所有测试通过")
        return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)