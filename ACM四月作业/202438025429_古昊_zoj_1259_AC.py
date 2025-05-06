import sys


first_case = True
line = sys.stdin.readline()
while True:
    # line = sys.stdin.readline()
    if not line:
        break
    L = int(line.strip())
    if L == 0:
        break
    if not first_case:
        print()
    first_case = False
    
    q1 = list(range(1, L+1))
    first_answer = True
    
    while True:
        line = sys.stdin.readline().strip()
        if line == '0':
            break
        if not line:
            continue
        q2 = list(map(int, line.split()))
        
        s1 = []
        q1_copy = q1.copy()
        valid = True
        
        for num in q2:
            while True:
                if q1_copy and num == q1_copy[0]:
                    q1_copy.pop(0)
                    break
                elif s1 and num == s1[-1]:
                    s1.pop()
                    break
                elif q1_copy:
                    s1.append(q1_copy.pop(0))
                else:
                    valid = False
                    break
            if not valid:
                break
        
        print("Yes" if valid else "No")
        first_answer = False 
    line = sys.stdin.readline()
    if L != 0:print()



# #include<iostream>
# #include<queue>
# #include<stack>

# using std::cin;using std::cout;
# using std::queue;
# using std::stack;


# int main (){
#   //std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#   int L;cin>>L;
#   bool ko=false;
#   while(L!=0){
#     if(ko)cout<<'\n';
#     else ko=true;
#     auto solve=[&](){
#       queue<int> q1,q2;
#       int num;
#       bool koao=false;
            
#       for(int i=1;i<=L;++i){
#         q1.push(i);
#       }

#       auto psh=[&](){
#          // int num;
#         while(true){
#           q2.push(num);
#           if(cin.peek()=='\n')break;
#           cin>>num;
#         }
#         return;
#       };

#       auto pan=[&](queue<int> q1)->bool{
#         stack<int> s1;
#         int tp;
#         while(!q2.empty()){
#           tp=q2.front();
#           if(tp!=q1.front()&&(s1.empty()||tp!=s1.top())){
#             if(q1.empty())break;
#             s1.push(q1.front());
#             q1.pop();
#           }else if(tp==q1.front()){
#             q2.pop();q1.pop();
#           }else if(tp==s1.top()){
#             q2.pop();s1.pop();
#           }
#         }
#         if(!q2.empty())return false;
#         else return true;
#       };

#       while (true){
#         cin>>num;
#         if(num==0)return;
#         q2=queue<int>();
#         if(koao)cout<<'\n';
#         else koao=true;
#         psh();
#         if(pan(q1))cout<<"Yes";
#         else cout<<"No";
#       }
      
#     };

#     solve();
#     cin>>L;
#     if(L!=0)cout<<'\n';
#   }
#   return 0;
# }