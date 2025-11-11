### lambda表达式需要通过self进行递归  
  
```cpp  
#include <iostream>
using namespace std;

int main() {
    // 使用指针实现递归调用
    auto factorial = [](int n, auto& self) -> int {
        if (n <= 1) return 1;
        return n * self(n - 1, self); // 递归调用
    };

    cout << "Factorial of 5: " << factorial(5, factorial) << endl; // 输出 120
    return 0;
}  
```