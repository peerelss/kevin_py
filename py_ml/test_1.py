# 定义参数
weight = 1
bias = 0

# 定义学习比率
learning_rate = 0.01

# 准备训练集，验证集和测试集
traning_set = [(2, 5), (5, 11), (6, 13), (7, 15), (8, 17)]
validating_set = [(12, 25), (1, 3)]
testing_set = [(9, 19), (13, 27)]

# 记录 weight 与 bias 的历史值
weight_history = [weight]
bias_history = [bias]

for epoch in range(1, 10000):
    print(f"epoch: {epoch}")

    # 根据训练集训练并修改参数
    for x, y in traning_set:
        # 计算预测值
        predicted = x * weight + bias
        # 计算损失
        diff = predicted - y
        loss = diff ** 2
        # 打印除错信息
        print(f"traning x: {x}, y: {y}, predicted: {predicted}, loss: {loss}, weight: {weight}, bias: {bias}")
        # 计算导函数值
        derivative_weight = 2 * diff * x
        derivative_bias = 2 * diff
        # 修改 weight 和 bias 以减少 loss
        # diff 为正时代表预测输出 > 正确输出，会减少 weight 和 bias
        # diff 为负时代表预测输出 < 正确输出，会增加 weight 和 bias
        weight -= derivative_weight * learning_rate
        bias -= derivative_bias * learning_rate
        # 记录 weight 和 bias 的历史值
        weight_history.append(weight)
        bias_history.append(bias)

    # 检查验证集
    validating_accuracy = 0
    for x, y in validating_set:
        predicted = x * weight + bias
        validating_accuracy += 1 - abs(y - predicted) / y
        print(f"validating x: {x}, y: {y}, predicted: {predicted}")
    validating_accuracy /= len(validating_set)

    # 如果验证集正确率大于 99 %，则停止训练
    print(f"validating accuracy: {validating_accuracy}")
    if validating_accuracy > 0.99:
        break

# 检查测试集
testing_accuracy = 0
for x, y in testing_set:
    predicted = x * weight + bias
    testing_accuracy += 1 - abs(y - predicted) / y
    print(f"testing x: {x}, y: {y}, predicted: {predicted}")
testing_accuracy /= len(testing_set)
print(f"testing accuracy: {testing_accuracy}")

# 显示 weight 与 bias 的变化
from matplotlib import pyplot
pyplot.plot(weight_history, label="weight")
pyplot.plot(bias_history, label="bias")
pyplot.legend()
pyplot.show()
