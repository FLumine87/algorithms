def solve(b=0):
    t = int(input())
    if t == 0:
        print("both")
        return
    
    v1 = [0] * t
    v2 = [0] * t
    
    # 读取一行并分割为多个整数
    v1_input = input().split()
    for i in range(t):
        v1[i] = int(v1_input[i])
    
    v2_input = input().split()
    for i in range(t):
        v2[i] = int(v2_input[i])
    
    def is_stack():
        it1 = 0
        it2 = t - 1
        while it1 < t and it2 >= 0:
            if v1[it1] != v2[it2]:
                return False
            it1 += 1
            it2 -= 1
        return True
    
    def is_queue():
        return v1 == v2
    
    def ot():
        whe = [False, False]
        whe[0] = is_stack()
        whe[1] = is_queue()
        
        if not whe[0] and not whe[1]:
            return -1
        elif whe[0] and whe[1]:
            return 0
        elif whe[0] and not whe[1]:
            return 1
        else:
            return 22
    
    res = ot()
    
    if b == 1:
        if res == -1:
            print("neither", end='')
        elif res == 0:
            print("both", end='')
        elif res == 1:
            print("stack", end='')
        else:
            print("queue", end='')
    else:
        if res == -1:
            print("neither")
        elif res == 0:
            print("both")
        elif res == 1:
            print("stack")
        else:
            print("queue")

T = int(input())
for _ in range(T):
    if _ == T - 1:
        solve(1)
    else:
        solve()

# #include<iostream>
# #include<vector>

# using std::cin;using std::cout;
# using std::vector;

# void solve(int b=0){
#     int t;
#     cin>>t;
#     if(t==0){
#         cout<<"both\n";
#         return;
#     }
#     vector<int> v1(t);
#     vector<int> v2(t);
#     auto is_stack=[&]()->bool{
#         auto it1=v1.begin();
#         auto it2=v2.rbegin();
#         while(it1 != v1.end() && it2!=v2.rend()){
#             if(*it1!=*it2)return false;
#             ++it1; ++it2;
#         }
#         return true;
#     };

#     auto is_queue=[&]()->bool{
#         if(v1==v2)return true;
#         else return false;
#     };
    
#     auto ot=[&]()->int{
#         vector<bool> whe(2);
#         if(is_stack())whe[0]=true;
#         else whe[0]=false;
#         if(is_queue())whe[1]=true;
#         else whe[1]=false;
#         if(whe[0]==false&&whe[1]==false)return -1;
#         else if(whe[0]==true&&whe[1]==true)return 0;
#         else if(whe[0]==true&&whe[1]==false)return 1;
#         else return 22;
#     };

#     for(int i=0;i<t;++i){
#         cin>>v1[i];
#     }
#     for(int i=0;i<t;++i){
#         cin>>v2[i];
#     }
#     int res=ot();
#     if(b==1){
#         if(res==-1){
#         cout<<"neither";return;
#         }else if(res==0){
#             cout<<"both";return;
#         }else if(res==1){
#             cout<<"stack";return;
#         }else{
#             cout<<"queue";return;
#     }
#     }
#     if(res==-1){
#         cout<<"neither\n";return;
#     }else if(res==0){
#         cout<<"both\n";return;
#     }else if(res==1){
#         cout<<"stack\n";return;
#     }else{
#         cout<<"queue\n";return;
#     }
# }

# int main(){
#     std::ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);
#     int T;
#     cin>>T;
#     while(T--){
#         if(T==0){
#             solve(1);
#             continue;
#         }
#         solve();
#     }
#     return 0;
# }