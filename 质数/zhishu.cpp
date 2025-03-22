#include <iostream>
#include <cmath>

bool isPrime(int n) {
    // 1. 小于等于 1 的数不是质数
    if (n <= 1) return false;

    // 2. 2 和 3 是质数
    if (n <= 3) return true;

    // 3. 排除能被 2 或 3 整除的数
    if (n % 2 == 0 || n % 3 == 0) return false;

    // 4. 试除法优化：检查到 sqrt(n)
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }

    // 5. 如果没有找到因数，则是质数
    return true;
}

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;

    if (isPrime(num)) {
        std::cout << num << " is a prime number.\n";
    } else {
        std::cout << num << " is not a prime number.\n";
    }

    return 0;
}