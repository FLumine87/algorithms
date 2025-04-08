### `std::vector` 常见方法及中文说明（表格形式）

#### **构造函数**
| 方法                                   | 说明                                                         |
|----------------------------------------|--------------------------------------------------------------|
| `vector()`                             | 创建一个空的 `vector`。                                      |
| `vector(size_type count)`              | 创建一个包含 `count` 个元素的 `vector`，元素默认初始化。     |
| `vector(size_type count, const T& value)` | 创建一个包含 `count` 个元素的 `vector`，每个元素初始化为 `value`。 |
| `vector(const vector& other)`          | 拷贝构造函数，创建一个与 `other` 相同的 `vector`。           |
---

#### **容量相关**
| 方法                  | 说明                                                         |
|-----------------------|--------------------------------------------------------------|
| `size()`              | 返回当前 `vector` 中的元素数量。                             |
| `capacity()`          | 返回当前 `vector` 分配的存储容量。                           |
| `empty()`             | 检查 `vector` 是否为空。                                     |
| `resize(size_type count)` | 调整 `vector` 的大小为 `count`，如果增大，新增元素默认初始化。 |
| `reserve(size_type new_cap)` | 预留至少 `new_cap` 的存储空间。                        |
| `shrink_to_fit()`     | 释放多余的容量，调整容量与当前大小一致。                      |
| `max_size()`          | 返回 `vector` 能容纳的最大元素数量。                         |

---

#### **元素访问**
| 方法                  | 说明                                                         |
|-----------------------|--------------------------------------------------------------|
| `operator[]`          | 通过索引访问元素，不进行边界检查。                           |
| `at(size_type pos)`   | 通过索引访问元素，带边界检查。                               |
| `front()`             | 返回第一个元素的引用。                                       |
| `back()`              | 返回最后一个元素的引用。                                     |
| `data()`              | 返回指向底层数组的指针。                                     |

---

#### **修改容器**
| 方法                                   | 说明                                                         |
|----------------------------------------|--------------------------------------------------------------|
| `push_back(const T& value)`            | 在 `vector` 的末尾添加一个元素，拷贝 `value`。               |
| `push_back(T&& value)`                 | 在 `vector` 的末尾添加一个元素，移动 `value`。               |
| `pop_back()`                           | 移除 `vector` 的最后一个元素。                               |
| `insert(iterator pos, const T& value)` | 在 `pos` 位置插入一个元素，拷贝 `value`。                    |
| `insert(iterator pos, T&& value)`      | 在 `pos` 位置插入一个元素，移动 `value`。                    |
| `insert(iterator pos, size_type count, const T& value)` | 在 `pos` 位置插入 `count` 个 `value`。                     |
| `erase(iterator pos)`                  | 移除 `pos` 位置的元素。                                      |
| `erase(iterator first, iterator last)` | 移除 `[first, last)` 范围内的元素。                         |
| `clear()`                              | 清空 `vector` 中的所有元素。                                 |
| `assign(size_type count, const T& value)` | 用 `count` 个 `value` 替换当前 `vector` 的内容。            |
| `assign(initializer_list<T> ilist)`    | 用初始化列表替换当前 `vector` 的内容。                      |

---

#### **迭代器相关**
| 方法                  | 说明                                                         |
|-----------------------|--------------------------------------------------------------|
| `begin()`             | 返回指向第一个元素的迭代器。                                 |
| `end()`               | 返回指向最后一个元素之后的迭代器。                           |
| `rbegin()`            | 返回指向最后一个元素的反向迭代器。                           |
| `rend()`              | 返回指向第一个元素之前的反向迭代器。                         |
| `cbegin()`            | 返回指向第一个元素的常量迭代器。                             |  
| `next( ForwardIt it, typename n = 1 )`          | 返回指向下一个元素的迭代器  |

---

#### **比较操作**
| 方法                  | 说明                                                         |
|-----------------------|--------------------------------------------------------------|
| `operator==`          | 检查两个 `vector` 是否相等。                                 |
| `operator!=`          | 检查两个 `vector` 是否不相等。                               |
| `operator<`           | 按字典序比较两个 `vector`。                                  |
| `operator<=`          | 按字典序比较两个 `vector`，小于或等于。                      |

---

#### **分配器相关**
| 方法                  | 说明                                                         |
|-----------------------|--------------------------------------------------------------|
| `get_allocator()`     | 返回与 `vector` 关联的分配器。                               |