matrix = {}

def solve(s):
    if len(s) == 1:
        print(0)
        return

    ans = 0
    pos = 0

    def is_p():
        nonlocal pos, ans
        tmp = [None, None]

        if pos >= len(s):
            return (-1, -1)

        if s[pos] == '(':
            pos += 1
            tmp[0] = is_p()
            if tmp[0] == (-1, -1):
                return (-1, -1)
        else:
            if s[pos] not in matrix:
                return (-1, -1)
            tmp[0] = matrix[s[pos]]
            pos += 1

        if s[pos] == '(':
            pos += 1
            tmp[1] = is_p()
            if tmp[1] == (-1, -1):
                return (-1, -1)
        else:
            if s[pos] not in matrix:
                return (-1, -1)
            tmp[1] = matrix[s[pos]]
            pos += 1

        if pos >= len(s) or s[pos] != ')':
            return (-1, -1)
        pos += 1

        if tmp[0][1] != tmp[1][0]:
            return (-1, -1)

        # 计算矩阵乘法的代价
        ans += tmp[0][0] * tmp[0][1] * tmp[1][1]
        return (tmp[0][0], tmp[1][1])

    res = is_p()
    if res[0] == -1:
        print("error")
    else:
        print(ans)

T = int(input())
for _ in range(T):
    c, a, b = input().split()
    matrix[c] = (int(a), int(b))

while True:
    try:
        s = input()
        if not s.strip():
            break
        solve(s)
    except EOFError:
        break

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
