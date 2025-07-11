

| **维度**    | ClaSP            | PELT            | FLUSS        | BINSEG         | STUMPY           |
| --------- | ---------------- | --------------- | ------------ | -------------- | ---------------- |
| **核心原理**  | 自监督分类 + 交叉验证找变化点 | 动态规划 + 剪枝优化成本函数 | 弧曲线找局部最小     | 递归二分 + 成本函数最小化 | 矩阵轮廓挖掘重复模式 / 异常  |
| **适用场景**  | 无超参、领域无关的变化点检测   | 已知分布假设的分割（如高斯）  | 形状差异主导的分割    | 简单分段（如分段常数）    | 相似模式 / 异常 / 周期检测 |
| **超参数依赖** | 无（自动学窗口w、变化点数C）  | 需设成本函数、惩罚项      | 需设子序列长度、变化点数 | 需设成本函数、分段数     | 需设窗口长度m、k 近邻数    |
| **关键特性**  | 强鲁棒性             | 线性时间效率          | 领域无关但依赖人工调参  | 简单场景高效         | 多任务（             |

| **维度**    | BINSEG         | STUMPY           |
| --------- | -------------- | ---------------- |
| **核心原理**  | 递归二分 + 成本函数最小化 | 矩阵轮廓挖掘重复模式 / 异常  |
| **适用场景**  | 简单分段（如分段常数）    | 相似模式 / 异常 / 周期检测 |
| **超参数依赖** | 需设成本函数、分段数     | 需设窗口长度 m、k 近邻数   |
| **关键特性**  | 简单场景高效         | 多任务（             |


| **维度**     | **ClaSP（无超参数）**            | **FLUSS（有超参数）**   | **PELT（有超参数）**    |
| ---------- | -------------------------- | ----------------- | ----------------- |
| **参数依赖性**  | 0（自动学习窗口、分段数）              | 需设置 L、n_regimes   | 需设置 penalty、成本函数  |
| **核心方法**   | 分类评分 + 统计检验                | 弧曲线极值 + 人工阈值      | 动态规划 + 成本函数最小化    |
| **时间复杂度**  | $O(C \cdot n^2)$（C 为分段数） | $O(n)$          | $O(n)$          |
| **领域适应性**  | 通用（医疗 / 工业 / 金融）           | 需调参适配领域           | 高斯分布数据效果最佳        |
| **基准测试排名** | 1st（70/107 数据集最优）          | 3rd（19/107 数据集最优） | 2nd（28/107 数据集最优） |
