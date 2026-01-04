## 三、合并排序（Merge Sort）

### 1. 分治策略（Divide-and-Conquer）
- **分（Divide）**：将序列分成两个大小相等的子序列。
- **治（Conquer）**：递归地对子序列排序。
- **合（Combine）**：合并两个有序子序列。

### 2. 合并操作
```python
def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
```

### 3. 合并排序实现
```python
def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
```

### 4. 时间复杂度分析
- 每层合并的总代价为 $O(n)$。
- 树的高度为 $O(\log n)$。
- 总时间复杂度为 $O(n \log n)$。

---

## 四、快速排序（Quick Sort）

### 1. 算法步骤
1. **分（Divide）**：选取一个基准（pivot），将序列分成三部分：
   - $L$：小于基准
   - $E$：等于基准
   - $G$：大于基准
1. **治（Conquer）**：递归地对 $L$ 和 $G$ 排序。
2. **合（Combine）**：将 $L$、$E$、$G$ 合并。

### 2. 快速排序实现
```python
def quick_sort(S):
    n = len(S)
    if n < 2:
        return
    p = S.first()          # 选取第一个元素为基准
    L, E, G = LinkedQueue(), LinkedQueue(), LinkedQueue()
    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    quick_sort(L)
    quick_sort(G)
    # 合并 L, E, G 回 S
```

### 3. 时间复杂度
- **最坏情况**：每次划分极不平衡，复杂度为 $O(n^2)$。
- **最好情况**：每次划分均匀，复杂度为 $O(n \log n)$。
- **平均情况**：在随机输入下，复杂度为 $O(n \log n)$。

---
## 三、随机化快速排序（Randomized Quick-Sort）

### 1. 目的
通过**随机选择基准**，避免最坏情况（如已排序序列）的发生，使算法在期望意义下高效。

### 2. 关键命题
**命题 12.3**：随机化快速排序在大小为 $n$ 的序列上的期望运行时间为 $O(n \log n)$。

### 3. 论证要点
- **好划分**：划分后两个子序列大小均在 $[n/4, 3n/4]$ 之间。
- **好划分的概率**：$1/2$。
- 即使存在坏划分，期望的划分层数为 $O(\log n)$。
- 每层划分的时间为 $O(n)$，因此总期望时间为 $O(n \log n)$。
