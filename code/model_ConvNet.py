import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        
        # 定义卷积层
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        
        # 定义池化层
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        
        # 定义全连接层
        self.fc1 = nn.Linear(64 * 340 * 256, 512)  # 注意：这里输入的尺寸是根据输入图像的分辨率计算得到的
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, out_features = 24)  # out_features 是数据集中的类别数量(24)

    def forward(self, x):
        # 前向传播
        
        # 卷积 -> 激活函数 -> 池化
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        # 检查输入图像的分辨率是否符合要求
        if x.size()[2:] != (340, 256):  # 如果分辨率不是 (340, 256)
            return None  # 返回空值
        
        # 将特征张量展平
        x = x.view(-1, 64 * 340 * 256)  # 注意：这里的展平操作的维度根据输入图像的分辨率计算得到的
        
        # 全连接层 -> 激活函数
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 创建模型实例
model = CNN()
