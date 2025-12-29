| 函数        | 语法                                                          | 功能描述            |
| --------- | ----------------------------------------------------------- | --------------- |
| `strlen`  | `size_t strlen(const char* str);`                           | 返回字符串长度（不含'\0'） |
| `strcpy`  | `char* strcpy(char* dest, const char* src);`                | 复制字符串（包括'\0'）   |
| `strncpy` | `char* strncpy(char* dest, const char* src, size_t n);`     | 安全复制，最多n个字符     |
| `strcat`  | `char* strcat(char* dest, const char* src);`                | 将src追加到dest末尾   |
| `strncat` | `char* strncat(char* dest, const char* src, size_t n);`     | 安全追加，最多n个字符     |
| `strcmp`  | `int strcmp(const char* s1, const char* s2);`               | 比较两个字符串         |
| `strncmp` | `int strncmp(const char* s1, const char* s2, size_t n);`    | 比较前n个字符         |
| `strchr`  | `char* strchr(const char* str, int ch);`                    | 查找字符首次出现位置      |
| `strrchr` | `char* strrchr(const char* str, int ch);`                   | 查找字符最后出现位置      |
| `strstr`  | `char* strstr(const char* haystack, const char* needle);`   | 查找子串首次出现        |
| `strtok`  | `char* strtok(char* str, const char* delim);`               | 分割字符串为标记        |
| `memset`  | `void* memset(void* ptr, int value, size_t num);`           | 设置内存块的值         |
| `memcpy`  | `void* memcpy(void* dest, const void* src, size_t n);`      | 复制内存块           |
| `memmove` | `void* memmove(void* dest, const void* src, size_t n);`     | 安全复制（可重叠）       |
| `memcmp`  | `int memcmp(const void* ptr1, const void* ptr2, size_t n);` | 比较内存块           |

