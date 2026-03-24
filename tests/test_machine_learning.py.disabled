"""
机器学习算法单元测试
"""

import unittest
import numpy as np
import sys
sys.path.append('/root/.openclaw/workspace/YuanbaoSectBot')

from algorithms.machine_learning.linear_regression import LinearRegression
from algorithms.machine_learning.logistic_regression import LogisticRegression


class TestLinearRegression(unittest.TestCase):
    """线性回归测试类"""
    
    def setUp(self):
        """设置测试数据"""
        # 简单线性回归数据
        self.X_simple = np.array([[1], [2], [3], [4], [5]])
        self.y_simple = np.array([2, 4, 6, 8, 10])
        
        # 多元线性回归数据
        self.X_multiple = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
        self.y_multiple = np.array([3, 5, 7, 9, 11])
    
    def test_simple_linear_regression_fit(self):
        """测试简单线性回归拟合"""
        model = LinearRegression(fit_intercept=True)
        model.fit(self.X_simple, self.y_simple)
        
        # 验证模型参数
        self.assertIsNotNone(model.coef_)
        self.assertIsNotNone(model.intercept_)
        
        # 预测应该准确
        predictions = model.predict(self.X_simple)
        self.assertTrue(np.allclose(predictions, self.y_simple, rtol=0.1))
        
        # R²分数应该接近1
        r2_score = model.score(self.X_simple, self.y_simple)
        self.assertGreater(r2_score, 0.9)
    
    def test_simple_linear_regression_no_intercept(self):
        """测试简单线性回归（无截距）"""
        model = LinearRegression(fit_intercept=False)
        model.fit(self.X_simple, self.y_simple)
        
        # 截距应该为0
        self.assertEqual(model.intercept_, 0.0)
        
        # 预测应该准确
        predictions = model.predict(self.X_simple)
        self.assertTrue(np.allclose(predictions, self.y_simple, rtol=0.1))
    
    def test_multiple_linear_regression_fit(self):
        """测试多元线性回归拟合"""
        model = LinearRegression(fit_intercept=True)
        model.fit(self.X_multiple, self.y_multiple)
        
        # 验证模型参数
        self.assertIsNotNone(model.coef_)
        self.assertIsNotNone(model.intercept_)
        
        # 预测应该准确
        predictions = model.predict(self.X_multiple)
        self.assertTrue(np.allclose(predictions, self.y_multiple, rtol=0.1))
        
        # R²分数应该接近1
        r2_score = model.score(self.X_multiple, self.y_multiple)
        self.assertGreater(r2_score, 0.9)
    
    def test_linear_regression_predict(self):
        """测试线性回归预测"""
        model = LinearRegression(fit_intercept=True)
        model.fit(self.X_simple, self.y_simple)
        
        # 新数据预测
        new_X = np.array([[6], [7]])
        expected = np.array([12, 14])  # y = 2x
        
        predictions = model.predict(new_X)
        self.assertTrue(np.allclose(predictions, expected, rtol=0.1))
    
    def test_linear_regression_empty_data(self):
        """测试线性回归空数据"""
        model = LinearRegression(fit_intercept=True)
        
        # 空数据应该产生错误
        X_empty = np.array([])
        y_empty = np.array([])
        
        with self.assertRaises(Exception):
            model.fit(X_empty, y_empty)
    
    def test_linear_regression_summary(self):
        """测试模型摘要"""
        model = LinearRegression(fit_intercept=True)
        model.fit(self.X_simple, self.y_simple)
        
        summary = model.summary()
        self.assertIn("线性回归模型", summary)
        self.assertIn("拟合截距项", summary)
        self.assertIn("回归系数", summary)


class TestLogisticRegression(unittest.TestCase):
    """逻辑回归测试类"""
    
    def setUp(self):
        """设置测试数据"""
        # 二元分类数据
        self.X_binary = np.array([[0.5, 1], [1.5, 1], [2.5, 2], [3.5, 2], [4.5, 3]])
        self.y_binary = np.array([0, 0, 1, 1, 1])
        
        # 数据形状验证
        self.assertEqual(self.X_binary.shape[0], self.y_binary.shape[0])
    
    def test_logistic_regression_fit(self):
        """测试逻辑回归拟合"""
        model = LogisticRegression(learning_rate=0.1, iterations=1000, fit_intercept=True)
        model.fit(self.X_binary, self.y_binary)
        
        # 验证模型参数
        self.assertIsNotNone(model.coef_)
        self.assertIsNotNone(model.intercept_)
        
        # 应该有损失历史记录
        self.assertGreater(len(model.loss_history), 0)
        
        # 损失应该递减（或基本递减）
        if len(model.loss_history) > 10:
            self.assertLess(model.loss_history[-1], model.loss_history[0])
    
    def test_logistic_regression_predict_proba(self):
        """测试概率预测"""
        model = LogisticRegression(learning_rate=0.1, iterations=1000, fit_intercept=True)
        model.fit(self.X_binary, self.y_binary)
        
        # 概率预测应该在0-1范围内
        probabilities = model.predict_proba(self.X_binary)
        self.assertTrue(np.all(probabilities >= 0))
        self.assertTrue(np.all(probabilities <= 1))
        
        # 类别0应该概率较低，类别1应该概率较高
        prob_class0 = probabilities[self.y_binary == 0]
        prob_class1 = probabilities[self.y_binary == 1]
        
        self.assertTrue(np.mean(prob_class0) < np.mean(prob_class1))
    
    def test_logistic_regression_predict(self):
        """测试类别预测"""
        model = LogisticRegression(learning_rate=0.1, iterations=1000, fit_intercept=True)
        model.fit(self.X_binary, self.y_binary)
        
        predictions = model.predict(self.X_binary)
        
        # 预测应该是整数0或1
        self.assertTrue(np.all(predictions >= 0))
        self.assertTrue(np.all(predictions <= 1))
        
        # 准确率应该较高
        accuracy = model.score(self.X_binary, self.y_binary)
        self.assertGreater(accuracy, 0.7)
    
    def test_logistic_regression_confusion_matrix(self):
        """测试混淆矩阵"""
        model = LogisticRegression(learning_rate=0.1, iterations=1000, fit_intercept=True)
        model.fit(self.X_binary, self.y_binary)
        
        confusion = model.confusion_matrix(self.X_binary, self.y_binary)
        
        # 验证混淆矩阵格式
        self.assertIn("TP", confusion)
        self.assertIn("FP", confusion)
        self.assertIn("TN", confusion)
        self.assertIn("FN", confusion)
        
        # 所有值应该是整数
        self.assertIsInstance(confusion["TP"], (int, np.integer))
        self.assertIsInstance(confusion["FP"], (int, np.integer))
        self.assertIsInstance(confusion["TN"], (int, np.integer))
        self.assertIsInstance(confusion["FN"], (int, np.integer))
    
    def test_logistic_regression_empty_data(self):
        """测试逻辑回归空数据"""
        model = LogisticRegression()
        
        # 空数据应该产生错误
        X_empty = np.array([])
        y_empty = np.array([])
        
        with self.assertRaises(Exception):
            model.fit(X_empty, y_empty)
    
    def test_logistic_regression_summary(self):
        """测试模型摘要"""
        model = LogisticRegression(learning_rate=0.1, iterations=1000, fit_intercept=True)
        model.fit(self.X_binary, self.y_binary)
        
        summary = model.summary()
        self.assertIn("逻辑回归模型", summary)
        self.assertIn("拟合截距项", summary)
        self.assertIn("学习率", summary)
        self.assertIn("迭代次数", summary)
        self.assertIn("回归系数", summary)
    
    def test_logistic_regression_sigmoid_function(self):
        """测试Sigmoid函数"""
        model = LogisticRegression()
        
        # Sigmoid函数测试
        test_values = np.array([-10, -1, 0, 1, 10])
        sigmoid_results = model.sigmoid(test_values)
        
        # Sigmoid应该在0-1范围内
        self.assertTrue(np.all(sigmoid_results >= 0))
        self.assertTrue(np.all(sigmoid_results <= 1))
        
        # 负值应该接近0，正值应该接近1
        self.assertTrue(sigmoid_results[0] < 0.001)  # -10
        self.assertTrue(sigmoid_results[-1] > 0.999)  # 10


def test_linear_regression_edge_cases():
    """测试线性回归边界情况"""
    print("\n测试线性回归边界情况:")
    
    # 测试奇异矩阵
    X_singular = np.array([[1, 1], [1, 1], [1, 1]])
    y_singular = np.array([2, 2, 2])
    
    model = LinearRegression(fit_intercept=True)
    try:
        model.fit(X_singular, y_singular)
        print("奇异矩阵测试通过")
    except Exception as e:
        print(f"奇异矩阵测试失败: {e}")
    
    # 测试单个样本
    X_single = np.array([[1]])
    y_single = np.array([1])
    
    model = LinearRegression(fit_intercept=True)
    try:
        model.fit(X_single, y_single)
        print("单个样本测试通过")
    except Exception as e:
        print(f"单个样本测试失败: {e}")


def test_logistic_regression_edge_cases():
    """测试逻辑回归边界情况"""
    print("\n测试逻辑回归边界情况:")
    
    # 测试所有样本都是同一个类别
    X_uniform = np.array([[1], [2], [3]])
    y_uniform = np.array([1, 1, 1])  # 全是1
    
    model = LogisticRegression()
    try:
        model.fit(X_uniform, y_uniform)
        print("均匀类别测试通过")
    except Exception as e:
        print(f"均匀类别测试失败: {e}")
    
    # 测试极端概率值
    X_extreme = np.array([[-100], [100]])
    y_extreme = np.array([0, 1])
    
    model = LogisticRegression()
    try:
        model.fit(X_extreme, y_extreme)
        probabilities = model.predict_proba(X_extreme)
        print(f"极端概率测试通过，概率值: {probabilities}")
    except Exception as e:
        print(f"极端概率测试失败: {e}")


if __name__ == "__main__":
    unittest.main()
    
    # 运行边界情况测试
    test_linear_regression_edge_cases()
    test_logistic_regression_edge_cases()