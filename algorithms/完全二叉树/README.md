>完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（从第 0 层开始），则该层包含 1~ 2^h 个节点。  
  
由定义可知，可以用位运算进行二分查找    

下面的代码是路径查找的方法，用于所有的二叉树，但非完全二叉树要转换成完全来做  
```CPP  
        int bits = 1 << (level - 1);
        while (node != nullptr && bits > 0) {
            if (!(bits & key)) {
                node = node->left;
            } else {
                node = node->right;
            }
            bits >>= 1;
        }
        return node != nullptr;
```  
  
对上面的解读：关键在于掩码为1000……  
因此每次右移一位即可遍历每一个方向  
注意：掩码少一位，因为要从第二位开始遍历

## 以下是ai生成  
1. 完全二叉树的节点编号与路径
在完全二叉树中，节点可以按照层次从上到下、从左到右进行编号：

根节点编号为 1。
左子节点编号为 2 * k，右子节点编号为 2 * k + 1（k 是父节点的编号）。
例如：

节点编号为：1, 2, 3, 4, 5, 6。
每个节点的编号可以用二进制表示：

节点 1：1（二进制 1）
节点 2：10（二进制 10）
节点 3：11（二进制 11）
节点 4：100（二进制 100）
节点 5：101（二进制 101）
节点 6：110（二进制 110）
路径特性：

从根节点到某个节点的路径可以通过该节点编号的二进制表示来确定：
二进制的每一位（从高位到低位）表示路径的方向：
0 表示向左。
1 表示向右。

        1
      /   \
     2     3
    / \   /
   4   5 6

2. 掩码 bits 的作用
掩码 bits 是一个二进制数，用于逐位检查目标节点编号的路径方向。

代码片段
工作原理
初始化掩码：

level 是树的高度（从根节点到目标节点的层数）。
1 << (level - 1) 表示将 1 左移 level - 1 位，生成一个最高位为 1 的二进制数。
例如：
如果 level = 3，则 bits = 1 << 2 = 100（二进制）。
逐位检查路径：

bits & key 用于检查目标节点编号 key 的当前位：
如果结果为 0，说明当前位是 0，路径向左。
如果结果不为 0，说明当前位是 1，路径向右。
根据结果，更新当前节点为左子节点或右子节点。
更新掩码：

每次检查完一位后，将掩码右移一位，准备检查下一位。
终止条件：

当掩码 bits 为 0 时，说明所有路径位都已检查完毕。
如果 node 不为 nullptr，说明目标节点存在；否则目标节点不存在。
3. 示例分析
示例 1：检查节点 5 是否存在
假设完全二叉树如下：

节点编号为：1, 2, 3, 4, 5, 6。
节点 5 的编号为 101（二进制）。
树的高度 level = 3。
步骤：

初始化掩码：

逐位检查路径：

第一位（100 & 101 = 100）：

当前位为 1，路径向右。
更新 node = node->right（从节点 1 到节点 3）。
更新 bits >>= 1，bits = 010。
第二位（010 & 101 = 000）：

当前位为 0，路径向左。
更新 node = node->left（从节点 3 到节点 5）。
更新 bits >>= 1，bits = 001。
第三位（001 & 101 = 001）：

当前位为 1，路径向右。
更新 node = node->right（节点 5 没有右子节点，node = nullptr）。
更新 bits >>= 1，bits = 000。
返回结果：

如果 node != nullptr，说明节点存在；否则不存在。
4. 总结
掩码 bits 的作用是逐位检查目标节点编号的路径方向。它通过以下步骤实现：

初始化掩码为 1 << (level - 1)，从最高位开始检查路径。
使用 bits & key 判断当前位是 0（向左）还是 1（向右）。
每次检查后，将掩码右移一位，直到所有路径位都检查完毕。
这种方法利用了完全二叉树的特性，通过位运算高效地确定路径，避免了递归或复杂的逻辑判断。

5. 优势
高效：
通过位运算直接确定路径方向，时间复杂度为 O(log(n))。
简洁：
使用掩码和位运算代替复杂的条件判断，代码简洁且易于理解。
适用于完全二叉树：
这种方法依赖于完全二叉树的节点编号特性，适用于完全二叉树的路径查找问题。