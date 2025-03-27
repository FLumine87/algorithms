# 进制转换
```cpp  
    auto zhuanhuan =[&s](int n,const int& i){
        while(n>0){
            s+=(n%i)+'0';
            n=n/i;
        }
    };
```  
但要注意了，+'0'后的字符串只能用来判断回文，不满足真正的16进制等。