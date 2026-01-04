## 三、映射（Map）与字典（Dictionary）

### 1. 基本概念
- **映射**：一种存储键值对（key-value pairs）的数据结构
- **字典**：Python 中对映射的实现（`dict`）
- 键必须唯一，值可重复

### 2. 常见应用场景
- ID → 姓名映射
- 域名 → IP 地址
- 用户名 → 个人资料
- 颜色名 → RGB 值

### 3. Map ADT（抽象数据类型）
课件中列出了映射的标准操作，包括：
- `M[k]`：查找
- `M[k] = v`：插入/更新
- `del M[k]`：删除
- `len(M)`
- `iter(M)`
- `M.get(k, default)`
- `M.setdefault(k, default)`
- `M.pop(k)`
- `M.items()`, `M.keys()`, `M.values()`
- `M.update(M2)`

---

## 四、无序映射实现（UnsortedTableMap）

### 1. 实现方式
- 使用 Python 列表存储 `_Item` 对象（键值对）
- 键值对存储顺序无关

### 2. 时间复杂度
| 操作     | 时间复杂度           |
| ------ | --------------- |
| `find` | O(n)            |
| `set`  | O(n)（需先查找是否已存在） |
| `del`  | O(n)            |
| 遍历     | O(n)            |

### 3. 优点与缺点
- 优点：实现简单
- 缺点：查找效率低

---

## 五、有序映射实现（SortedTableMap）

### 1. 实现方式
- 使用有序数组存储键值对，按键排序
- 支持**二分查找**

### 2. 支持的操作（除基本 Map 操作外）
- `find_min()`, `find_max()`
- `find_lt(k)`, `find_le(k)`, `find_gt(k)`, `find_ge(k)`
- `find_range(start, stop)`
- `reversed()`

### 3. 时间复杂度
| 操作                    | 时间复杂度                 |
| --------------------- | --------------------- |
| `find`（二分）            | O(log n)              |
| `set/del`             | O(n)（需移动元素）           |
| `find_min`/`find_max` | O(1)                  |
| `find_range`          | O(log n + s)（s 为结果数量） |

---

## 六、Python 中的映射抽象基类（MutableMapping）

### 1. `MutableMapping` 类
- Python `collections` 模块中的抽象基类
- 提供了除以下五个方法外的所有默认实现：
  - `__getitem__`
  - `__setitem__`
  - `__delitem__`
  - `__len__`
  - `__iter__`

### 2. `MapBase` 类
- 自定义的抽象基类，包含嵌套类 `_Item`
- `_Item` 用于存储键值对，支持比较操作（基于键）
