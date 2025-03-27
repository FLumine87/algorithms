#include<iostream>
#include<cmath>
#include<string>

using std::string;
using std::cin;using std::cout;

void solve(const int n){
    bool ans_l[15]={false};
    string s;

    auto zhuanhuan =[&s](int n,const int& i){
        while(n>0){
            s+=(n%i)+'0';
            n=n/i;
        }
    };

    auto is_huiwen =[&]()->bool{
        int a=0;int b=s.size()-1;
        while(a<b){
            if(s[a]!=s[b])return false;
            ++a;--b;
        }
        return true;
    };
    
    for(int i=0;i<15;++i){
        zhuanhuan(n,i+2);
        if(is_huiwen())ans_l[i]=true;
        s="";
    }

    string ans="";
    for (auto e=0;e<15;++e){
        if(ans_l[e]){
            ans+=std::to_string(e+2);ans+=" ";
        }
    }
    if(ans.size()){
        ans.pop_back();
        cout<<"Number "<<n<<" is palindrom in basis "<<ans<<"\n";
    }
    else{
        cout<<"Number "<<n<<" is not a palindrom\n";
    }
}

int main(){
    std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n;
    cin>>n;
    while(n!=0){
        solve(n);
        cin>>n;
    }
    return 0;
}