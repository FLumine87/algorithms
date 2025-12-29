| 函数                         | 语法                                                    | 功能描述                   |
| -------------------------- | ----------------------------------------------------- | ---------------------- |
| **排序相关**                   |                                                       |                        |
| `sort`                     | `sort(begin, end);`                                   | 对范围[begin,end)升序排序     |
| `stable_sort`              | `stable_sort(begin, end);`                            | 稳定排序（相等元素保持原序）         |
| `partial_sort`             | `partial_sort(begin, middle, end);`                   | 部分排序，使[begin,middle)有序 |
| `nth_element`              | `nth_element(begin, nth, end);`                       | 使第n个元素处于正确位置           |
| **查找相关**                   |                                                       |                        |
| `find`                     | `find(begin, end, value);`                            | 线性查找，返回迭代器             |
| `find_if`                  | `find_if(begin, end, pred);`                          | 查找满足条件的元素              |
| `binary_search`            | `binary_search(begin, end, value);`                   | 二分查找（需已排序）             |
| `lower_bound`              | `lower_bound(begin, end, value);`                     | 返回不小于value的第一个位置       |
| `upper_bound`              | `upper_bound(begin, end, value);`                     | 返回大于value的第一个位置        |
| `equal_range`              | `equal_range(begin, end, value);`                     | 返回等于value的范围           |
| **修改操作**                   |                                                       |                        |
| `reverse`                  | `reverse(begin, end);`                                | 反转元素顺序                 |
| `rotate`                   | `rotate(begin, middle, end);`                         | 循环移位                   |
| `shuffle`                  | `shuffle(begin, end, gen);`                           | 随机重排                   |
| `fill`                     | `fill(begin, end, value);`                            | 用value填充范围             |
| `fill_n`                   | `fill_n(begin, n, value);`                            | 用value填充n个元素           |
| `copy`                     | `copy(src_begin, src_end, dest);`                     | 复制范围                   |
| `copy_n`                   | `copy_n(src, n, dest);`                               | 复制n个元素                 |
| `move`                     | `move(src_begin, src_end, dest);`                     | 移动元素（C++11）            |
| `replace`                  | `replace(begin, end, old_val, new_val);`              | 替换值                    |
| `replace_if`               | `replace_if(begin, end, pred, new_val);`              | 替换满足条件的值               |
| `swap`                     | `swap(a, b);`                                         | 交换两个值                  |
| `swap_ranges`              | `swap_ranges(begin1, end1, begin2);`                  | 交换两个范围                 |
| **数值操作**                   |                                                       |                        |
| `max_element`              | `max_element(begin, end);`                            | 返回最大元素的迭代器             |
| `min_element`              | `min_element(begin, end);`                            | 返回最小元素的迭代器             |
| `minmax_element`           | `minmax_element(begin, end);`                         | 返回最小和最大元素的迭代器          |
| `count`                    | `count(begin, end, value);`                           | 统计值出现的次数               |
| `count_if`                 | `count_if(begin, end, pred);`                         | 统计满足条件的元素个数            |
| **集合操作**                   |                                                       |                        |
| `merge`                    | `merge(begin1, end1, begin2, end2, dest);`            | 合并两个已排序范围              |
| `set_union`                | `set_union(begin1, end1, begin2, end2, dest);`        | 求并集                    |
| `set_intersection`         | `set_intersection(begin1, end1, begin2, end2, dest);` | 求交集                    |
| `set_difference`           | `set_difference(begin1, end1, begin2, end2, dest);`   | 求差集                    |
| `set_symmetric_difference` | `set_symmetric_difference(...);`                      | 求对称差集                  |
| `includes`                 | `includes(begin1, end1, begin2, end2);`               | 检查是否包含                 |
| **堆操作**                    |                                                       |                        |
| `make_heap`                | `make_heap(begin, end);`                              | 将范围构造成堆                |
| `push_heap`                | `push_heap(begin, end);`                              | 向堆中添加元素                |
| `pop_heap`                 | `pop_heap(begin, end);`                               | 从堆中移除最大元素              |
| `sort_heap`                | `sort_heap(begin, end);`                              | 将堆排序为升序序列              |
| **排列操作**                   |                                                       |                        |
| `next_permutation`         | `next_permutation(begin, end);`                       | 生成下一个排列                |
| `prev_permutation`         | `prev_permutation(begin, end);`                       | 生成上一个排列                |
| `is_permutation`           | `is_permutation(begin1, end1, begin2);`               | 检查是否为排列                |

