"""
线性回归算法实现
"""

import numpy as np


class LinearRegression:
    """
    线性回归模型

    使用最小二乘法求解线性回归问题

    参数:
        fit_intercept (bool): 是否拟合截距项

    属性:
        coef_ (ndarray): 回归系数
        intercept_ (float): 截距项
    """

    def __init__(self, fit_intercept=True):
        """
        初始化线性回归模型

        参数:
            fit_intercept (bool): 是否拟合截距项
        """
        self.fit_intercept = fit_intercept
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        """
        拟合线性回归模型

        参数:
            X (ndarray): 特征矩阵，形状为 (n_samples, n_features)
            y (ndarray): 目标变量，形状为 (n_samples,)

        返回:
            self: 拟合后的模型
        """
        n_samples, n_features = X.shape

        # 如果需要拟合截距项，添加截距列
        if self.fit_intercept:
            X = np.c_[np.ones(n_samples), X]

        # 最小二乘法求解
        try:
            # 使用正规方程法求解权重
            weights = np.linalg.pinv(X.T @ X) @ X.T @ y

            if self.fit_intercept:
                self.intercept_ = weights[0]
                self.coef_ = weights[1:]
            else:
                self.intercept_ = 0.0
                self.coef_ = weights

        except np.linalg.LinAlgError:
            # 如果矩阵不可逆，使用梯度下降法
            self._gradient_descent(X, y)

        return self

    def predict(self, X):
        """
        预测目标变量

        参数:
            X (ndarray): 特征矩阵，形状为 (n_samples, n_features)

        返回:
            ndarray: 预测值，形状为 (n_samples,)
        """
        if self.fit_intercept:
            predictions = self.intercept_ + np.dot(X, self.coef_)
        else:
            predictions = np.dot(X, self.coef_)

        return predictions

    def score(self, X, y):
        """
        计算模型的R²分数

        参数:
            X (ndarray): 特征矩阵
            y (ndarray): 真实目标变量

        返回:
            float: R²分数
        """
        predictions = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - predictions) ** 2)

        r2 = 1 - (ss_residual / ss_total)
        return r2

    def _gradient_descent(self, X, y, learning_rate=0.01, iterations=1000):
        """
        梯度下降法训练模型

        参数:
            X (ndarray): 特征矩阵
            y (ndarray): 目标变量
            learning_rate (float): 学习率
            iterations (int): 迭代次数

        返回:
            None
        """
        n_samples, n_features = X.shape

        # 初始化权重
        weights = np.zeros(n_features)

        for i in range(iterations):
            # 预测值
            predictions = np.dot(X, weights)

            # 计算梯度
            gradient = -2 / n_samples * np.dot(X.T, (y - predictions))

            # 更新权重
            weights -= learning_rate * gradient

        if self.fit_intercept:
            self.intercept_ = weights[0]
            self.coef_ = weights[1:]
        else:
            self.intercept_ = 0.0
            self.coef_ = weights

    def summary(self):
        """
        打印模型摘要

        返回:
            str: 模型信息摘要
        """
        if self.coef_ is None:
            return "模型尚未训练"

        info = f"线性回归模型\n"
        info += f"拟合截距项: {self.fit_intercept}\n"
        if self.fit_intercept:
            info += f"截距项: {self.intercept_:.4f}\n"
        info += f"回归系数:\n"
        for i, coef in enumerate(self.coef_):
            info += f"  Feature {i}: {coef:.4f}\n"

        return info


def simple_linear_regression_demo():
    """
    线性回归演示示例
    """
    # 生成示例数据
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1, 3, 2, 5, 4])

    print("线性回归示例:")
    print(f"特征矩阵 X: {X}")
    print(f"目标变量 y: {y}")

    # 创建并训练模型
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)

    print("\n模型摘要:")
    print(model.summary())

    # 预测
    predictions = model.predict(X)
    print(f"\n预测值: {predictions}")

    # 计算R²分数
    r2_score = model.score(X, y)
    print(f"R²分数: {r2_score:.4f}")

    # 新数据预测
    new_X = np.array([[6], [7]])
    new_predictions = model.predict(new_X)
    print(f"\n新数据预测: {new_predictions}")


def multiple_linear_regression_demo():
    """
    多元线性回归演示示例
    """
    # 生成示例数据（2个特征）
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([3, 5, 7, 9, 11])

    print("多元线性回归示例:")
    print(f"特征矩阵 X (shape: {X.shape}):\n{X}")
    print(f"目标变量 y: {y}")

    # 创建并训练模型
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)

    print("\n模型摘要:")
    print(model.summary())

    # 预测
    predictions = model.predict(X)
    print(f"\n预测值: {predictions}")

    # 计算R²分数
    r2_score = model.score(X, y)
    print(f"R²分数: {r2_score:.4f}")


if __name__ == "__main__":
    print("线性回归算法演示")
    print("================\n")

    # 简单线性回归演示
    simple_linear_regression_demo()

    print("\n\n================\n")

    # 多元线性回归演示
    multiple_linear_regression_demo()
