C++ 标准模板库（STL）提供了一组通用的容器类，用于存储和管理数据。以下是 STL 中的主要容器及其详细介绍：
# 顺序容器
## vector
描述：动态数组，支持快速随机访问和在末尾插入/删除元素。
特点：动态调整大小，支持随机访问。
时间复杂度：随机访问 O(1)，在末尾插入/删除 O(1)（摊销），在中间插入/删除 O(n)。
示例：  
```cpp
#include <vector>
#include <iostream>
int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.push_back(6);
    std::cout << vec[2] << std::endl; // 输出 3
    return 0;
}  
```
## deque
描述：双端队列，支持在两端快速插入/删除元素。
特点：双端操作高效，支持随机访问。
时间复杂度：随机访问 O(1)，在两端插入/删除 O(1)。
示例：  
```cpp
#include <deque>
#include <iostream>
int main() {
    std::deque<int> deq = {1, 2, 3, 4, 5};
    deq.push_front(0);
    deq.push_back(6);
    std::cout << deq[2] << std::endl; // 输出 2
    return 0;
}  
```
## list
描述：双向链表，支持在任意位置快速插入/删除元素。
特点：双向链表，不支持随机访问。
时间复杂度：插入/删除 O(1)，访问 O(n)。
示例：  
```cpp
#include <list>
#include <iostream>
int main() {
    std::list<int> lst = {1, 2, 3, 4, 5};
    lst.push_back(6);
    lst.push_front(0);
    auto it = lst.begin();
    std::advance(it, 2);
    std::cout << *it << std::endl; // 输出 1
    return 0;
}  
```
## forward_list
描述：单向链表，支持在任意位置快速插入/删除元素。
特点：单向链表，不支持随机访问。
时间复杂度：插入/删除 O(1)，访问 O(n)。
示例：  
```cpp
#include <forward_list>
#include <iostream>
int main() {
    std::forward_list<int> flst = {1, 2, 3, 4, 5};
    flst.push_front(0);
    auto it = flst.begin();
    std::advance(it, 2);
    std::cout << *it << std::endl; // 输出 1
    return 0;
}  
```
# 关联容器
## set
描述：有序集合，存储唯一元素，自动排序。
特点：元素唯一，自动排序。
时间复杂度：插入/删除/查找 O(log n)。
示例：  
```cpp
#include <set>
#include <iostream>
int main() {
    std::set<int> s = {3, 1, 4, 1, 5};
    s.insert(2);
    std::cout << *s.begin() << std::endl; // 输出 1
    return 0;
}  
```
## multiset
描述：有序集合，存储可重复元素，自动排序。
特点：元素可重复，自动排序。
时间复杂度：插入/删除/查找 O(log n)。
示例：  
```cpp
#include <set>
#include <iostream>
int main() {
    std::multiset<int> ms = {3, 1, 4, 1, 5};
    ms.insert(2);
    std::cout << *ms.begin() << std::endl; // 输出 1
    return 0;
}  
```
## map
描述：有序映射，存储键值对，键唯一，自动排序。
特点：键唯一，自动排序。
时间复杂度：插入/删除/查找 O(log n)。
示例：  
```cpp
#include <map>
#include <iostream>
int main() {
    std::map<int, std::string> m = {{1, "one"}, {2, "two"}, {3, "three"}};
    m[4] = "four";
    std::cout << m[2] << std::endl; // 输出 two
    return 0;
}
```
## multimap
描述：有序映射，存储可重复键的键值对，自动排序。
特点：键可重复，自动排序。
时间复杂度：插入/删除/查找 O(log n)。
示例：  
```cpp
#include <map>
#include <iostream>
int main() {
    std::multimap<int, std::string> mm = {{1, "one"}, {2, "two"}, {2, "deux"}};
    mm.insert({3, "three"});
    auto range = mm.equal_range(2);
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->second << " "; // 输出 two deux
    }
    return 0;
}  
```
# 无序容器
## unordered_set
描述：无序集合，存储唯一元素，基于哈希表。
特点：元素唯一，无序存储。
时间复杂度：插入/删除/查找 O(1)（平均）。
示例：  
```cpp
#include <unordered_set>
#include <iostream>
int main() {
    std::unordered_set<int> us = {3, 1, 4, 1, 5};
    us.insert(2);
    std::cout << *us.begin() << std::endl; // 输出无序
    return 0;
}  
```
## unordered_multiset
描述：无序集合，存储可重复元素，基于哈希表。
特点：元素可重复，无序存储。
时间复杂度：插入/删除/查找 O(1)（平均）。
示例：  
```cpp
#include <unordered_set>
#include <iostream>
int main() {
    std::unordered_multiset<int> ums = {3, 1, 4, 1, 5};
    ums.insert(2);
    std::cout << *ums.begin() << std::endl; // 输出无序
    return 0;
}  
```
## unordered_map
描述：无序映射，存储键值对，键唯一，基于哈希表。
特点：键唯一，无序存储。
时间复杂度：插入/删除/查找 O(1)（平均）。
示例：  
```cpp
#include <unordered_map>
#include <iostream>
int main() {
    std::unordered_map<int, std::string> um = {{1, "one"}, {2, "two"}, {3, "three"}};
    um[4] = "four";
    std::cout << um[2] << std::endl; // 输出 two
    return 0;
}  
```
## unordered_multimap
描述：无序映射，存储可重复键的键值对，基于哈希表。
特点：键可重复，无序存储。
时间复杂度：插入/删除/查找 O(1)（平均）。
示例：  
```cpp
#include <unordered_map>
#include <iostream>
int main() {
    std::unordered_multimap<int, std::string> umm = {{1, "one"}, {2, "two"}, {2, "deux"}};
    umm.insert({3, "three"});
    auto range = umm.equal_range(2);
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->second << " "; // 输出 two deux
    }
    return 0;
}    
```
# 容器适配器
## stack
描述：栈，后进先出（LIFO）。
特点：只允许在一端插入和删除元素。
时间复杂度：插入/删除 O(1)。
示例：  
```cpp
#include <stack>
#include <iostream>
int main() {
    std::stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    std::cout << s.top() << std::endl; // 输出 3
    s.pop();
    std::cout << s.top() << std::endl; // 输出 2
    return 0;
}  
```
## queue
描述：队列，先进先出（FIFO）。
特点：只允许在一端插入，在另一端删除元素。
时间复杂度：插入/删除 O(1)。
示例：  
```cpp
#include <queue>
#include <iostream>
int main() {
    std::queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);
    std::cout << q.front() << std::endl; // 输出 1
    q.pop();
    std::cout << q.front() << std::endl; // 输出 2
    return 0;
}  
```
## priority_queue
描述：优先队列，元素按优先级排序。
特点：最大元素优先出队。
时间复杂度：插入 O(log n)，删除 O(log n)。
示例：  
```cpp
#include <queue>
#include <iostream>
int main() {
    std::priority_queue<int> pq;
    pq.push(1);
    pq.push(3);
    pq.push(2);
    std::cout << pq.top() << std::endl; // 输出 3
    pq.pop();
    std::cout << pq.top() << std::endl; // 输出 2
    return 0;
}  
```
总结
STL 提供了多种容器，每种容器都有其独特的特点和适用场景。选择合适的容器可以提高程序的性能和可读性。