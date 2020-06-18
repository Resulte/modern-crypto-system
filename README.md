# modern-crypto-system
现代密码加解密系统，自行设计的基于Feistel结构的分组密码+AES密码，python实现

# 分组密码

自行设计的基于Feistel结构的分组密码，包含有雪崩效应分析。

采用的轮函数为异或，对于函数为简单的异或函数的feistel网络来说，难以达到雪崩效应的要求（50%以上），但是随着加密轮次的提升，雪崩效应也越来越大。

### 效果演示

雪崩效应分析：给出一个随机的输入，改变1比特后，追踪所有各处理环节及轮次改变的比特数量比例

![效果演示](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/modern1.png)

# AES密码

### 流程图

![流程图](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/modern2.png)

### 效果演示

![效果演示](https://edu-boker.oss-cn-beijing.aliyuncs.com/crypto/modern3.png)