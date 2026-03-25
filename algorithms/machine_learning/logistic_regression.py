"""
逻辑回归算法实现
"""

import numpy as np


class LogisticRegression:
    """
    逻辑回归模型

    使用梯度下降法求解逻辑回归问题

    参数:
        learning_rate (float): 学习率
        iterations (int): 迭代次数
        fit_intercept (bool): 是否拟合截距项

    属性:
        coef_ (ndarray): 回归系数
        intercept_ (float): 截距项
    """

    def __init__(self, learning_rate=0.01, iterations=1000, fit_intercept=True):
        """
        初始化逻辑回归模型

        参数:
            learning_rate (float): 学习率
            iterations (int): 迭代次数
            fit_intercept (bool): 是否拟合截距项
        """
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.fit_intercept = fit_intercept
        self.coef_ = None
        self.intercept_ = None
        self.loss_history = []

    def sigmoid(self, z):
        """
        Sigmoid函数

        参数:
            z (ndarray): 输入

        返回:
            ndarray: Sigmoid输出
        """
        return 1 / (1 + np.exp(-z))

    def predict_proba(self, X):
        """
        预测概率

        参数:
            X (ndarray): 特征矩阵

        返回:
            ndarray: 概率值
        """
        if self.fit_intercept:
            scores = self.intercept_ + np.dot(X, self.coef_)
        else:
            scores = np.dot(X, self.coef_)

        probabilities = self.sigmoid(scores)
        return probabilities

    def predict(self, X, threshold=0.5):
        """
        预测类别

        参数:
            X (ndarray): 特征矩阵
            threshold (float): 分类阈值

        返回:
            ndarray: 预测类别
        """
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)

    def fit(self, X, y):
        """
        拟合逻辑回归模型

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
            n_features += 1

        # 初始化权重
        weights = np.zeros(n_features)

        # 梯度下降
        for i in range(self.iterations):
            # 计算预测概率
            probabilities = self.sigmoid(np.dot(X, weights))

            # 计算梯度
            gradient = np.dot(X.T, (probabilities - y)) / n_samples

            # 更新权重
            weights -= self.learning_rate * gradient

            # 计算损失（对数损失）
            loss = -np.mean(
                y * np.log(probabilities) + (1 - y) * np.log(1 - probabilities)
            )
            self.loss_history.append(loss)

        if self.fit_intercept:
            self.intercept_ = weights[0]
            self.coef_ = weights[1:]
        else:
            self.intercept_ = 0.0
            self.coef_ = weights

        return self

    def score(self, X, y, threshold=0.5):
        """
        计算模型的准确率

        参数:
            X (ndarray): 特征矩阵
            y (ndarray): 真实目标变量
            threshold (float): 分类阈值

        返回:
            float: 准确率
        """
        predictions = self.predict(X, threshold)
        accuracy = np.mean(predictions == y)
        return accuracy

    def confusion_matrix(self, X, y, threshold=0.5):
        """
        计算混淆矩阵

        参数:
            X (ndarray): 特征矩阵
            y (ndarray): 真实目标变量
            threshold (float): 分类阈值

        返回:
            dict: 混淆矩阵各项指标
        """
        predictions = self.predict(X, threshold)

        tp = np.sum((predictions == 1) & (y == 1))  # 真正例
        fp = np.sum((predictions == 1) & (y == 0))  # 假正例
        tn = np.sum((predictions == 0) & (y == 0))  # 真负例
        fn = np.sum((predictions == 0) & (y == 1))  # 假负例

        confusion_matrix = {"TP": tp, "FP": fp, "TN": tn, "FN": fn}

        return confusion_matrix

    def summary(self):
        """
        打印模型摘要

        返回:
            str: 模型信息摘要
        """
        if self.coef_ is None:
            return "模型尚未训练"

        info = f"逻辑回归模型\n"
        info += f"拟合截距项: {self.fit_intercept}\n"
        info += f"学习率: {self.learning_rate}\n"
        info += f"迭代次数: {self.iterations}\n"
        if self.fit_intercept:
            info += f"截距项: {self.intercept_:.4f}\n"
        info += f"回归系数:\n"
        for i, coef in enumerate(self.coef_):
            info += f"  Feature {i}: {coef:.4f}\n"
        if self.loss_history:
            info += f"最终损失: {self.loss_history[-1]:.4f}\n"

        return info


def logistic_regression_demo():
    """
    逻辑回归演示示例
    """
    # 生成示例数据（2个特征）
    X = np.array([[0.5, 1], [1.5, 1], [2.5, 2], [3.5, 2], [4.5, 3]])
    y = np.array([0, 0, 1, 1, 1])

    print("逻辑回归示例:")
    print(f"特征矩阵 X:\n{X}")
    print(f"目标变量 y: {y}")

    # 创建并训练模型
    model = LogisticRegression(learning_rate=0.1, iterations=1000, fit_intercept=True)
    model.fit(X, y)

    print("\n模型摘要:")
    print(model.summary())

    # 预测概率和类别
    probabilities = model.predict_proba(X)
    predictions = model.predict(X)

    print(f"\n预测概率: {probabilities}")
    print(f"预测类别: {predictions}")

    # 计算准确率
    accuracy = model.score(X, y)
    print(f"准确率: {accuracy:.4f}")

    # 混淆矩阵
    confusion = model.confusion_matrix(X, y)
    print(f"\n混淆矩阵:")
    print(f"  TP (真正例): {confusion['TP']}")
    print(f"  FP (假正例): {confusion['FP']}")
    print(f"  TN (真负例): {confusion['TN']}")
    print(f"  FN (假负例): {confusion['FN']}")

    # 新数据预测
    new_X = np.array([[1.5, 2], [3.0, 2.5]])
    new_probabilities = model.predict_proba(new_X)
    new_predictions = model.predict(new_X)

    print(f"\n新数据:")
    print(f"  数据: {new_X}")
    print(f"  预测概率: {new_probabilities}")
    print(f"  预测类别: {new_predictions}")


def multiclass_logistic_regression_demo():
    """
    多分类逻辑回归演示示例
    """
    # 生成多分类示例数据
    X = np.array([[0, 1], [1, 2], [2, 3], [3, 4], [4, -1], [-1, -2]])
    y = np.array([0, 1, 1, 2, 0, 2])

    print("多分类逻辑回归示例:")
    print(f"特征矩阵 X:\n{X}")
    print(f"目标变量 y: {y}")

    # 为每个类别创建逻辑回归模型
    models = []
    for class_id in np.unique(y):
        # 将问题转换为二元分类
        binary_y = np.where(y == class_id, 1, 0)

        model = LogisticRegression(
            learning_rate=0.1, iterations=500, fit_intercept=True
        )
        model.fit(X, binary_y)
        models.append((class_id, model))

    print("\n多分类模型摘要:")
    for class_id, model in models:
        print(f"类别 {class_id}:")
        print(f"  截距项: {model.intercept_:.4f}")
        print(f"  系数: {model.coef_}")
        print(f"  损失: {model.loss_history[-1]:.4f}")

    # 多分类预测
    new_X = np.array([[1, 1.5], [2.5, 3]])

    predictions = []
    probabilities = []

    for sample in new_X:
        sample_probabilities = []
        for class_id, model in models:
            prob = model.predict_proba(sample.reshape(1, -1))
            sample_probabilities.append(prob[0])

        # 选择概率最高的类别
        best_class = np.argmax(sample_probabilities)
        predictions.append(best_class)
        probabilities.append(sample_probabilities)

    print(f"\n新数据:")
    print(f"  数据: {new_X}")
    print(f"  预测概率: {probabilities}")
    print(f"  预测类别: {predictions}")


if __name__ == "__main__":
    print("逻辑回归算法演示")
    print("================\n")

    # 二元分类演示
    logistic_regression_demo()

    print("\n\n================\n")

    # 多分类演示
    multiclass_logistic_regression_demo()
