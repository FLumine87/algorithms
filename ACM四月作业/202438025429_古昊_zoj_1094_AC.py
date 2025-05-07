from typing import Dict, Tuple

def solve(s: str, matrix: Dict[str, Tuple[int, int]]) -> None:
    if len(s) == 1:
        print(0)
        return
    
    stack = []
    total = 0
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c.isalpha():
            stack.append(matrix[c])
        elif c == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            if not stack:
                print("error")
                return
            stack.pop()  # 弹出左括号
            
            temp.reverse()
            if len(temp) < 2:
                print("error")
                return
            
            # 计算矩阵链乘法
            current = temp[0]
            for mat in temp[1:]:
                if current[1] != mat[0]:
                    print("error")
                    return
                total += current[0] * current[1] * mat[1]
                current = (current[0], mat[1])
            stack.append(current)
    
    if len(stack) != 1 or isinstance(stack[0], str):
        print("error")
        return
    print(total)

n = int(input())
matrix_info: Dict[str, Tuple[int, int]] = {}
for _ in range(n):
    c, a, b = input().split()
    matrix_info[c] = (int(a), int(b))

try:
    while True:
        s = input().strip()
        if not s:
            continue
        solve(s, matrix_info)
except EOFError:
        pass

# #include<iostream>
# #include<stack>
# #include<unordered_map>
# #include<utility>
# #include<string>

# typedef std::pair<int,int> PII;

# using std::unordered_map;using std::string;
# using std::cout;using std::cin;using std::stack;
# using std::make_pair;

# unordered_map<char,PII> martix;

# void solve(string& s){
#     if(s.size()==1){
#         cout<<0<<'\n';
#         return;
#     }

#     long long int ans=0;
#     int pos=1;

#     auto is_p=[&](auto& self)->PII{
#         std::pair<PII,PII> tmp;
#         if(s[pos]=='('){
#             ++pos;
#             tmp.first=self(self);
#             if (tmp.first == make_pair(-1, -1)) return make_pair(-1, -1);            
#         }else{
#             tmp.first=martix[s[pos]];
#             pos++;
#         }
#         if(s[pos]=='('){
#             ++pos;
#             tmp.second=self(self);
#             if (tmp.second==make_pair(-1,-1))return make_pair(-1,-1);  
#         }else{
#             tmp.second=martix[s[pos]];
#             pos++;
#         }
#         ++pos;
#         if(tmp.first.second!=tmp.second.first)return make_pair(-1,-1);
#         ans+=tmp.first.first*tmp.first.second*tmp.second.second;
#         return make_pair(tmp.first.first,tmp.second.second);
#     };



#     PII res=is_p(is_p);
#     if(res.first==-1)cout<<"error"<<'\n';
#     else cout<<ans<<'\n';
#     return;
# }    

# int main(){
#     std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#     int T;cin>>T;
#     while(T--){
#         // inma();
#         char c;int a,b;
#         cin>>c>>a>>b;
#         PII an={a,b};
#         martix[c]=an;
#     }
#     string s;
#     while(cin>>s){
#       // while(std::getline(cin,s))
#         // if(s.empty())break;
#         solve(s);
#     }
#     return 0;
# }
